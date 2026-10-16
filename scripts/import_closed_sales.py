#!/usr/bin/env python3
"""Merge closed-sales CSVs into listings.json.

The site reads one file, listings.json. On-market rows (Active, Coming Soon,
Pending, Under Contract) stay as they are. This importer replaces Sold rows
with the union of the CSV files you pass.

The team export is one file. It already includes every agent and has
co-listings merged into a single row. Pass that file by itself. Passing an
older per-agent export alongside it can duplicate closings.

PhotoURL is ignored. A front photo already saved for that MLS in
listings.json is kept, on listing-side and buyer-side rows. Rows without a
saved photo stay image null. Buyer-side rows without a photo keep
photoAllowed false.

TeamMember is the public credit on the card ("Sold by Trevor Stuck"). Names
are the ones used on the site, not the longer MLS legal names. ListAgent,
CoListAgent, and BuyerAgent are not copied onto the card.

Do not commit the source CSVs. They include private agent fields. The JSON
written here has only the public card fields.

Usage:
  python3 scripts/import_closed_sales.py adg-team-closed-12mo.csv
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LISTINGS_PATH = ROOT / "listings.json"
BROKERAGE = "Coldwell Banker Realty"

PROPERTY_TAGS = {
    "residential": "Residential",
    "land": "Land",
    "commercial sale": "Commercial",
    "commercial": "Commercial",
    "multi-family": "Multi-Family",
    "multifamily": "Multi-Family",
}

# MLS legal names -> the name on adamdruckgroup.com.
DISPLAY_NAMES = {
    "adam druck": "Adam Druck",
    "trevor logan stuck": "Trevor Stuck",
    "trevor stuck": "Trevor Stuck",
    "zachery e keller": "Zach Keller",
    "zachery keller": "Zach Keller",
    "zach keller": "Zach Keller",
    "katie a kopp": "Katie Kopp",
    "katie kopp": "Katie Kopp",
    "tyler john zeller": "Tyler Zeller",
    "tyler zeller": "Tyler Zeller",
}


def norm_space(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip())


def address_key(address: str, unit: str, city: str, zip_code: str) -> tuple[str, str, str, str]:
    street = norm_space(address).lower().replace(".", "")
    street = re.sub(r",\s*", ", ", street)
    return (street, norm_space(unit).lower(), norm_space(city).lower(), norm_space(zip_code))


def is_excluded_lot(address: str) -> bool:
    """13925 and 13975 Wolf Rd were lot sales and clash with the active house."""
    street = norm_space(address).lower().replace(".", "")
    return bool(re.match(r"13925\s+wolf\b", street) or re.match(r"13975\s+wolf\b", street))


def display_address(address: str, unit: str) -> str:
    street = re.sub(r"\s*,\s*", ", ", norm_space(address))
    unit = norm_space(unit)
    if unit:
        return f"{street}, Unit {unit}"
    return street


def number_or_none(value: str):
    text = (value or "").strip().replace(",", "")
    if not text:
        return None
    number = float(text)
    if number.is_integer():
        return int(number)
    return number


def property_tag(value: str) -> str:
    raw = norm_space(value)
    return PROPERTY_TAGS.get(raw.lower(), raw or "Residential")


def side_of(value: str) -> str:
    raw = norm_space(value).lower().replace(" ", "")
    if raw == "buyer":
        return "buyer"
    # "Both" and "Listing+Buyer" mean the team listed it and brought the buyer.
    # Show that closing once, as the listing.
    if raw in {"listing", "both", "listing+buyer"}:
        return "listing"
    raise ValueError(f"Unknown AdamSide value: {value!r}")


def display_agent(name: str) -> str:
    key = norm_space(name).lower().replace(".", "")
    key = re.sub(r"\s+", " ", key).strip()
    shown = DISPLAY_NAMES.get(key)
    if shown:
        return shown
    print(f"Warning: team member {name!r} has no public display name.", file=sys.stderr)
    return norm_space(name)


def agents_of(value: str) -> list[str]:
    names = []
    for part in (value or "").split(";"):
        part = norm_space(part)
        if not part:
            continue
        shown = display_agent(part)
        if shown not in names:
            names.append(shown)
    return names


def read_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def prepare_rows(csv_paths: list[Path]) -> tuple[list[dict], dict]:
    rows = []
    stats = {
        "read": 0,
        "excluded_wolf_lots": 0,
        "dropped_buyer_duplicates": 0,
        "dropped_mls_duplicates": 0,
        "missing_team_member": 0,
        "files": [str(path) for path in csv_paths],
    }
    for path in csv_paths:
        for row in read_csv(path):
            stats["read"] += 1
            if is_excluded_lot(row.get("Address", "")):
                stats["excluded_wolf_lots"] += 1
                continue
            side_of(row.get("AdamSide", ""))
            rows.append(row)

    grouped: dict[tuple, list[dict]] = {}
    for row in rows:
        key = address_key(row.get("Address", ""), row.get("Unit", ""), row.get("City", ""), row.get("Zip", ""))
        grouped.setdefault(key, []).append(row)

    kept = []
    for group in grouped.values():
        sides = {side_of(row.get("AdamSide", "")) for row in group}
        if "listing" in sides and "buyer" in sides:
            listing_rows = [row for row in group if side_of(row.get("AdamSide", "")) == "listing"]
            stats["dropped_buyer_duplicates"] += len(group) - len(listing_rows)
            kept.extend(listing_rows)
        else:
            kept.extend(group)

    by_mls: dict[str, dict] = {}
    order: list[str] = []
    for row in kept:
        mls = norm_space(row.get("MLS", ""))
        if not mls:
            order.append(f"__row_{len(order)}")
            by_mls[order[-1]] = row
            continue
        if mls in by_mls:
            stats["dropped_mls_duplicates"] += 1
            if side_of(by_mls[mls].get("AdamSide", "")) != "listing" and side_of(row.get("AdamSide", "")) == "listing":
                by_mls[mls] = row
            continue
        by_mls[mls] = row
        order.append(mls)
    return [by_mls[key] for key in order], stats


def sold_record(row: dict, previous: dict | None) -> dict:
    side = side_of(row.get("AdamSide", ""))
    agents = agents_of(row.get("TeamMember", ""))
    photo_allowed = side == "listing"
    image = None
    image_alt = None
    # A front photo already saved for this MLS stays, including a buyer-side
    # card. The export's PhotoURL is never copied. Rows with no saved photo
    # stay image null, and buyer-side rows in that case keep photoAllowed false.
    if previous:
        previous_image = previous.get("image")
        if isinstance(previous_image, str) and previous_image.strip():
            image = previous_image.strip()
            alt = previous.get("imageAlt")
            image_alt = alt if isinstance(alt, str) and alt.strip() else None
            photo_allowed = True

    beds = number_or_none(row.get("Beds", ""))
    baths_full = number_or_none(row.get("BathsFull", ""))
    baths_half = number_or_none(row.get("BathsHalf", ""))
    if baths_full is None and baths_half is None:
        baths_half_out = None
    else:
        baths_half_out = 0 if baths_half is None else baths_half
        baths_full = 0 if baths_full is None else baths_full

    return {
        "mls": norm_space(row.get("MLS", "")),
        "status": "Sold",
        "side": side,
        "agents": agents,
        "propertyType": property_tag(row.get("PropertyType", "")),
        "price": number_or_none(row.get("ListPrice", "")),
        "soldPrice": number_or_none(row.get("ClosePrice", "")),
        "closeDate": norm_space(row.get("CloseDate", "")) or None,
        "pendingDate": None,
        "address": display_address(row.get("Address", ""), row.get("Unit", "")),
        "city": norm_space(row.get("City", "")),
        "state": norm_space(row.get("State", "")),
        "zip": norm_space(row.get("Zip", "")),
        "beds": beds,
        "bathsFull": baths_full,
        "bathsHalf": baths_half_out,
        "sqft": number_or_none(row.get("SqftAboveGrade", "")),
        "listed": None,
        "brokerage": BROKERAGE,
        "url": None,
        "image": image,
        "imageAlt": image_alt,
        "photoAllowed": photo_allowed,
    }


def merge(csv_paths: list[Path], listings_path: Path = LISTINGS_PATH) -> dict:
    data = json.loads(listings_path.read_text(encoding="utf-8"))
    existing = data.get("listings") or []
    previous_by_mls = {str(row.get("mls")): row for row in existing if row.get("mls")}
    raw_rows, stats = prepare_rows(csv_paths)
    sold = [sold_record(row, previous_by_mls.get(norm_space(row.get("MLS", "")))) for row in raw_rows]
    sold.sort(key=lambda row: row.get("closeDate") or "", reverse=True)
    sold_mls = {row["mls"] for row in sold}
    # Closed file wins over an on-market row with the same MLS.
    kept = []
    for row in existing:
        status = norm_space(str(row.get("status", ""))).lower()
        if status == "sold":
            continue
        if str(row.get("mls")) in sold_mls:
            continue
        kept.append(row)
    data["listings"] = kept + sold
    data["updated"] = "2026-10-16"
    data["source"] = (
        "On-market rows come from the Bright MLS export. "
        "Sold rows come from the team closed-sales importer."
    )
    data["notes"] = (
        "One file drives Newest, Pending, and Recently Sold. "
        "Status Active, Coming Soon, or New Listing appears under Newest. "
        "Status Pending or Under Contract appears under Pending. "
        "Status Sold appears under Recently Sold. "
        "Sold rows are the whole Adam Druck Group, refreshed by scripts/import_closed_sales.py. "
        "Each sold row's agents list is the public credit, shown as Sold by. "
        "A sold card shows a front photo when image is a saved photo of that property. "
        "Rows without a usable photo keep image null and the card shows the Adam Druck Group mark. "
        "Buyer-side rows stay side buyer. "
        "Do not invent prices, dates, or photos."
    )
    listings_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    stats["sold"] = len(sold)
    stats["listing_side"] = sum(1 for row in sold if row["side"] == "listing")
    stats["buyer_side"] = sum(1 for row in sold if row["side"] == "buyer")
    stats["with_photo"] = sum(1 for row in sold if row.get("image"))
    stats["co_listed"] = sum(1 for row in sold if len(row.get("agents") or []) > 1)
    credit = {}
    for row in sold:
        if not row.get("agents"):
            stats["missing_team_member"] += 1
        for name in row.get("agents") or []:
            credit[name] = credit.get(name, 0) + 1
    stats["agent_credits"] = credit
    return stats


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: python3 scripts/import_closed_sales.py file1.csv [file2.csv ...]", file=sys.stderr)
        return 1
    paths = [Path(arg) for arg in argv[1:]]
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        print("Missing file(s): " + ", ".join(missing), file=sys.stderr)
        return 1
    stats = merge(paths)
    print(
        f"Read {stats['read']} rows from {len(paths)} file(s). "
        f"Wrote {stats['sold']} sold rows "
        f"({stats['listing_side']} listing side, {stats['buyer_side']} buyer side). "
        f"Left out {stats['excluded_wolf_lots']} Wolf Rd lot sale(s). "
        f"Dropped {stats['dropped_buyer_duplicates']} buyer-side duplicate(s) "
        f"and {stats['dropped_mls_duplicates']} duplicate MLS row(s). "
        f"Co-listed: {stats['co_listed']}. "
        f"Photos on sold cards: {stats['with_photo']}. "
        f"Credits: {stats['agent_credits']}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

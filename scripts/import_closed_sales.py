#!/usr/bin/env python3
"""Merge closed-sales CSVs into listings.json.

The site reads one file, listings.json. On-market rows (Active, Coming Soon,
Pending, Under Contract) stay as they are. This importer replaces Sold rows
with the union of the CSV files you pass, so teammate exports in the same
format can be added by running the script again with every file included.

PhotoURL is ignored. Buyer-side sales never get a photo. Listing-side sales
keep photoAllowed true and image null unless a photo was already saved on
that MLS in listings.json.

Do not commit the source CSVs. They include private agent fields. The JSON
written here has only the public card fields.

Usage:
  python3 scripts/import_closed_sales.py adam.csv teammate.csv
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
    raw = norm_space(value).lower()
    if raw == "buyer":
        return "buyer"
    if raw in {"listing", "both"}:
        # "Both" is his listing and his buyer. Show it once, as the listing.
        return "listing"
    raise ValueError(f"Unknown AdamSide value: {value!r}")


def read_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def prepare_rows(csv_paths: list[Path]) -> tuple[list[dict], dict]:
    rows = []
    stats = {
        "read": 0,
        "excluded_wolf_lots": 0,
        "dropped_buyer_duplicates": 0,
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
    return kept, stats


def sold_record(row: dict, previous: dict | None) -> dict:
    side = side_of(row.get("AdamSide", ""))
    photo_allowed = side == "listing"
    image = None
    image_alt = None
    # A listing-side photo already saved for this MLS can stay.
    # A buyer-side sale never shows a photo, even if one was stored before.
    if photo_allowed and previous:
        previous_side = norm_space(str(previous.get("side", ""))).lower()
        previous_allowed = previous.get("photoAllowed") is not False and previous_side != "buyer"
        previous_image = previous.get("image")
        if previous_allowed and isinstance(previous_image, str) and previous_image.strip():
            image = previous_image.strip()
            alt = previous.get("imageAlt")
            image_alt = alt if isinstance(alt, str) and alt.strip() else None

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
    listings_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    stats["sold"] = len(sold)
    stats["listing_side"] = sum(1 for row in sold if row["side"] == "listing")
    stats["buyer_side"] = sum(1 for row in sold if row["side"] == "buyer")
    stats["with_photo"] = sum(1 for row in sold if row.get("image"))
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
        f"Dropped {stats['dropped_buyer_duplicates']} buyer-side duplicate(s). "
        f"Photos on sold cards: {stats['with_photo']}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

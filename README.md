# Adam Druck Group

Static site for [adamdruckgroup.com](https://adamdruckgroup.com), served by GitHub Pages.

## Listings

The home page and [sales.html](sales.html) both read [`listings.json`](listings.json). There is no live MLS or IDX feed. A live feed would need an IDX agreement approved by Adam's office.

One array, `listings`, drives every section. A daily update adds a row, removes a row, or changes `status` and the dates and prices that go with it.

| `status` | Where it shows | Sorted by |
| --- | --- | --- |
| `Active`, `Coming Soon`, `New Listing` | Newest listings, under the home page hero | `listed`, newest first |
| `Pending`, `Under Contract` | Pending, lower on the home page | `pendingDate`, newest first |
| `Sold` | Latest 6 on the home page, and all of them on `/sales.html` | `closeDate`, newest first |

`homepageSoldLimit` is how many sold cards the home page shows. Keep it between 6 and 9.

Every card shows **Coldwell Banker Realty**. The page fills that name in if `brokerage` is blank. Leave the Equal Housing Opportunity lines in place.

### Change a listing by hand

Edit `listings.json` only. Do not guess a price, date, bed count, or address.

To move a home from Newest to Pending, set `status` to `Pending` and set `pendingDate` to `YYYY-MM-DD`. To mark it sold by hand, set `status` to `Sold`, set `soldPrice` and `closeDate`, and set `side` to `listing` or `buyer`. The sold card uses `soldPrice` and `closeDate`, not the list price.

Remove a home by deleting its object. If it had photos, delete `images/listings/<mls-lowercase>/` when nothing else uses those files.

### Add a card photo

Active, Coming Soon, and Pending cards already have an `image` field. It is `null` until a photo is ready, and the card says "Photo coming soon." To fill one in:

1. Save a JPEG you can verify is that property as `images/listings/<mls-in-lowercase>/front.jpg`. About 1280 pixels on the long side, JPEG quality around 70.
2. Set these two fields on that listing and leave every other field alone:

```json
"image": "images/listings/payk2113324/front.jpg",
"imageAlt": "Front of 653 Broadway, Hanover, PA"
```

Use the lowercase MLS number in the path. `photoAllowed` stays `true` on these rows. One card photo is enough. Do not fill `gallery`.

These eight listings now use a photo from Adam's own gallery. `01.jpg` is the front, except 426 Jennifer Dr and 478 Rear Wasp St. Those `01` files are twilight shots with a replaced sky, so the card uses `02` instead: the daytime front on Jennifer, and the side entry on Wasp. A small Bright MLS mark sat in the bottom-left corner and was cropped off the lawn.

| MLS | Card photo |
| --- | --- |
| `PAYK2113324` | Front of 653 Broadway, Hanover |
| `PAAD2026056` | Front of 32 Quiet Creek Dr, Gettysburg |
| `PAAD2025752` | Front of 2581 Old Harrisburg Rd, Unit 31, Gettysburg |
| `PAYK2113022` | Front of 245 Abbey Dr, Mount Wolf |
| `PAYK2107306` | Front of 13 Maul Ave, Felton |
| `PAYK2109168` | Front of 251 Highview Dr, Airville |
| `PAYK2109526` | Daytime front of 426 Jennifer Dr, New Cumberland |
| `PALA2095588` | Side entry of 478 Rear Wasp St, Marietta |

13925 Wolf Rd already uses `images/listings/payk2113766/front.jpg` (the daytime front). Do not use the twilight front of that house. Do not set `image` on a sold row whose `side` is `buyer`.

### Add an on-market listing

Copy an existing Active or Pending object and replace the values from the MLS sheet.

- `price` is the list price as a number (`350000`, not `"$350,000"`).
- `beds`, `bathsFull`, and `bathsHalf` are counts. One full and one half is `1` and `1`, shown as `1.5 ba`.
- `sqft` is a number. Use null when the sheet has no square footage.
- `url` is the Moxi listing page when one exists. Otherwise use `searchUrl`.
- `image` is a path such as `images/listings/payk2113766/front.jpg`, or `null`.
- Use a photo only when you know it is that property. Resize it to about 1280 pixels on the long side, JPEG quality around 70. The card loads `image` only. `gallery` is optional and is not shown.
- The twilight front of 13925 Wolf Rd is AI-altered. Do not use it. The card photo is the daytime front.

### Sold rows and the importer

Closed sales are loaded with `scripts/import_closed_sales.py`. The team export is one CSV that already includes every agent. Co-listings are one row, with both names in `TeamMember` separated by a semicolon. Pass that file by itself. The script replaces the Sold rows with that set and leaves Active, Coming Soon, and Pending rows in place. If a closed MLS is still sitting in those rows, the closed row replaces it.

```bash
python3 scripts/import_closed_sales.py adg-team-closed-12mo.csv
```

Keep the CSVs out of this repo. They contain private agent remarks. The importer writes only the public card fields. It does not copy `ListAgent`, `CoListAgent`, `BuyerAgent`, or `PhotoURL`.

`TeamMember` becomes `agents`, using the names on this site:

| In the export | On the card |
| --- | --- |
| Adam Druck | Adam Druck |
| Trevor Logan Stuck | Trevor Stuck |
| Zachery E Keller | Zach Keller |
| Katie A. Kopp | Katie Kopp |
| Tyler John Zeller | Tyler Zeller |

A card with one name says "Sold by Trevor Stuck". A card with two says "Sold by Adam Druck and Trevor Stuck". `/sales.html` has a filter for those names. A co-listed sale shows up under each agent. Amanda Eisenhart is not a separate credit in this export. Her co-listed rows are already assigned to Adam in `TeamMember`.

Rules the importer already applies:

- 13925 Wolf Rd and 13975 Wolf Rd are left out. They were lot sales and would sit next to the active Wolf Rd house.
- If the same address was closed once as the listing and once as the buyer, the buyer row is dropped. 433 Valley St is kept once, as the listing.
- `AdamSide` of `Listing`, `Both`, or `Listing+Buyer` becomes `side: "listing"` and the card says "Listed by Adam Druck Group". `Buyer` becomes `side: "buyer"` and the card says "Represented the Buyer".
- Land and commercial sales are kept. `propertyType` is the tag on the card (`Land`, `Commercial`, `Multi-Family`, `Residential`).
- `PhotoURL` is ignored. Every sold card is photo-free until a real listing photo is added by hand.

### Photos on sold cards

Buyer-side rows must stay `side: "buyer"`, `photoAllowed: false`, and `image: null`. Those photos belong to the other brokerage, so the page will not render an image even if one is present.

Listing-side rows may set `image` later to a photo verified as that property. Leave `image` null until then. An import keeps a listing-side photo that was already saved for that MLS, and never copies a photo onto a buyer-side row.

### Fields

| Field | On-market | Sold |
| --- | --- | --- |
| `mls` | yes | yes |
| `status` | yes | `Sold` |
| `side` | `listing` | `listing` or `buyer` |
| `agents` | omit | public names, such as `["Trevor Stuck"]` |
| `propertyType` | yes | yes |
| `price` | list price | list price from the sheet; the card shows `soldPrice` |
| `soldPrice` | null | close price |
| `closeDate` | null | `YYYY-MM-DD` |
| `pendingDate` | set for Pending | null |
| `address`, `city`, `state`, `zip` | yes | yes |
| `beds`, `bathsFull`, `bathsHalf`, `sqft` | yes, or null | yes, or null |
| `listed` | `YYYY-MM-DD` | null |
| `brokerage` | `Coldwell Banker Realty` | `Coldwell Banker Realty` |
| `url` | Moxi page or search | null unless a real listing page is known |
| `image` | path or null | null, unless a verified listing-side photo is added |
| `photoAllowed` | true | true for listing side, false for buyer side |

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

Closed sales are loaded with `scripts/import_closed_sales.py`. Teammate files use the same CSV columns (`MLS`, `Address`, `Unit`, `City`, `State`, `Zip`, `PropertyType`, `Beds`, `BathsFull`, `BathsHalf`, `SqftAboveGrade`, `ListPrice`, `ClosePrice`, `CloseDate`, `AdamSide`). Pass every file that should be on the site in one command. The script replaces the Sold rows with that set and leaves Active, Coming Soon, and Pending rows in place. If a closed MLS is still sitting in those rows, the closed row replaces it.

```bash
python3 scripts/import_closed_sales.py adam.csv teammate.csv
```

Keep the CSVs out of this repo. They contain private agent remarks. The importer writes only the public card fields.

Rules the importer already applies:

- 13925 Wolf Rd and 13975 Wolf Rd are left out. They were lot sales and would sit next to the active Wolf Rd house.
- If the same address was closed once as the listing and once as the buyer, the buyer row is dropped. 433 Valley St is kept once, as the listing.
- `AdamSide` of `Listing` or `Both` becomes `side: "listing"` and the card says "Listed by Adam Druck Group". `Buyer` becomes `side: "buyer"` and the card says "Represented the Buyer".
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

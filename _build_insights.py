#!/usr/bin/env python3
"""Generate the six Insights articles as standalone pages under insights/.

Content policy: evergreen frameworks and program explainers only — no
perishable market statistics are baked into static pages. Where numbers
appear in the BRRRR walk-through they are round, clearly-labeled
illustrations, not client data.
"""
import os
import importlib.util

spec = importlib.util.spec_from_file_location(
    "shell_mod", os.path.join(os.path.dirname(__file__), "_page-shell.py")
)
shell_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(shell_mod)
shell = shell_mod.shell

OUT_DIR = os.path.join(os.path.dirname(__file__), "insights")


def article_body(eyebrow: str, title_html: str, dek: str, body_html: str) -> str:
    return f"""
<section class="page-lead">
  <div class="page-lead__inner">
    <p class="eyebrow page-lead__eyebrow">{eyebrow}</p>
    <h1 class="page-lead__title">{title_html}</h1>
    <p class="page-lead__lede">{dek}</p>
  </div>
</section>

<section class="section">
  <div class="section__inner" style="max-width: 720px;">
    <div style="color: var(--slate); font-size: 1.05rem; line-height: 1.75;">
{body_html}
    </div>
    <div style="margin-top: 3rem; padding: 2rem; background: var(--cream); border-left: 3px solid var(--celestial);">
      <p style="margin: 0 0 1rem; font-family: var(--serif); font-size: 1.15rem; color: var(--ink);">
        Want this applied to your situation — with live numbers instead of frameworks?
      </p>
      <a href="/contact.html#message" class="btn btn--primary">Talk to the Team</a>
      <a href="/home-value.html" class="btn btn--ghost" style="margin-left: 0.5rem;">What's My Home Worth?</a>
    </div>
    <p style="margin-top: 2rem;"><a href="/insights.html" style="color: var(--cb-blue);">&larr; All Insights</a></p>
  </div>
</section>
"""


H = lambda t: f'<h2 style="font-family: var(--serif); color: var(--ink); font-size: 1.5rem; margin: 2.2rem 0 0.8rem;">{t}</h2>'
P = lambda t: f'<p style="margin: 0 0 1.1rem;">{t}</p>'
LI = lambda *items: "<ul style='margin: 0 0 1.1rem; padding-left: 1.2rem;'>" + "".join(
    f"<li style='margin-bottom: 0.5rem;'>{i}</li>" for i in items
) + "</ul>"

ARTICLES = [
    {
        "slug": "york-county-market-indicators",
        "eyebrow": "Market Report",
        "title": 'Q1 York County: Inventory, Pricing &amp; What Spring <span class="italic">Actually Looks Like</span>',
        "meta_title": "How to Read the York County Market | Adam Druck Group",
        "dek": "The handful of numbers that actually predict what spring will do — and how to read them like an agent instead of a headline.",
        "body": (
            P("Every spring, national headlines declare the market is either roaring back or falling apart. Neither is ever quite true in York County — our market moves on a few local indicators that most coverage skips entirely. Here's what we actually watch, and how to read it.")
            + H("Months of inventory, not listing counts")
            + P("Raw “homes for sale” numbers mean nothing without the demand side. Months of inventory — how long the current supply would last at the current sales pace — is the single best signal. Under roughly four months, sellers hold leverage and well-priced homes draw multiple offers. Over six, buyers can negotiate. York County has spent most of the last several years firmly on the seller side of that line, which is why “wait for the crash” has been expensive advice here.")
            + H("List-to-sale ratio: the honesty meter")
            + P("When homes consistently close at or above list price, pricing strategy is working and demand is real. When the ratio slips, it usually shows up in this number before it shows up anywhere else — sellers chasing the market down with price cuts is a trailing symptom, not a leading signal.")
            + H("Days on market, by price band")
            + P("County-wide averages hide the story. Entry-level and mid-market homes in strong school districts move on a completely different clock than upper-bracket properties. If you're pricing a home, the DOM that matters is for <em>your</em> price band, <em>your</em> school district, this season — not the county average.")
            + H("The spring pattern")
            + P("York County's spring market reliably starts earlier than people expect — serious buyers are in motion by late February, well before the April yard-sign bloom. Listing just ahead of the wave, into thinner competition, routinely beats listing into the peak.")
            + P("We pull these numbers live from the MLS whenever we price a home or write an offer. If you want the current read for your street — not last quarter's, not the county average — that's a fifteen-minute conversation.")
        ),
    },
    {
        "slug": "seventy-percent-rule-reconsidered",
        "eyebrow": "Investor Guide",
        "title": 'The 70% Rule, Reconsidered: Flip Math for York&rsquo;s <span class="italic">Real Margins</span>',
        "meta_title": "The 70% Rule, Reconsidered — Flip Math for York County | Adam Druck Group",
        "dek": "The classic formula is a screening tool, not an underwrite. Here's where it breaks in Central Pennsylvania — and what we calculate instead.",
        "body": (
            P("Every flipping course teaches the same formula: pay no more than 70% of the after-repair value, minus rehab costs. It's a fine thirty-second screen. It is not an underwrite, and treating it like one is how first flips lose money in York County.")
            + H("What the 70% rule silently assumes")
            + P("The 30% margin is supposed to cover selling costs, holding costs, financing, and profit. But those aren't constants — they're variables that swing hard with price point. On a $450,000 flip, 30% leaves generous room. On a $140,000 York City rowhome, the fixed costs — transfer tax, utilities through a winter hold, insurance on a vacant property, two closings — eat a far bigger share of a far smaller margin.")
            + H("Where York deals actually differ")
            + LI(
                "<strong>Pennsylvania transfer tax</strong> is paid on both ends of a flip and is higher than most out-of-state formulas assume.",
                "<strong>Older housing stock</strong> — much of the county's value inventory predates 1950. Knob-and-tube, cast-iron stacks, and stone foundations don't care what your rehab-per-square-foot rule of thumb says.",
                "<strong>Price-band cliffs</strong> — an over-improved rowhome doesn't get its money back. ARV is capped by the block, not by the renovation budget.",
            )
            + H("What we run instead")
            + P("Every deal we bring an investor gets a full cost stack: purchase, itemized rehab, month-by-month carry, realistic financing costs, both sets of closing costs, and the sale-side commission — solved for net profit and cash-on-cash return, not a percentage screen. If a deal only works at 70% and falls apart at 72%, it was never a deal; it was a coin flip.")
            + P("We built internal tools that run this math in seconds, on every MLS listing and auction property in the county, every day. That's the deal flow our investors see.")
        ),
    },
    {
        "slug": "pa-first-time-buyer-programs",
        "eyebrow": "First-Time Buyers",
        "title": 'Pennsylvania First-Time Buyer Programs Most Lenders <span class="italic">Won&rsquo;t Mention</span>',
        "meta_title": "PA First-Time Buyer Programs Explained | Adam Druck Group",
        "dek": "PHFA loans, down-payment assistance, and closing-cost help — what exists, who qualifies, and why you have to ask.",
        "body": (
            P("The biggest myth in first-time buying is “you need 20% down.” In Pennsylvania, the honest number for many qualified buyers is a small fraction of that — sometimes close to zero out of pocket — because of state programs that plenty of loan officers simply never bring up.")
            + H("The PHFA family")
            + P("The Pennsylvania Housing Finance Agency runs the state's flagship programs. The Keystone Home Loan offers below-retail rates to buyers under income and purchase-price limits that most of York County fits comfortably. Layered on top, PHFA's assistance programs can put thousands toward your down payment and closing costs, often structured as a second loan with terms dramatically friendlier than saving for years while renting.")
            + H("Why lenders skip them")
            + P("PHFA loans involve more paperwork, training requirements, and thinner margins for the lender. A loan officer paid on volume has little incentive to slow down for them. That's not a conspiracy — it's an incentive structure — but it means the burden is on you (or your agent) to ask the question directly: “Am I eligible for PHFA programs, and will you write one?” Some excellent local lenders will; we keep a list.")
            + H("Beyond the state programs")
            + LI(
                "<strong>Seller assist</strong> — in Pennsylvania a seller can contribute toward your closing costs; in the right negotiation this is thousands of dollars, and we ask for it routinely.",
                "<strong>First-generation and county-level grants</strong> — programs come and go with funding cycles, which is exactly why a static list goes stale and a good agent's current list doesn't.",
                "<strong>Lender credits</strong> — trading a slightly higher rate for cash at closing is sometimes the right move for a buyer who's cash-tight but income-strong.",
            )
            + P("Program limits and terms change with funding cycles — verify current numbers with a PHFA-participating lender before you plan around them. Better yet, sit down with us first: fifteen minutes of program-matching before you tour a single home routinely changes what you can afford.")
        ),
    },
    {
        "slug": "pricing-strategy-list-high-costs-money",
        "eyebrow": "Sellers",
        "title": 'Pricing Strategy: Why &lsquo;Just List High&rsquo; <span class="italic">Costs You Money</span>',
        "meta_title": "Pricing Strategy for Sellers | Adam Druck Group",
        "dek": "The first two weeks decide everything. Here's the mechanism — and the pricing approach that actually produces over-ask results.",
        "body": (
            P("“We can always come down” sounds harmless. Mechanically, it's the most expensive sentence in residential real estate — because of how buyers, agents, and search portals actually behave in the first fourteen days of a listing.")
            + H("The attention spike you only get once")
            + P("Every serious buyer in your price band sees your home the week it lists. Saved searches fire, agents preview it, showings cluster. That audience is the largest it will ever be. Price into it correctly and the competitive pressure does your negotiating for you. Price over it and the spike passes quietly — and the buyers who remain are the ones trained to smell an overpriced listing aging on the vine.")
            + H("Price cuts are a signal, not a strategy")
            + P("The moment a listing shows a reduction, the buyer's question changes from “how do I win this house?” to “what's wrong with it, and how low will they go?” Data across markets is consistent: homes that sell after significant reductions net less than comparable homes priced correctly on day one — frequently less than the “low” price the seller was afraid of.")
            + H("What correct pricing looks like")
            + LI(
                "<strong>Comparables weighted like an appraiser</strong> — settled sales, same school district, same condition tier; not the neighbor's wish price.",
                "<strong>Search-band awareness</strong> — buyers search in brackets. A home at $305,000 is invisible to everyone capped at $300,000; sometimes the winning price is just under the line, harvesting two audiences.",
                "<strong>A launch, not an upload</strong> — pricing works with preparation and marketing: photos, coming-soon buzz, and a showing window that concentrates demand into the same weekend.",
            )
            + P("This is exactly how we price every ADG listing — it's why our sellers so often see multiple offers in the first week. If you want the analysis run on your home, it's complimentary.")
        ),
    },
    {
        "slug": "brrrr-york-county-walkthrough",
        "eyebrow": "Investor Case Study",
        "title": 'BRRRR in York County: A Real Deal, <span class="italic">From Acquisition to Refi</span>',
        "meta_title": "BRRRR in York County — A Full Walk-Through | Adam Druck Group",
        "dek": "Buy, rehab, rent, refinance, repeat — walked through end to end with round, illustrative numbers and the honest failure points.",
        "body": (
            P("BRRRR — buy, rehab, rent, refinance, repeat — is how patient investors build a rental portfolio without feeding it fresh capital forever. York County is genuinely good terrain for it: entry prices low enough to buy below replacement cost, rents solid relative to purchase prices, and steady tenant demand. Here's the whole cycle with round, <em>illustrative</em> numbers.")
            + H("The shape of a deal")
            + LI(
                "<strong>Buy</strong> a tired single-family for $120,000 — off-MLS, auction, or a listing everyone else scrolled past.",
                "<strong>Rehab</strong> with $40,000 focused on what tenants and appraisers both reward: mechanicals, kitchen, bath, flooring. All-in: $160,000.",
                "<strong>Rent</strong> at market to a well-screened tenant — say $1,500 a month.",
                "<strong>Refinance</strong> once seasoned: if it appraises at $215,000 and a lender writes 75% of value, the new loan is roughly $161,000 — your capital comes back out.",
                "<strong>Repeat</strong> with the same money, now holding a cash-flowing rental you effectively control for nearly nothing left in.",
            )
            + H("Where it actually fails")
            + P("Everything above hinges on two numbers being real: the after-repair value and the rehab budget. Optimistic ARV is the classic sin — the refinance appraisal doesn't care what you hoped. The second failure is timeline: every extra month between purchase and refi is carry cost, and lenders want seasoning. The third is rate math — a refi that made sense on paper at one rate can go upside-down on cash flow at another, which is why we stress-test every hold at higher rates before buying.")
            + H("Why the team matters")
            + P("BRRRR is five transactions wearing one name — acquisition, construction, leasing, appraisal, finance. We source the deals (including off-market and auction flow most investors never see), underwrite them with the same math we use for our own money, and manage the hand-offs. If you want to see live deals that fit this model, ask for the investor list.")
        ),
    },
    {
        "slug": "dover-township-second-look",
        "eyebrow": "Neighborhood Spotlight",
        "title": 'Why Dover Township Deserves <span class="italic">a Second Look</span>',
        "meta_title": "Dover Township Spotlight | Adam Druck Group",
        "dek": "Quietly, one of York County's best value stories — for first-time buyers and buy-and-hold investors alike.",
        "body": (
            P("Ask most buyers to name York County's hot spots and you'll hear the same short list. Dover Township rarely makes it — and that's precisely the opportunity. Some of the best value math in the county lives in places the conversation skips.")
            + H("The value case")
            + P("Dover sits close enough to Route 30 and the county's employment spine for a reasonable commute, without the price premium of the districts everyone bids on. Dollar for dollar, buyers consistently get more house, more lot, and newer systems than the equivalent budget buys in the fashionable zip codes. For a first purchase, that gap is the difference between stretching and breathing room.")
            + H("The landlord case")
            + P("For buy-and-hold investors, the ratio that matters is rent to purchase price — and outlying townships like Dover often carry better ratios than the trendy blocks, with tenant bases anchored by stable local employment rather than turnover-heavy student or transient demand. Boring is profitable in rentals.")
            + H("What to check before you buy")
            + LI(
                "<strong>Water and sewer</strong> — parts of the township are on well and septic; know which you're buying and inspect accordingly.",
                "<strong>Township development pipeline</strong> — new construction phases can shape both competition and future value; the township office will tell you what's approved.",
                "<strong>School assignment</strong> — verify the actual assigned schools for the parcel rather than assuming from the mailing address.",
            )
            + P("Every township has a version of this story — the question is whether the specific street and the specific house hold up. That's what we do all day. If Dover's on your list, or you want the three other townships we'd put beside it, let's talk.")
        ),
    },
]


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    for a in ARTICLES:
        html = shell(
            title=a["meta_title"],
            description=a["dek"],
            canonical_slug=f"insights/{a['slug']}.html",
            body_html=article_body(a["eyebrow"], a["title"], a["dek"], a["body"]),
        )
        out = os.path.join(OUT_DIR, f"{a['slug']}.html")
        with open(out, "w") as f:
            f.write(html)
        print(f"✓ insights/{a['slug']}.html ({len(html):,} bytes)")


if __name__ == "__main__":
    main()

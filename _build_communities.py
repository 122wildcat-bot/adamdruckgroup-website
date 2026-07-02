#!/usr/bin/env python3
"""Generate six community pages under communities/.

Content policy: evergreen local flavor and structural facts only — no
perishable market statistics (prices, DOM, tax rates, current inventory)
are baked into static pages. Ratings that go stale (percentile rankings,
current test scores) are also excluded. Voice: insider-realtor, direct,
tuned per-town.
"""
import os
import importlib.util

spec = importlib.util.spec_from_file_location(
    "shell_mod", os.path.join(os.path.dirname(__file__), "_page-shell.py")
)
shell_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(shell_mod)
shell = shell_mod.shell

OUT_DIR = os.path.join(os.path.dirname(__file__), "communities")


def community_body(town: str, eyebrow: str, dek: str, sections: list, faqs: list, related: list) -> str:
    """Build community page body. `sections` is list of (heading, html_body).
    `faqs` is list of (question, answer). `related` is list of (label, href).
    """
    section_html = ""
    for heading, body in sections:
        section_html += f'<h2 style="font-family: var(--serif); color: var(--ink); font-size: 1.5rem; margin: 2.2rem 0 0.8rem;">{heading}</h2>\n{body}\n'

    faq_html = '<h2 style="font-family: var(--serif); color: var(--ink); font-size: 1.5rem; margin: 2.6rem 0 1rem;">Common questions from buyers &amp; sellers</h2>\n'
    for q, a in faqs:
        faq_html += f'<div style="margin-bottom: 1.4rem;"><p style="font-weight: 600; color: var(--ink); margin: 0 0 0.4rem;">{q}</p><p style="margin: 0;">{a}</p></div>\n'

    related_html = '<h3 style="font-family: var(--serif); color: var(--ink); font-size: 1.15rem; margin: 2.6rem 0 0.8rem;">Also explore</h3>\n<ul style="margin: 0 0 1.1rem; padding-left: 1.2rem;">\n'
    for label, href in related:
        related_html += f'  <li style="margin-bottom: 0.4rem;"><a href="{href}" style="color: var(--cb-blue);">{label}</a></li>\n'
    related_html += "</ul>\n"

    return f"""
<section class="page-lead">
  <div class="page-lead__inner">
    <p class="eyebrow page-lead__eyebrow">{eyebrow}</p>
    <h1 class="page-lead__title">{town}</h1>
    <p class="page-lead__lede">{dek}</p>
  </div>
</section>

<section class="section">
  <div class="section__inner" style="max-width: 720px;">
    <div style="color: var(--slate); font-size: 1.05rem; line-height: 1.75;">
{section_html}
{faq_html}
    </div>

    <div style="margin-top: 3rem; padding: 2rem; background: var(--cream); border-left: 3px solid var(--celestial);">
      <p style="margin: 0 0 1rem; font-family: var(--serif); font-size: 1.15rem; color: var(--ink);">
        Thinking about buying or selling in {town}?
      </p>
      <a href="/home-value.html" class="btn btn--primary">What&rsquo;s My Home Worth?</a>
      <a href="/contact.html#message" class="btn btn--ghost" style="margin-left: 0.5rem;">Talk to the Team</a>
    </div>

    <div style="margin-top: 2rem;">
{related_html}
    </div>

    <p style="margin-top: 1.5rem;"><a href="/communities.html" style="color: var(--cb-blue);">&larr; All Communities</a></p>
  </div>
</section>
"""


P = lambda t: f'<p style="margin: 0 0 1.1rem;">{t}</p>'
LI = lambda *items: "<ul style='margin: 0 0 1.1rem; padding-left: 1.2rem;'>" + "".join(
    f"<li style='margin-bottom: 0.5rem;'>{i}</li>" for i in items
) + "</ul>"


# ============================================================================
# YORK, PA — The White Rose City. Historic, urban, layered.
# Voice: proud of history, honest that "York" is really 6 markets in a trench coat.
# ============================================================================
YORK = {
    "slug": "york",
    "town": "York, PA",
    "eyebrow": "Community Guide",
    "meta_title": "Living in York, PA — The White Rose City | Adam Druck Group",
    "dek": "The First Capital of the United States, the White Rose City, the market where six school districts and a dozen distinct neighborhoods all get called by one name. Here&rsquo;s how to actually read it.",
    "sections": [
        ("What it feels like to live here",
            P("York is a compact, historic downtown ringed by townships that each feel like their own place. Founded in 1741 as the first town west of the Susquehanna, it spent nine months as the seat of the Continental Congress — the Articles of Confederation were adopted here in November 1777, and this is where the phrase &ldquo;the United States of America&rdquo; was first written into a founding document. That history isn&rsquo;t museum-piece; it&rsquo;s Continental Square downtown, the Colonial Complex, First Friday art walks, and a Central Market that has been operating since 1888.")
            + P("But the honest thing about York is that &ldquo;York&rdquo; isn&rsquo;t one market. The city proper, Spring Garden, East York, West York, and the surrounding townships each have different school districts, different tax profiles, and completely different housing stock. Which side of town you land on matters more than any headline number.")
        ),
        ("Neighborhoods &amp; housing stock",
            LI(
                "<strong>Downtown / Center City</strong> — brick rowhomes, Victorian singles, and loft-style conversions in former factory buildings. Walkable, historic, city taxes and city schools.",
                "<strong>Spring Garden Township (17403)</strong> — established mid-century capes and colonials, tree-lined streets, walkable to downtown; York Suburban schools.",
                "<strong>East York / Springettsbury Township (17402)</strong> — postwar to modern subdivisions along the Route 30 corridor. Ranches, splits, colonials; convenient to shopping and I-83.",
                "<strong>West York / West Manchester</strong> — older borough rowhomes plus newer development pushing west along Route 30.",
                "<strong>Manchester Township &amp; north</strong> — newer construction, larger lots, quieter feel.",
            )
        ),
        ("Schools — the piece most buyers misread",
            P("There is no single &ldquo;York school district.&rdquo; The city itself is York City School District. Ring around it and you pick up six more — York Suburban (Spring Garden and parts of East York), Central York (northeast, Route 30 corridor), West York Area, Dallastown Area, Red Lion Area, and Northeastern. School district is <em>the</em> variable that shapes both price and future resale in this market; every parcel we look at, we verify the assigned schools before we let a buyer fall in love with a house.")
        ),
        ("Commute &amp; connectivity",
            LI(
                "<strong>I-83</strong> — 25 minutes to Harrisburg, roughly 50 to Baltimore, 90+ to DC.",
                "<strong>Route 30</strong> — Lancaster about 35 minutes east, Gettysburg about 30 minutes west.",
                "<strong>Amtrak Keystone</strong> — accessible via Lancaster or Harrisburg for Philadelphia and New York.",
                "<strong>Major employers</strong> — WellSpan Health, York Hospital, Harley-Davidson York Vehicle Operations (motorcycles are still built here), BAE Systems, Dentsply Sirona.",
            )
        ),
        ("What to do here",
            P("<strong>Central Market York</strong> (operating since 1888) anchors downtown three days a week. <strong>PeoplesBank Park</strong> is home to York Revolution baseball in the Atlantic League. The <strong>Heritage Rail Trail County Park</strong> runs 21+ miles south to the Maryland line — cycling, running, or a Saturday morning walk. <strong>Codorus State Park</strong> is 20 minutes south for boating and camping. York is also called the <em>Factory Tour Capital of the World</em> — Harley-Davidson runs a tour, Wolfgang Candy is nearby, and Utz is 30 minutes over in Hanover.")
        ),
    ],
    "faqs": [
        ("Is York, PA a good place to live?",
            "For value in the mid-Atlantic, it&rsquo;s hard to beat — you&rsquo;re within an hour of Harrisburg, Baltimore, and Lancaster at a housing cost that&rsquo;s a fraction of those metros. Whether it fits <em>you</em> depends heavily on which side of town, which district, and what housing stock you want. That&rsquo;s exactly the conversation we have with every buyer moving in from out of the area."),
        ("What&rsquo;s the difference between York City, East York, and Spring Garden?",
            "York City proper is the historic urban core — different school district, different tax profile, denser housing. East York (Springettsbury Township) is the postwar and modern suburb along the Route 30 corridor. Spring Garden Township sits between them — older suburban feel, York Suburban schools. Different price bands, different buyer profiles."),
        ("How&rsquo;s the commute to Baltimore or DC?",
            "Baltimore is a real commute — about 50 minutes to the city, longer at rush. DC is a stretch (90+ minutes each way), but people do it, especially with hybrid schedules. A steady flow of buyers keeps moving up from those metros for the price gap."),
        ("Which York-area school districts do buyers ask about most?",
            "York Suburban, Central York, and Dallastown Area come up most often in the mid-to-upper price bands — each with its own personality. But school assignment is parcel-level, not zip-code-level, so we always verify the actual assigned schools before you write an offer."),
    ],
    "related": [
        ("Dallastown, PA", "/communities/dallastown.html"),
        ("Red Lion, PA", "/communities/red-lion.html"),
        ("Hanover, PA", "/communities/hanover.html"),
        ("What&rsquo;s my home worth?", "/home-value.html"),
    ],
}


# ============================================================================
# DALLASTOWN, PA — Compact borough, cigar-town heritage, top-tier district.
# Voice: warm, specific, borough-vs-township distinction is a running theme.
# ============================================================================
DALLASTOWN = {
    "slug": "dallastown",
    "town": "Dallastown, PA",
    "eyebrow": "Community Guide",
    "meta_title": "Living in Dallastown, PA — Borough, Schools &amp; Commute | Adam Druck Group",
    "dek": "A walkable borough with brick sidewalks, a top-ranked school district that stretches well beyond the borough line, and one of the most reliable I-83 commutes in the county.",
    "sections": [
        ("What it feels like to live here",
            P("Dallastown is a small, walkable borough with a real Main Street — brick sidewalks, a central square anchored by the historic Commercial Hotel corner, and enough front porches to make you slow down when you drive through. Named in 1844 for Vice President George M. Dallas and incorporated in 1866, it grew up around cigars — by the 1880s, York County produced roughly a fifth of all cigars in the United States, and Dallastown was one of the epicenters. The industry is gone; the tight, dense town it built is still here.")
        ),
        ("Housing stock",
            LI(
                "<strong>Historic borough core</strong> — Victorian, Second Empire, and Colonial Revival singles from the cigar-era boom.",
                "<strong>Early-20th-century worker cottages and four-squares</strong> — the walkable heart of the borough.",
                "<strong>Mid-century capes and ranches</strong> — postwar York Township growth just beyond the borough line.",
                "<strong>Newer construction</strong> — subdivisions at the edges of York Township and Springfield Township that share the Dallastown mailing address.",
            )
        ),
        ("Schools — the biggest reason people move here",
            P("Dallastown Area School District covers roughly 52 square miles — the borough plus York Township and pieces of Springfield and Jacobus. It consistently ranks in the top tier of Pennsylvania districts for proficiency, graduation rate, and college-and-career readiness, with a broad slate of AP and dual-enrollment offerings and strong athletics and arts programs. Every out-of-state buyer we work with who has kids in school asks about Dallastown — and once they tour, they usually understand why.")
        ),
        ("Commute &amp; connectivity",
            LI(
                "<strong>York City</strong> — about 7 miles up Route 74, 12&ndash;15 minutes.",
                "<strong>I-83</strong> interchange minutes from the borough — the reason this district commutes so well.",
                "<strong>Harrisburg</strong> — roughly 35 miles, 35&ndash;45 minutes.",
                "<strong>Baltimore</strong> — about 55 miles, an hour outside rush.",
            )
        ),
        ("What to do here",
            P("<strong>Dallastown Community Park</strong> handles the ball fields and playgrounds. <strong>Wyndridge Farm</strong> — cidery, brewery, restaurant, event venue — is the local Saturday afternoon anchor. The <strong>Heritage Rail Trail</strong> is accessible for cycling and running. <strong>Nixon County Park</strong> and <strong>William H. Kain County Park at Lake Redman</strong> are both close for hiking and fishing. In the borough itself: a summer <strong>Carnival</strong> that&rsquo;s been running 25+ years with free admission, a Halloween parade, and Christmas in Dallastown. <strong>Sechrist Brothers Butcher</strong> has been on Main Street since 1877.")
        ),
    ],
    "faqs": [
        ("Is my address the Dallastown borough or York Township?",
            "This trips up almost every out-of-town buyer. Plenty of homes with a Dallastown mailing address are actually in York Township, not the borough — different taxes, different municipal services, sometimes even different police coverage. Same school district in most cases, but the municipality matters for what you pay and how the property gets served. We verify this on every listing before we let anyone write an offer."),
        ("How&rsquo;s the commute to York, Harrisburg, and Baltimore?",
            "This is Dallastown&rsquo;s hidden superpower. Route 74 puts you in York in 12&ndash;15 minutes, the I-83 on-ramp is a few minutes from the borough, and from there you&rsquo;re roughly 35 to Harrisburg and an hour to Baltimore. It&rsquo;s the reason so many two-income households pick this district."),
        ("How is the Dallastown Area school district?",
            "Consistently one of the top-performing districts in York County across the metrics that matter to buyers — proficiency, graduation rate, AP and dual enrollment, and strong athletics and arts. Whether that fits your family is a personal fit question, but the objective performance is not the concern here."),
        ("Can I walk to things, or do I have to drive everywhere?",
            "In the borough itself, quite a bit is walkable — post office, coffee, pizza, church, park, library. Once you&rsquo;re out into York Township you&rsquo;re back in the car for anything. That&rsquo;s the borough-vs-township tradeoff in a sentence."),
    ],
    "related": [
        ("Red Lion, PA", "/communities/red-lion.html"),
        ("York, PA", "/communities/york.html"),
        ("Sell your home", "/sell.html"),
        ("What&rsquo;s my home worth?", "/home-value.html"),
    ],
}


# ============================================================================
# RED LION, PA — Cigars and furniture heritage. Rowhouses, small-town.
# Voice: character-forward, honest about the borough vs. surrounding townships.
# ============================================================================
RED_LION = {
    "slug": "red-lion",
    "town": "Red Lion, PA",
    "eyebrow": "Community Guide",
    "meta_title": "Living in Red Lion, PA — Cigar Town, Rowhouses &amp; Real Value | Adam Druck Group",
    "dek": "Named for a tavern, built on cigars and furniture, and still one of the best character-per-dollar boroughs in York County.",
    "sections": [
        ("What it feels like to live here",
            P("Red Lion has one of the more specific personalities in the county. Named for the Red Lion Tavern that stood at the crossroads before the town did, it grew up around the Maryland &amp; Pennsylvania Railroad — locals call it the &ldquo;Ma &amp; Pa&rdquo; — and hit its stride as a cigar town. At the peak, 150+ cigar factories operated inside the borough limits; York County as a whole made an estimated 10&ndash;20% of the country&rsquo;s cigars. Once cigars faded, furniture manufacturing took over for most of the twentieth century. That industrial past is why the borough has the density, sidewalks, and Main Street it has.")
            + P("The signature local tradition is the New Year&rsquo;s Eve <strong>cigar drop</strong> — Red Lion&rsquo;s answer to Times Square, tipped to the town&rsquo;s heritage. The Street Fair has been running 48+ years. Halestorm&rsquo;s Lzzy Hale is from here. Nothing about Red Lion is generic.")
        ),
        ("Housing stock",
            LI(
                "<strong>Borough core</strong> — rowhouses and attached homes, pre-1939 brick and frame, Colonial Revival and Italianate styling. Narrow lots, deep porches, sidewalks in every direction.",
                "<strong>Single-family detached</strong> — mixed in through the borough, mostly on the tighter lots.",
                "<strong>Mid-century and post-1970 subdivisions</strong> — as you move out into Windsor and Chanceford townships, the neighborhoods open up into ranches, splits, and newer builds.",
                "<strong>New construction</strong> — active in the broader 17356 zip beyond the borough line.",
            )
        ),
        ("Schools",
            P("<strong>Red Lion Area School District</strong> runs on the mission &ldquo;Real Learning for Real Life.&rdquo; It has been recognized nationally by the NAMM Foundation as one of the country&rsquo;s Best Communities for Music Education (multiple years in the 2010s) and offers a STEAM Ahead program that&rsquo;s not standard in every district this size. The district&rsquo;s geography stretches well past the borough, so &ldquo;going to Red Lion schools&rdquo; and &ldquo;living in Red Lion the borough&rdquo; are two different address questions.")
        ),
        ("Commute &amp; connectivity",
            LI(
                "<strong>York City</strong> — about 8 miles up Route 74, 15&ndash;20 minutes.",
                "<strong>Lancaster</strong> — 25&ndash;30 miles via Route 74 to Route 30 East, 35&ndash;45 minutes.",
                "<strong>Baltimore</strong> — about 50 miles via I-83, 60&ndash;70 minutes outside rush.",
                "<strong>rabbittransit</strong> — bus service to York.",
            )
        ),
        ("What to do here",
            P("<strong>Fairmount Park</strong> (11 acres, splash pad, veterans memorial) is the borough&rsquo;s main greenspace. <strong>Nitchkey Field</strong> handles youth sports. The <strong>Ma &amp; Pa Community Greenway</strong> trail traces the old railbed. The <strong>Red Lion Borough Historic District</strong> and the former <strong>Consumers Cigar Box Company</strong> are on the National Register. The annual <strong>Street Fair</strong> is the summer social calendar for the whole town; <strong>Suds and Songs</strong>, <strong>Food Truck Fridays</strong>, and a July 4th car show and fireworks round out the calendar. The New Year&rsquo;s cigar drop is the one everyone shows up for.")
        ),
    ],
    "faqs": [
        ("Is Red Lion a good place to live?",
            "For character and price it&rsquo;s one of the strongest values in the county. What you get is a walkable borough with real texture — porches, brick, a Main Street with actual stores — plus a district with a genuinely good reputation and a straightforward commute to York. What you should verify: municipality (borough vs. township), the specific block, and how much sidewalk life you actually want."),
        ("What&rsquo;s the commute to York like?",
            "Straightforward — Route 74 is a direct shot in, 15&ndash;20 minutes to downtown or East York. That&rsquo;s why the borough works so well for people who want small-town at home and city amenities during the day."),
        ("How is the Red Lion Area school district?",
            "Well-regarded, with a particular strength in music and arts programming and a genuine STEAM initiative. It&rsquo;s a district families move <em>toward</em> for a reason, but as always we&rsquo;ll walk you through what fits your kids and where the assigned school actually sits."),
        ("Rowhouses or single-family — what should I look at in Red Lion?",
            "Depends on what you value. Rowhouses give you the walkable, historic borough experience at the lowest price point in the district; single-family in the outlying townships gets you space and a garage. Both make sense, for different reasons. We&rsquo;ll show you the tradeoffs on the block level."),
    ],
    "related": [
        ("Dallastown, PA", "/communities/dallastown.html"),
        ("York, PA", "/communities/york.html"),
        ("Investor guide", "/invest.html"),
        ("What&rsquo;s my home worth?", "/home-value.html"),
    ],
}


# ============================================================================
# HANOVER, PA — Snack Food Capital, Battle of Hanover, straddles two counties.
# Voice: proud of the specificity, honest about the two-district geography.
# ============================================================================
HANOVER = {
    "slug": "hanover",
    "town": "Hanover, PA",
    "eyebrow": "Community Guide",
    "meta_title": "Living in Hanover, PA — Snack Food Capital &amp; Historic Downtown | Adam Druck Group",
    "dek": "The Snack Food Capital of the World, the site of the first Civil War battle on Northern soil, and one of the largest walkable historic downtowns in the region.",
    "sections": [
        ("What it feels like to live here",
            P("Hanover is the rare small city that&rsquo;s specifically known for something. Utz was founded here in 1921 with a $300 investment by William and Salie Utz; Snyder&rsquo;s of Hanover traces back to the same neighborhood. That cluster of snack manufacturers is why Hanover carries the &ldquo;Snack Food Capital of the World&rdquo; nickname, and it&rsquo;s still one of the reasons the borough has a stable employment base most towns this size don&rsquo;t.")
            + P("The other thing worth knowing: the <strong>Battle of Hanover</strong> was fought here on June 30, 1863 — Union cavalry under Kilpatrick versus J.E.B. Stuart, fighting through the borough streets. It was the first Civil War battle on Northern soil, and Stuart&rsquo;s delay contributed to his late arrival at Gettysburg the following day. The borough is a federally designated <strong>Preserve America Community</strong>, and the Hanover Historic District covers 885 acres with 2,600+ contributing buildings.")
        ),
        ("Housing stock",
            LI(
                "<strong>Historic core</strong> — Queen Anne, Colonial Revival, and Pennsylvania German vernacular, roughly 1870&ndash;1946. This is the National Register district; density and architecture at levels most PA boroughs don&rsquo;t reach.",
                "<strong>Mid-century</strong> — ranches, splits, and modest colonials from the postwar snack-industry expansion.",
                "<strong>Newer suburban-style developments</strong> — Penn Township, West Manheim, Conewago, and Heidelberg Townships all carry Hanover addresses with different school assignments.",
            )
        ),
        ("Schools — two districts, one town",
            P("This is the piece most out-of-area buyers miss. The borough itself is served by <strong>Hanover Public School District</strong> — smaller, roughly 1,950 students, tight-knit and relationship-driven. The surrounding townships are served by <strong>South Western School District</strong> — larger, roughly 4,350 students, broader program offerings. Both are well-regarded; they&rsquo;re just different scales. Which one you get is determined by the parcel, not the mailing address, and that boundary runs right through Hanover-labeled listings.")
        ),
        ("Commute &amp; connectivity",
            LI(
                "<strong>Gettysburg</strong> — about 14 miles west via Route 116, 20&ndash;25 minutes.",
                "<strong>York</strong> — about 19 miles east via Route 116, 25&ndash;30 minutes.",
                "<strong>Baltimore</strong> — about 45 miles south via Route 94, 55&ndash;75 minutes.",
                "<strong>Major employers</strong> — Utz, Snyder&rsquo;s/Campbell&rsquo;s, R.H. Sheppard, Hanover Hospital, plus the broader manufacturing base.",
            )
        ),
        ("What to do here",
            P("<strong>Codorus State Park</strong> is 3 miles out — a 1,275-acre lake (Lake Marburg), 19+ miles of trails, boating, and fishing that punches well above what most towns this size have access to. <strong>Utz</strong> runs a self-guided factory tour and outlet store. <strong>Hanover Shoe Farms</strong> is one of the country&rsquo;s premier Standardbred breeding operations. The <strong>Eichelberger Performing Arts Center</strong> anchors downtown culture, and the <strong>Warehime-Myers Mansion</strong> is the local history museum. Downtown itself carries a walkable, restaurant-and-shop life you don&rsquo;t find in most boroughs this size.")
        ),
    ],
    "faqs": [
        ("Is Hanover in York County or Adams County?",
            "The borough is in York County, but the greater Hanover area spills over into Adams County (west) — mailing addresses can read &ldquo;Hanover&rdquo; on either side of the line. Different county, different tax jurisdiction, sometimes a different school district. Always something to confirm before writing an offer."),
        ("What&rsquo;s the difference between Hanover Public and South Western schools?",
            "Hanover Public is the borough district — smaller, tighter, roughly 1,950 students. South Western covers the surrounding townships — larger, roughly 4,350 students, broader course catalog. Both are well-regarded; they&rsquo;re different scales for different families. The dividing line is parcel-level."),
        ("Is downtown Hanover actually walkable?",
            "For a town this size, yes — genuinely walkable, with restaurants, shops, and the Eichelberger anchoring the district. It&rsquo;s one of the reasons the borough gets attention from buyers moving out of Baltimore and DC for a slower pace without giving up a walkable Saturday."),
        ("How&rsquo;s the commute to Baltimore or Gettysburg?",
            "Gettysburg is a 20&ndash;25 minute drive west on Route 116 — genuinely close. Baltimore is a real commute at 55&ndash;75 minutes on Route 94, but doable on hybrid schedules, and plenty of Hanover residents do exactly that."),
    ],
    "related": [
        ("Dillsburg, PA", "/communities/dillsburg.html"),
        ("York, PA", "/communities/york.html"),
        ("Sell your home", "/sell.html"),
        ("What&rsquo;s my home worth?", "/home-value.html"),
    ],
}


# ============================================================================
# DILLSBURG, PA — Northern York, Pickle Drop, Harrisburg commuter town.
# Voice: playful nod to the Pickle Drop, practical about Harrisburg proximity.
# ============================================================================
DILLSBURG = {
    "slug": "dillsburg",
    "town": "Dillsburg, PA",
    "eyebrow": "Community Guide",
    "meta_title": "Living in Dillsburg, PA — Northern York, Pickle Drop &amp; Harrisburg Commute | Adam Druck Group",
    "dek": "A small borough at the base of South Mountain with a famously offbeat New Year&rsquo;s tradition, top-tier commute access to Harrisburg, and one of the county&rsquo;s quieter housing markets.",
    "sections": [
        ("What it feels like to live here",
            P("Dillsburg is the borough that drops a pickle. On New Year&rsquo;s Eve since 1992 — a tradition that started as an Eagle Scout project — a giant pickle descends over Baltimore Street and pulls a crowd from across the region. That&rsquo;s the surface. Underneath, it&rsquo;s a compact borough of roughly 2,700 people in less than a square mile, founded around 1740 by Matthew Dill and incorporated in 1833, sitting at the base of South Mountain in the northern reach of York County. J.E.B. Stuart&rsquo;s cavalry passed through in 1863. The town square, the 19th-century architecture, and the small-town scale are all still here.")
        ),
        ("Housing stock",
            LI(
                "<strong>Borough</strong> — late-19th and early-20th-century colonials and cape cods clustered around the square.",
                "<strong>Carroll Township &amp; surrounding</strong> — newer single-family developments and some rural acreage; several active builders serve the market.",
                "<strong>Northern York corridor</strong> — mix of established neighborhoods and newer subdivisions along Route 15 and Route 74.",
            )
        ),
        ("Schools",
            P("<strong>Northern York County School District</strong> — Northern High School and Northern Middle School sit inside the borough itself. The district is community-supportive, athletically strong (the Polar Bears), and consistently posts reading and math proficiency above the Pennsylvania average. It&rsquo;s the kind of district families move to specifically for the size and the scale.")
        ),
        ("Commute &amp; connectivity",
            LI(
                "<strong>Harrisburg</strong> — this is Dillsburg&rsquo;s core appeal. 15&ndash;16 miles up Route 15, 15&ndash;20 minutes to the state Capitol complex.",
                "<strong>Carlisle</strong> — 11 miles west on Route 74, 15&ndash;17 minutes.",
                "<strong>York</strong> — 21 miles south on Route 74, 25&ndash;30 minutes.",
                "<strong>rabbittransit 15N</strong> commuter bus service is available.",
            )
        ),
        ("What to do here",
            P("<strong>Ski Roundtop Mountain Resort</strong> is about 6 miles away — skiing, snowboarding, and tubing in season, plus a summer program. <strong>Gifford Pinchot State Park</strong> is 10&ndash;15 minutes out — a 2,300-acre state park with a 340-acre lake for boating and fishing. <strong>Pine Grove Furnace State Park</strong> is 15&ndash;20 minutes west (this is where thru-hikers on the Appalachian Trail traditionally do the half-gallon ice cream challenge). In the borough itself: <strong>Dill&rsquo;s Tavern</strong>, a 1794 living-history museum, and the <strong>Quay House</strong> on the National Register. Plus, of course, the Pickle Drop.")
        ),
    ],
    "faqs": [
        ("Is Dillsburg a realistic Harrisburg commute?",
            "It&rsquo;s one of the best short commutes to downtown Harrisburg you can find without living inside the city — 15&ndash;20 minutes up Route 15, no interstate, no toll. For state government employees and Capitol-complex workers, Dillsburg is a well-worn choice for exactly this reason."),
        ("How is the Northern York County school district?",
            "Well-regarded, community-supportive, and structurally on the smaller side — which some families specifically want. Reading and math proficiency runs above the Pennsylvania average, and the athletic and extracurricular scene is strong for a district this size."),
        ("Is Dillsburg rural, small-town, or suburban?",
            "The borough itself is genuine small-town — 2,700 people, a square, a couple of streets of downtown. Step a few minutes outside the borough into Carroll Township and it turns into a mix of newer suburban development and rural acreage. You can pick your flavor within a five-mile radius."),
        ("What about outdoor recreation?",
            "This is one of Dillsburg&rsquo;s strongest cards. Ski Roundtop, Gifford Pinchot, and Pine Grove Furnace are all a short drive; the Appalachian Trail is close; and the whole northern York foothills terrain is legitimately good for hiking, cycling, and fishing."),
    ],
    "related": [
        ("Harrisburg, PA", "/communities/harrisburg.html"),
        ("York, PA", "/communities/york.html"),
        ("Buyer guide", "/buy.html"),
        ("What&rsquo;s my home worth?", "/home-value.html"),
    ],
}


# ============================================================================
# HARRISBURG, PA — State capital, Susquehanna, city + West Shore/East Shore.
# Voice: honest about the city-vs-suburbs question, informed by state-capital jobs.
# ============================================================================
HARRISBURG = {
    "slug": "harrisburg",
    "town": "Harrisburg, PA",
    "eyebrow": "Community Guide",
    "meta_title": "Living in Harrisburg, PA — State Capital, River Cities &amp; Suburbs | Adam Druck Group",
    "dek": "Pennsylvania&rsquo;s capital city, a Susquehanna riverfront, and a metro that runs from historic rowhouse neighborhoods to some of the most sought-after school districts on the East Shore and West Shore.",
    "sections": [
        ("What it feels like to live here",
            P("Harrisburg has been the state capital since 1812, and the whole city is organized around that fact — the domed Capitol building, the state office complex, the ring of professional services and law firms and lobbying shops that state government pulls in. The Susquehanna runs the entire western edge of the city, which is why so many of the postcards start with Riverfront Park or City Island. The <strong>City Beautiful</strong> movement — kicked off locally by Mira Lloyd Dock&rsquo;s 1900 speech — is why the park system, the esplanade, and the Capitol dedication (attended by Teddy Roosevelt in 1906) look the way they do today.")
            + P("What most out-of-area buyers underestimate is how sharply the metro splits into city, East Shore, and West Shore — three genuinely different housing markets with different price points, different school districts, and different commute realities.")
        ),
        ("Neighborhoods &amp; housing stock",
            LI(
                "<strong>Midtown &amp; Uptown Harrisburg</strong> — historic rowhouses, walkable, arts-and-restaurant density; Old Uptown is a National Register historic district.",
                "<strong>East Shore suburbs</strong> — Lower Paxton, Swatara Township, Susquehanna Township, Hummelstown; mix of postwar ranches, splits, and newer construction.",
                "<strong>West Shore</strong> — Camp Hill, Mechanicsburg, Hampden Township; strong walkability in the older boroughs, newer suburban growth further out.",
                "<strong>Riverfront neighborhoods</strong> — Shipoke and Riverside on the city side carry premium riverfront character.",
            )
        ),
        ("School districts",
            P("The metro is covered by a set of very different districts. Inside the city: <strong>Harrisburg City School District</strong>. On the East Shore: <strong>Central Dauphin</strong>, <strong>Susquehanna Township</strong>, and <strong>Lower Dauphin</strong> (Hummelstown area) each have their own character and scale. On the West Shore: <strong>Cumberland Valley</strong> and <strong>Camp Hill</strong> both draw families specifically for the schools. The metro-wide rule holds: parcel-level assignment, verify before you fall in love.")
        ),
        ("Commute &amp; connectivity",
            LI(
                "<strong>Amtrak Keystone Service</strong> — up to 13 weekday trains, about 1h45m to Philadelphia, roughly 3.5 hours to New York, with strong on-time performance. One of the reasons Harrisburg works for hybrid commuters.",
                "<strong>State government</strong> — the metro&rsquo;s largest employment engine; Capitol complex, executive branch offices, PennDOT, state courts.",
                "<strong>I-83 south to York</strong> — about 25 minutes to York, roughly 75 to Baltimore.",
                "<strong>I-81, I-76 (PA Turnpike), Route 322</strong> — all converge here.",
            )
        ),
        ("What to do here",
            P("<strong>Riverfront Park</strong> and <strong>City Island</strong> (with FNB Field for Senators baseball) anchor the city&rsquo;s waterfront. The <strong>State Capitol complex</strong> offers free tours. <strong>Broad Street Market</strong> has been operating since 1860 — one of the oldest continuously operating public markets in the country, on the National Register. The <strong>Whitaker Center</strong> handles performing arts and science. <strong>Capital Area Greenbelt</strong> is a 20-mile trail loop around the city. <strong>Wildwood Park</strong> and the <strong>National Civil War Museum</strong> round it out. Annual anchors include <strong>Kipona</strong> (Labor Day weekend, running for over a century), Restaurant Week, and <strong>3rd in the Burg</strong> — a monthly arts crawl.")
        ),
        ("The suburbs, briefly",
            LI(
                "<strong>Camp Hill</strong> — small, walkable West Shore borough with its own district; consistently among the most-asked in the metro.",
                "<strong>Mechanicsburg</strong> — larger West Shore town, historic downtown plus significant newer development.",
                "<strong>Hummelstown</strong> — East Shore, tight-knit, home to a walkable downtown and the Hershey Med area.",
                "<strong>Susquehanna Township</strong> — first-ring East Shore suburb, mixed housing stock, direct city access.",
            )
        ),
    ],
    "faqs": [
        ("Is Harrisburg city or the suburbs the better move?",
            "Depends entirely on what you want. The city gives you rowhouse living, walkability, arts, restaurants, and the shortest possible commute to Capitol jobs — plus the Broad Street Market and the riverfront. The suburbs (especially Camp Hill, Cumberland Valley, and Lower Dauphin) give you the school districts and space that families with kids often prioritize. We work both sides of the river."),
        ("Can you commute from Harrisburg to Philadelphia?",
            "Yes, and a real number of people do. The Amtrak Keystone runs up to 13 weekday trains and hits Philadelphia in about 1h45m, with strong on-time performance. It&rsquo;s the reason Harrisburg is one of the more viable &ldquo;live cheaper, work in the city&rdquo; plays on the East Coast for hybrid schedules."),
        ("How stable is the local economy?",
            "As stable as it gets. State government is not going anywhere, and it&rsquo;s the largest employment engine in the metro. Add in healthcare (Penn State Health, UPMC), higher ed, and the professional-services ring that clusters around state government, and you have one of the more recession-resistant labor markets in the region."),
        ("What&rsquo;s the deal with the West Shore vs. East Shore rivalry?",
            "It&rsquo;s real, it&rsquo;s mostly friendly, and it comes down to which side of the Susquehanna you commute across each day. West Shore (Camp Hill, Mechanicsburg, Hampden) tends to be newer, more suburban, and school-district-anchored. East Shore (Susquehanna Township, Lower Paxton, Hummelstown) has the direct-city-access advantage. Both work. The bridges are the flex point at rush hour."),
    ],
    "related": [
        ("Dillsburg, PA", "/communities/dillsburg.html"),
        ("York, PA", "/communities/york.html"),
        ("Sell your home", "/sell.html"),
        ("What&rsquo;s my home worth?", "/home-value.html"),
    ],
}


COMMUNITIES = [YORK, DALLASTOWN, RED_LION, HANOVER, DILLSBURG, HARRISBURG]


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    for c in COMMUNITIES:
        body_html = community_body(
            town=c["town"],
            eyebrow=c["eyebrow"],
            dek=c["dek"],
            sections=c["sections"],
            faqs=c["faqs"],
            related=c["related"],
        )
        html = shell(
            title=c["meta_title"],
            description=c["dek"].replace("&rsquo;", "'").replace("&ldquo;", '"').replace("&rdquo;", '"'),
            canonical_slug=f"communities/{c['slug']}.html",
            body_html=body_html,
        )
        out = os.path.join(OUT_DIR, f"{c['slug']}.html")
        with open(out, "w") as f:
            f.write(html)
        print(f"✓ communities/{c['slug']}.html ({len(html):,} bytes)")


if __name__ == "__main__":
    main()

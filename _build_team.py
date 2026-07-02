#!/usr/bin/env python3
"""Generates individual agent bio pages + /team hub for Adam Druck Group."""
import os
from pathlib import Path

SITE_ROOT = Path(__file__).parent
TEAM_DIR = SITE_ROOT / "team"
TEAM_DIR.mkdir(exist_ok=True)

# GSC verification tag (same as rest of site)
GSC_TAG = '<meta name="google-site-verification" content="1WGCk5WyM1KNoxqdy_fbgdbiVcqvBEbPIqIQ0wHMTqg" />'

AGENTS = [
    {
        "slug": "adam-druck",
        "first": "Adam",
        "last": "Druck",
        "role": "Team Lead · REALTOR®",
        "title": "Team Lead & Owner",
        "phone": "(717) 487-2579",
        "phone_tel": "+17174872579",
        "email": "yourrealtoradamd@gmail.com",
        "photo": "/images/team/adam.jpg",
        "license": "RS-0038815 (PA) · Licensed in PA, MD, DE",
        "specialties": [
            "Seller strategy & pricing",
            "Investment & flip analysis",
            "Luxury residential",
            "Relocation into York County",
        ],
        "bio_short": "A York County native leading one of the region's most active real estate teams.",
        "bio_long": [
            "Adam Druck grew up in York County and has spent his entire career helping the people who live here buy, sell, and invest in real estate. As the founder and team lead of the Adam Druck Group at Coldwell Banker Realty, he has personally guided hundreds of transactions across South Central Pennsylvania — from first-time buyers stepping into a Dallastown starter home to luxury sellers listing on a Dillsburg horse farm.",
            "His approach is straightforward: pair generational local knowledge with modern marketing, sharp pricing, and old-school follow-through. Clients get the reach of Coldwell Banker's global network combined with an agent who genuinely knows which side of Route 30 has the best light and which neighborhoods hold value in a soft market.",
            "Adam is licensed in Pennsylvania, Maryland, and Delaware, and has been recognized among the top-producing agents in the region every year of his career. When he's not showing homes, he's usually running numbers on a flip, out at a Phillies game, or on the golf course.",
        ],
    },
    {
        "slug": "trevor-stuck",
        "first": "Trevor",
        "last": "Stuck",
        "role": "REALTOR®",
        "title": "REALTOR®",
        "phone": "(717) 599-2375",
        "phone_tel": "+17175992375",
        "email": None,
        "photo": "/images/team/trevor.jpg",
        "license": "Licensed REALTOR® in Pennsylvania",
        "specialties": [
            "First-time buyers",
            "Growing families",
            "New construction",
            "Buyer representation",
        ],
        "bio_short": "A consultative, patient guide for first-time buyers and growing families across York County.",
        "bio_long": [
            "Trevor Stuck is the kind of agent people describe as \"the reason we actually enjoyed the process.\" His style is unhurried, deeply detail-oriented, and built around asking the right questions before making a single showing appointment.",
            "That approach makes him a natural fit for first-time buyers who need someone to translate lender jargon, inspection findings, and negotiation strategy without ever making them feel behind. It also makes him a favorite of growing families who are trading up — a group that needs an agent willing to run the same neighborhood four times before pulling the trigger.",
            "Trevor works closely with Adam and the rest of the Adam Druck Group, tapping the team's marketing, pricing, and negotiation resources on every transaction — while giving each client the one-on-one attention of a boutique practice.",
        ],
    },
    {
        "slug": "tyler-zeller",
        "first": "Tyler",
        "last": "Zeller",
        "role": "REALTOR®",
        "title": "REALTOR®",
        "phone": "(717) 891-6430",
        "phone_tel": "+17178916430",
        "email": None,
        "photo": "/images/team/tyler.jpg",
        "license": "Licensed REALTOR® in Pennsylvania",
        "specialties": [
            "Property condition & inspection strategy",
            "Value-driven buyers",
            "Investment property analysis",
            "Move-up sellers",
        ],
        "bio_short": "A sharp eye for property condition and value — Tyler helps clients see past the paint to what a home really is.",
        "bio_long": [
            "Tyler Zeller brings a builder's eye to real estate. He can walk a showing and tell a buyer within minutes whether the roof was replaced during the last owner or two before, whether the basement moisture is a $200 fix or a $20,000 one, and whether the kitchen renovation was cosmetic or structural.",
            "That's an unusual skill set — and it's a huge advantage for buyers who don't want to get emotionally attached to a house that's going to eat them alive in year two. It's also a huge advantage for sellers, because Tyler helps clients understand exactly which improvements will move the needle at listing and which are money left on the closing table.",
            "Tyler represents buyers and sellers across York, Dallastown, Red Lion, and the broader south-of-York market, backed by the full marketing and negotiation resources of the Adam Druck Group at Coldwell Banker.",
        ],
    },
    {
        "slug": "katie-kopp",
        "first": "Katie",
        "last": "Kopp",
        "role": "REALTOR®",
        "title": "REALTOR®",
        "phone": "(717) 578-4183",
        "phone_tel": "+17175784183",
        "email": None,
        "photo": "/images/team/katie.jpg",
        "license": "Licensed REALTOR® in Pennsylvania",
        "specialties": [
            "Seller listings & staging",
            "Modern marketing & social",
            "Move-up sellers",
            "First-time sellers",
        ],
        "bio_short": "Modern marketing instincts paired with genuine warmth — Katie helps sellers present their home at its best.",
        "bio_long": [
            "Katie Kopp built her practice around a simple observation: the way a home is presented online is the way most buyers decide whether to see it in person. So she treats every listing like a small campaign — clean photography, thoughtful copy, targeted social distribution, and staging advice that respects the seller's budget and taste.",
            "The result is a listing experience that feels genuinely modern without ever being pushy. Sellers who work with Katie describe her as warm, calm, and unusually easy to reach — a rare combination in a fast market.",
            "Katie is a natural fit for first-time sellers who want the process demystified, and for move-up sellers who need a coordinated buy-and-sell plan. She works alongside the full Adam Druck Group at Coldwell Banker Realty.",
        ],
    },
    {
        "slug": "amanda-eisenhart",
        "first": "Amanda",
        "last": "Eisenhart",
        "role": "REALTOR® · Certified Global Luxury Agent",
        "title": "REALTOR® · Certified Global Luxury Agent",
        "phone": "(717) 916-9222",
        "phone_tel": "+17179169222",
        "email": None,
        "photo": "/images/team/amanda.jpg",
        "license": "Licensed REALTOR® in Pennsylvania · Coldwell Banker Global Luxury Certified",
        "specialties": [
            "Luxury residential",
            "First-time homebuyers",
            "Concierge-level service",
            "Relocation",
        ],
        "bio_short": "A Certified Global Luxury Agent with the patience and clarity to make every client — from first-timers to eight-figure buyers — feel guided.",
        "bio_long": [
            "Amanda Eisenhart is a detail-oriented real estate professional who listens closely and goes the extra mile to deliver a smooth, successful experience for every client — whether they're buying their first condo or listing a signature estate.",
            "As a Coldwell Banker Global Luxury Certified Agent, Amanda has access to a specialized marketing platform for high-end properties, including international distribution through the Wall Street Journal Real Estate portfolio and the Coldwell Banker Global Luxury network. But what her clients talk about first is her patience — she's the kind of agent who will genuinely spend an extra Saturday walking a first-time buyer through the same three houses so they can make a confident decision.",
            "Amanda serves buyers and sellers throughout York County and the surrounding Pennsylvania, Maryland, and Delaware markets as part of the Adam Druck Group at Coldwell Banker Realty.",
        ],
    },
    {
        "slug": "zach-keller",
        "first": "Zach",
        "last": "Keller",
        "role": "REALTOR®",
        "title": "REALTOR®",
        "phone": None,
        "phone_tel": None,
        "email": "zach.keller@cbrealty.com",
        "photo": "/images/team/zach.jpg",
        "license": "Licensed REALTOR® in Pennsylvania",
        "specialties": [
            "First-time buyers",
            "Luxury listings",
            "Negotiation",
            "Investment properties",
        ],
        "bio_short": "Calm, methodical, and equally at home walking a first-time buyer through inspection as negotiating on a luxury listing.",
        "bio_long": [
            "Zach Keller brings a level-headed, methodical approach to every transaction — a style that clients across every price point end up appreciating. First-time buyers get someone who never makes them feel like their questions are basic. Luxury sellers get someone who is unhurried, thorough, and willing to have the hard conversations about pricing and positioning that other agents avoid.",
            "That range — genuine comfort at every price point — is what sets Zach apart. It comes from a genuine curiosity about how real estate actually works: the financing, the inspection standards, the negotiation psychology, and the marketing tactics that actually move a listing.",
            "Zach works across York County and the surrounding tri-state region as part of the Adam Druck Group at Coldwell Banker Realty.",
        ],
    },
]

BASE_URL = "https://adamdruckgroup.com"


def nav_html():
    return """<header class="nav" id="nav">
  <div class="nav__inner">
    <a href="/" class="nav__logo" aria-label="Adam Druck Group — Home">
      <svg class="nav__logo-mark" viewBox="0 0 120 44" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <text x="0" y="30" font-family="Inter, system-ui, sans-serif" font-weight="700" font-size="28" fill="#012169">A</text>
        <text x="34" y="30" font-family="Inter, system-ui, sans-serif" font-weight="700" font-size="28" fill="#012169">D</text>
        <text x="69" y="30" font-family="Inter, system-ui, sans-serif" font-weight="700" font-size="28.5" fill="#418FDE">G</text>
        <line x1="0" y1="38" x2="103" y2="38" stroke="#012169" stroke-width="1.5"/>
      </svg>
      <span class="nav__logo-text">
        <span class="nav__logo-name">Adam Druck Group</span>
        <span class="nav__logo-sub">Coldwell Banker Realty</span>
      </span>
    </a>
    <nav class="nav__links" aria-label="Primary">
      <a href="/buy.html">Buy</a>
      <a href="/sell.html">Sell</a>
      <a href="/invest.html">Invest</a>
      <a href="/communities.html">Communities</a>
      <a href="/team/">Team</a>
      <a href="/home-value.html">Home Value</a>
      <a href="/insights.html">Insights</a>
      <a href="/contact.html">Contact</a>
      <a href="https://adamdruck.sites.cbmoxi.com/search" class="nav__cta" target="_blank" rel="noopener">Search Homes</a>
    </nav>
    <button class="nav__toggle" id="navToggle" aria-label="Open menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>"""


def footer_html():
    return """<footer class="footer">
  <div class="footer__inner">
    <div class="footer__brand">
      <p class="footer__logo">Adam Druck Group</p>
      <p class="footer__sub">at Coldwell Banker Realty</p>
      <p class="footer__addr">2451 Kingston Ct<br />York, PA 17402</p>
      <p class="footer__contact">
        <a href="tel:+17174872579">(717) 487-2579</a> ·
        <a href="mailto:yourrealtoradamd@gmail.com">yourrealtoradamd@gmail.com</a>
      </p>
    </div>
    <div class="footer__links">
      <a href="/buy.html">Buy</a>
      <a href="/sell.html">Sell</a>
      <a href="/invest.html">Invest</a>
      <a href="/communities.html">Communities</a>
      <a href="/team/">Team</a>
      <a href="/home-value.html">Home Value</a>
      <a href="/insights.html">Insights</a>
      <a href="/review.html">Leave a Review</a>
      <a href="/contact.html">Contact</a>
    </div>
    <p class="footer__legal">
      © 2026 Adam Druck Group. All rights reserved. Each office is independently owned and operated. Equal Housing Opportunity.
    </p>
  </div>
</footer>"""


def agent_page(agent):
    slug = agent["slug"]
    name = f"{agent['first']} {agent['last']}"
    url = f"{BASE_URL}/team/{slug}.html"
    page_title = f"{name} — {agent['role']} | Adam Druck Group"
    meta_desc = agent["bio_short"] + f" Contact {name} at the Adam Druck Group at Coldwell Banker Realty in York, PA."

    # Contact list
    contact_items = []
    if agent["phone"]:
        contact_items.append(f'<li><a href="tel:{agent["phone_tel"]}">{agent["phone"]}</a></li>')
    if agent["email"]:
        contact_items.append(f'<li><a href="mailto:{agent["email"]}">{agent["email"]}</a></li>')
    contact_html = "\n          ".join(contact_items)

    # CTA buttons
    cta_buttons = []
    if agent["phone_tel"]:
        cta_buttons.append(f'<a href="tel:{agent["phone_tel"]}" class="btn btn--primary">Call {agent["first"]}</a>')
        cta_buttons.append(f'<a href="sms:{agent["phone_tel"]}" class="btn btn--secondary">Text {agent["first"]}</a>')
    if agent["email"]:
        cta_buttons.append(f'<a href="mailto:{agent["email"]}" class="btn btn--secondary">Email {agent["first"]}</a>')
    cta_buttons.append('<a href="/contact.html" class="btn btn--ghost">Book a call</a>')
    cta_html = "\n        ".join(cta_buttons)

    # Bio paragraphs
    bio_html = "\n        ".join(f"<p>{p}</p>" for p in agent["bio_long"])

    # Specialties
    spec_html = "\n          ".join(f"<li>{s}</li>" for s in agent["specialties"])

    # Person JSON-LD
    person_ld = f'''
{{
  "@context": "https://schema.org",
  "@type": "RealEstateAgent",
  "@id": "{url}#person",
  "name": "{name}",
  "jobTitle": "{agent['title']}",
  "image": "{BASE_URL}{agent['photo']}",
  "url": "{url}",
  "worksFor": {{
    "@type": "RealEstateAgent",
    "@id": "{BASE_URL}/#organization",
    "name": "Adam Druck Group"
  }},
  "affiliation": {{
    "@type": "Organization",
    "name": "Coldwell Banker Realty"
  }},'''
    if agent["phone"]:
        person_ld += f'\n  "telephone": "{agent["phone_tel"]}",'
    if agent["email"]:
        person_ld += f'\n  "email": "{agent["email"]}",'
    person_ld += '''
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "2451 Kingston Ct",
    "addressLocality": "York",
    "addressRegion": "PA",
    "postalCode": "17402",
    "addressCountry": "US"
  },
  "areaServed": [
    {"@type": "AdministrativeArea", "name": "York County, PA"},
    {"@type": "AdministrativeArea", "name": "South Central Pennsylvania"}
  ]
}'''

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{page_title}</title>
<meta name="description" content="{meta_desc}" />
<meta name="theme-color" content="#012169" />
<meta name="author" content="Adam Druck Group" />
<meta name="robots" content="index, follow, max-image-preview:large" />
{GSC_TAG}

<link rel="canonical" href="{url}" />

<meta property="og:title" content="{page_title}" />
<meta property="og:description" content="{meta_desc}" />
<meta property="og:type" content="profile" />
<meta property="og:url" content="{url}" />
<meta property="og:image" content="{BASE_URL}{agent['photo']}" />
<meta property="og:site_name" content="Adam Druck Group" />
<meta property="og:locale" content="en_US" />

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{page_title}" />
<meta name="twitter:description" content="{meta_desc}" />
<meta name="twitter:image" content="{BASE_URL}{agent['photo']}" />

<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,500;9..144,600&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/styles.css" />
<link rel="icon" type="image/svg+xml" href="/favicon.svg" />

<script type="application/ld+json">
{person_ld}
</script>

<script data-goatcounter="https://adamdruckgroup.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
</head>
<body>

{nav_html()}

<main class="agent-detail">

  <section class="agent-hero">
    <div class="agent-hero__inner">
      <div class="agent-hero__photo">
        <img src="{agent['photo']}" alt="{name}, {agent['role']} at Adam Druck Group" />
      </div>
      <div class="agent-hero__body">
        <p class="eyebrow">Adam Druck Group · Coldwell Banker Realty</p>
        <h1 class="agent-hero__name"><span class="serif">{agent['first']}</span> <span class="serif italic">{agent['last']}</span></h1>
        <p class="agent-hero__role">{agent['role']}</p>
        <p class="agent-hero__lede">{agent['bio_short']}</p>
        <div class="agent-hero__cta">
        {cta_html}
        </div>
        <ul class="agent-hero__contact">
          {contact_html}
        </ul>
      </div>
    </div>
  </section>

  <section class="agent-body">
    <div class="agent-body__inner">
      <div class="agent-body__bio">
        <p class="eyebrow">About {agent['first']}</p>
        {bio_html}
      </div>
      <aside class="agent-body__side">
        <div class="agent-side-card">
          <p class="eyebrow">Specialties</p>
          <ul>
          {spec_html}
          </ul>
        </div>
        <div class="agent-side-card">
          <p class="eyebrow">License</p>
          <p>{agent['license']}</p>
        </div>
        <div class="agent-side-card agent-side-card--cta">
          <p class="eyebrow">Ready to talk?</p>
          <p>{agent['first']} responds personally to every message.</p>
          <a href="/contact.html" class="btn btn--primary btn--block">Get in touch</a>
        </div>
      </aside>
    </div>
  </section>

  <section class="agent-team-cta">
    <div class="agent-team-cta__inner">
      <p class="eyebrow">The Adam Druck Group</p>
      <h2 class="section-title"><span class="serif">Six specialists.</span> <span class="serif italic">One standard of service.</span></h2>
      <p>Every client of the Adam Druck Group gets the full weight of our team — coordinated marketing, sharp pricing, and the backing of Coldwell Banker's global network.</p>
      <a href="/team/" class="btn btn--secondary">Meet the full team</a>
    </div>
  </section>

</main>

{footer_html()}

</body>
</html>
"""


def hub_page():
    cards = []
    for a in AGENTS:
        name = f"{a['first']} {a['last']}"
        contact_line = ""
        if a["phone"]:
            contact_line = f'<a href="tel:{a["phone_tel"]}">{a["phone"]}</a>'
        elif a["email"]:
            contact_line = f'<a href="mailto:{a["email"]}">{a["email"]}</a>'
        cards.append(f'''
    <article class="team-card">
      <a href="/team/{a['slug']}.html" class="team-card__link" aria-label="Meet {name}">
        <div class="team-card__photo">
          <img src="{a['photo']}" alt="{name}, {a['role']} at Adam Druck Group" loading="lazy" />
        </div>
        <div class="team-card__body">
          <p class="team-card__role">{a['role']}</p>
          <h3 class="team-card__name">{name}</h3>
          <p class="team-card__bio">{a['bio_short']}</p>
          <p class="team-card__contact">{contact_line}</p>
          <span class="team-card__cta">View profile →</span>
        </div>
      </a>
    </article>''')

    cards_html = "\n".join(cards)
    url = f"{BASE_URL}/team/"
    title = "Meet the Team | Adam Druck Group at Coldwell Banker Realty"
    desc = "Six specialists. One standard of service. Meet the agents of the Adam Druck Group — a top-producing real estate team serving York County, Pennsylvania and the surrounding tri-state region."

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<meta name="theme-color" content="#012169" />
<meta name="author" content="Adam Druck Group" />
<meta name="robots" content="index, follow, max-image-preview:large" />
{GSC_TAG}

<link rel="canonical" href="{url}" />

<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:type" content="website" />
<meta property="og:url" content="{url}" />
<meta property="og:image" content="{BASE_URL}/images/hero/york-hero.jpg" />
<meta property="og:site_name" content="Adam Druck Group" />
<meta property="og:locale" content="en_US" />

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{title}" />
<meta name="twitter:description" content="{desc}" />
<meta name="twitter:image" content="{BASE_URL}/images/hero/york-hero.jpg" />

<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,500;9..144,600&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/styles.css" />
<link rel="icon" type="image/svg+xml" href="/favicon.svg" />

<script data-goatcounter="https://adamdruckgroup.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
</head>
<body>

{nav_html()}

<main class="team-hub">

  <section class="team-hub__hero">
    <div class="team-hub__hero-inner">
      <p class="eyebrow">Meet the Group</p>
      <h1 class="section-title">
        <span class="serif">Six specialists.</span>
        <span class="serif italic">One standard of service.</span>
      </h1>
      <p class="team-hub__lede">
        The Adam Druck Group is a boutique real estate team at Coldwell Banker Realty —
        a group of specialists rooted in York County, backed by generational local knowledge
        and Coldwell Banker's global marketing network.
      </p>
    </div>
  </section>

  <section class="team-hub__grid-section">
    <div class="team-hub__grid">
      {cards_html}
    </div>
  </section>

  <section class="team-hub__cta">
    <div class="team-hub__cta-inner">
      <p class="eyebrow">Ready to talk?</p>
      <h2 class="section-title"><span class="serif">Let's make it</span> <span class="serif italic">the easy part.</span></h2>
      <p>Whatever your next move — buying, selling, investing, relocating — one of our agents is the right fit. Tell us what you're working on and we'll take it from there.</p>
      <a href="/contact.html" class="btn btn--primary">Contact the team</a>
    </div>
  </section>

</main>

{footer_html()}

</body>
</html>
"""


def main():
    # Write individual agent pages
    for agent in AGENTS:
        out = TEAM_DIR / f"{agent['slug']}.html"
        out.write_text(agent_page(agent))
        print(f"Wrote {out.relative_to(SITE_ROOT)}")

    # Write /team/ hub (index.html inside /team/)
    hub_out = TEAM_DIR / "index.html"
    hub_out.write_text(hub_page())
    print(f"Wrote {hub_out.relative_to(SITE_ROOT)}")


if __name__ == "__main__":
    main()

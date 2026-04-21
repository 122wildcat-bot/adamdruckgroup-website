#!/usr/bin/env python3
"""Generate the dedicated Contact page with Adam first, then all agents."""
import sys, os, importlib.util
spec = importlib.util.spec_from_file_location("shell_mod", os.path.join(os.path.dirname(__file__), "_page-shell.py"))
shell_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(shell_mod)
shell = shell_mod.shell

# Agent roster (Adam first, then alphabetical by first name)
AGENTS = [
    {
        "slug": "adam",
        "name": "Adam Druck",
        "role": "Team Lead · REALTOR®",
        "bio": "Fourth-generation York County native. 500+ transactions across PA, MD, and DE. Specializes in investor deals, listings, and complex buy-side negotiations.",
        "phone": "(717) 487-2579",
        "phone_href": "+17174872579",
        "email": "yourrealtoradamd@gmail.com",
        "licenses": "PA · MD · DE",
        "license_num": "RS-0038815 (PA)",
        "lead": True,
    },
    {
        "slug": "amanda",
        "name": "Amanda Eisenhart",
        "role": "REALTOR®",
        "bio": "Amanda brings empathy and deep market knowledge to every client relationship — a steady guide for first-time buyers and move-up families navigating the emotional side of the sale.",
        "phone": "(717) 659-4844",
        "phone_href": "+17176594844",
        "email": "movewithamandae@gmail.com",
        "licenses": "PA · MD",
        "license_num": None,
        "lead": False,
    },
    {
        "slug": "katie",
        "name": "Katie Kopp",
        "role": "REALTOR®",
        "bio": "Katie pairs modern marketing instincts with genuine warmth — a trusted resource for listings that need strong digital presence and buyers who want honest, thorough representation.",
        "phone": "(717) 578-4183",
        "phone_href": "+17175784183",
        "email": "katie.kopp@cbrealty.com",
        "licenses": "PA",
        "license_num": None,
        "lead": False,
    },
    {
        "slug": "trevor",
        "name": "Trevor Stuck",
        "role": "REALTOR®",
        "bio": "A consultative agent known for patient, detail-driven representation. Trevor works with first-time buyers, growing families, and sellers across York County and the surrounding region.",
        "phone": "(717) 599-2375",
        "phone_href": "+17175992375",
        "email": "trevorstuck.realtor@gmail.com",
        "licenses": "PA",
        "license_num": None,
        "lead": False,
    },
    {
        "slug": "tyler",
        "name": "Tyler Zeller",
        "role": "REALTOR®",
        "bio": "Tyler brings a sharp eye for property condition and value to every showing. Guiding buyers through inspections, offers, and closing with patient, informed counsel.",
        "phone": "(717) 891-6430",
        "phone_href": "+17178916430",
        "email": "tylerzellerrealtor@gmail.com",
        "licenses": "PA",
        "license_num": None,
        "lead": False,
    },
    {
        "slug": "zach",
        "name": "Zach Keller",
        "role": "REALTOR®",
        "bio": "Zach brings a calm, methodical approach to every transaction — equally comfortable walking a first-time buyer through their first inspection or negotiating terms on a luxury listing.",
        "phone": None,  # User has not provided Zach's phone yet
        "phone_href": None,
        "email": "zach.keller@cbrealty.com",
        "licenses": "PA",
        "license_num": None,
        "lead": False,
    },
]

def agent_card(agent):
    lead_class = " agent--lead" if agent["lead"] else ""
    license_line = f'        <p class="agent__license">License {agent["license_num"]} · Licensed in {agent["licenses"]}</p>' if agent["license_num"] else f'        <p class="agent__license">Licensed in {agent["licenses"]}</p>'
    phone_li = f'        <li><a href="tel:{agent["phone_href"]}">{agent["phone"]}</a></li>' if agent.get("phone") else ""
    contact_items = "\n".join(x for x in [phone_li, f'        <li><a href="mailto:{agent["email"]}">{agent["email"]}</a></li>'] if x)
    return f"""  <article class="agent{lead_class}">
    <div class="agent__photo">
      <img src="/images/team/{agent['slug']}.jpg" alt="{agent['name']}, REALTOR" loading="lazy" />
    </div>
    <div class="agent__body">
      <p class="agent__role">{agent['role']}</p>
      <h3 class="agent__name">{agent['name']}</h3>
      <p class="agent__bio">{agent['bio']}</p>
      <ul class="agent__contact">
{contact_items}
      </ul>
{license_line}
    </div>
  </article>"""

# Build body
lead_agent = AGENTS[0]
other_agents = AGENTS[1:]

body = f"""
<!-- ========== PAGE LEAD ========== -->
<section class="page-lead">
  <div class="page-lead__inner">
    <p class="eyebrow page-lead__eyebrow">Contact</p>
    <h1 class="page-lead__title">
      Let&rsquo;s <em class="italic">talk.</em>
    </h1>
    <p class="page-lead__lede">
      Every client works directly with the agent best suited to the job. Start with Adam or
      reach out to any team member below — we&rsquo;ll make sure you&rsquo;re matched right.
    </p>
    <div class="page-lead__cta">
      <a href="/#contact" class="btn btn--primary">Send a Message</a>
      <a href="tel:+17174872579" class="btn btn--ghost">(717) 487-2579</a>
    </div>
  </div>
</section>

<!-- ========== TEAM LEAD ========== -->
<section class="section" id="team-lead">
  <div class="section__inner">
    <div class="section__head">
      <p class="eyebrow">Start here</p>
      <h2 class="section-title">Team <span class="italic">lead.</span></h2>
    </div>
    <div class="team__grid team__grid--lead">
{agent_card(lead_agent)}
    </div>
  </div>
</section>

<!-- ========== AGENTS ========== -->
<section class="section section--cream" id="agents">
  <div class="section__inner">
    <div class="section__head">
      <p class="eyebrow">Our agents</p>
      <h2 class="section-title">The full <span class="italic">roster.</span></h2>
      <p class="page-lead__lede" style="margin-top:1rem;">
        Each agent brings a distinct style and specialty &mdash; we match you based on what you&rsquo;re buying, selling, or building.
      </p>
    </div>
    <div class="team__grid">
{chr(10).join(agent_card(a) for a in other_agents)}
    </div>
  </div>
</section>

<!-- ========== OFFICE INFO ========== -->
<section class="section section--ink" id="office">
  <div class="section__inner">
    <div class="two-col">
      <div>
        <p class="eyebrow">Visit the office</p>
        <h2 class="section-title" style="color: var(--paper);">Coldwell Banker Realty<br>&mdash; <span class="italic">York office.</span></h2>
        <p class="page-lead__lede" style="color: rgba(255,255,255,0.85);">
          Stop by for a sit-down, or schedule a call from wherever you are. We cover all of
          South Central Pennsylvania plus Northern Maryland and Delaware &mdash; most meetings
          happen at the property, over coffee, or by video.
        </p>
      </div>
      <div>
        <div class="office-info">
          <p class="eyebrow" style="color: var(--celestial-light);">Address</p>
          <p>2251 Eastern Blvd, Ste 201<br>York, PA 17402</p>
          <p class="eyebrow" style="color: var(--celestial-light); margin-top:2rem;">Direct line</p>
          <p><a href="tel:+17174872579">(717) 487-2579</a></p>
          <p class="eyebrow" style="color: var(--celestial-light); margin-top:2rem;">Email</p>
          <p><a href="mailto:yourrealtoradamd@gmail.com">yourrealtoradamd@gmail.com</a></p>
          <p class="eyebrow" style="color: var(--celestial-light); margin-top:2rem;">Licensed in</p>
          <p>Pennsylvania &middot; Maryland &middot; Delaware</p>
        </div>
      </div>
    </div>
  </div>
</section>
"""

html = shell(
    title="Contact Adam Druck & the Adam Druck Group | Coldwell Banker Realty",
    description="Reach Adam Druck or any agent on the Adam Druck Group team directly. Licensed across Pennsylvania, Maryland, and Delaware at Coldwell Banker Realty.",
    canonical_slug="contact.html",
    body_html=body,
)

with open("/home/user/workspace/adamdruckgroup/contact.html", "w") as f:
    f.write(html)

print(f"✓ contact.html ({len(html):,} bytes)")

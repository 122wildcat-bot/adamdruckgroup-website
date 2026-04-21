#!/usr/bin/env python3
"""Build all Adam Druck Group sub-pages using the shared shell."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
# Import shell function from _page-shell.py (dash in filename → importlib)
import importlib.util
spec = importlib.util.spec_from_file_location("shell_mod", os.path.join(os.path.dirname(__file__), "_page-shell.py"))
shell_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(shell_mod)
shell = shell_mod.shell

OUT = os.path.dirname(__file__)

# ======================================================================
# BUY
# ======================================================================
buy_body = """
<section class="page-lead">
  <div class="page-lead__inner">
    <p class="eyebrow page-lead__eyebrow">For Buyers</p>
    <h1 class="page-lead__title">
      The right home. <span class="italic">The right terms.</span>
    </h1>
    <p class="page-lead__lede">
      From first-home buyers navigating PHFA programs to discerning clients seeking
      discreet representation — we negotiate, inspect, and advocate like the keys
      are our own. Licensed across Pennsylvania, Maryland, and Delaware.
    </p>
    <div class="page-lead__cta">
      <a href="https://adamdruck.sites.cbmoxi.com/search" target="_blank" rel="noopener" class="btn btn--primary">Search Homes</a>
      <a href="/#contact" class="btn btn--ghost">Start a Buyer Call</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="section__inner">
    <div class="two-col">
      <div>
        <p class="eyebrow">The Buyer Experience</p>
        <h2 class="section-title" style="margin-bottom: 1.5rem;">
          Everything you need, <span class="italic">in the right order.</span>
        </h2>
        <p style="color: var(--slate); font-size: 1.05rem; line-height: 1.65; max-width: 55ch;">
          A home purchase has more than twenty moving pieces. We keep them in sequence
          so you can focus on the home, not the process.
        </p>
      </div>
      <div>
        <ol class="feature-list">
          <li><div class="ico">1</div><div>
            <h3>Lender Introductions</h3>
            <p>We connect you with trusted local lenders so you can compare rates and pick the right fit — before you fall in love with a home you can't secure.</p>
          </div></li>
          <li><div class="ico">2</div><div>
            <h3>Curated Home Search</h3>
            <p>We send only the listings worth your time, including off-market homes surfaced through our network — not algorithmic noise.</p>
          </div></li>
          <li><div class="ico">3</div><div>
            <h3>Honest Walkthroughs</h3>
            <p>At every showing we point out roof age, electrical concerns, moisture signs, and resale considerations — before you're under contract, not after.</p>
          </div></li>
          <li><div class="ico">4</div><div>
            <h3>Strategic Offers</h3>
            <p>We craft offers that win in today's market: escalation clauses, smart contingencies, and the terms that matter most to the seller on the other side.</p>
          </div></li>
          <li><div class="ico">5</div><div>
            <h3>Inspection &amp; Negotiation</h3>
            <p>We negotiate repair credits with purpose and protect your earnest money through every contingency period.</p>
          </div></li>
          <li><div class="ico">6</div><div>
            <h3>Closing &amp; Beyond</h3>
            <p>We attend every closing in person — and stay in touch long after, for refinances, renovations, and your next move.</p>
          </div></li>
        </ol>
      </div>
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="section__inner">
    <div class="section__head">
      <p class="eyebrow">Who We Serve</p>
      <h2 class="section-title">Every buyer, <span class="italic">every price point.</span></h2>
    </div>
    <div class="client-types">
      <div class="client-type">
        <span class="client-type__num">01</span>
        <h3>First-Time Buyers</h3>
        <p>Patient guidance through financing options, inspections, and the offer process — at the pace that's right for you.</p>
      </div>
      <div class="client-type">
        <span class="client-type__num">02</span>
        <h3>Move-Up &amp; Move-Down</h3>
        <p>Sophisticated sequencing between the sale of your current home and the purchase of your next — with minimal gap and maximum leverage.</p>
      </div>
      <div class="client-type">
        <span class="client-type__num">03</span>
        <h3>Luxury &amp; Estate</h3>
        <p>Discreet representation, curated showings, and negotiation fluency for properties above the $700K threshold.</p>
      </div>
      <div class="client-type">
        <span class="client-type__num">04</span>
        <h3>Relocation Buyers</h3>
        <p>Virtual tours, neighborhood orientation, and local expertise for clients moving into York County from out of state.</p>
      </div>
      <div class="client-type">
        <span class="client-type__num">05</span>
        <h3>New Construction</h3>
        <p>We represent you at the builder's table — where having your own advocate matters more than most buyers realize.</p>
      </div>
      <div class="client-type">
        <span class="client-type__num">06</span>
        <h3>Tri-State Buyers</h3>
        <p>Licensed and active in PA, MD, and DE — so a shift in your search zone doesn't require a new agent.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--ink">
  <div class="section__inner" style="text-align: center; max-width: 720px;">
    <p class="eyebrow">Ready When You Are</p>
    <h2 class="section-title" style="color: var(--paper); margin-bottom: 1.5rem;">
      Let's start the search <span class="italic" style="color: var(--celestial-light);">with a conversation.</span>
    </h2>
    <p style="color: rgba(253, 252, 248, 0.75); font-size: 1.1rem; line-height: 1.6; margin-bottom: 2.5rem; max-width: 55ch; margin-left: auto; margin-right: auto;">
      Twenty minutes on a call. We'll learn what you're looking for, share what's realistic,
      and build a custom shortlist within one business day.
    </p>
    <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 1rem;">
      <a href="/#contact" class="btn btn--primary">Start a Buyer Call</a>
      <a href="tel:+17174872579" class="btn btn--ghost" style="color: var(--paper); border-color: rgba(253,252,248,0.3);">(717) 487-2579</a>
    </div>
  </div>
</section>
"""

# ======================================================================
# SELL
# ======================================================================
sell_body = """
<section class="page-lead">
  <div class="page-lead__inner">
    <p class="eyebrow page-lead__eyebrow">For Sellers</p>
    <h1 class="page-lead__title">
      Sell for more. <span class="italic">Sell with confidence.</span>
    </h1>
    <p class="page-lead__lede">
      Coldwell Banker Realty's global reach paired with our York County roots.
      We price with precision, stage with purpose, and market with the same rigor
      we'd bring to our own homes.
    </p>
    <div class="page-lead__cta">
      <a href="#valuation" class="btn btn--primary">Get My Home's Value</a>
      <a href="tel:+17174872579" class="btn btn--ghost">(717) 487-2579</a>
    </div>
  </div>
</section>

<section class="section" id="valuation">
  <div class="section__inner">
    <div class="valuation-cta">
      <div>
        <p class="eyebrow">Complimentary &amp; No Obligation</p>
        <h2>What's your home worth <span style="font-style:italic; color: var(--celestial-light);">in today's market?</span></h2>
        <p>
          A real local valuation — not an algorithmic estimate. We'll send a side-by-side
          analysis of recent comparable sales, active competition in your market, and a
          realistic price range. Usually within one business day.
        </p>
      </div>
      <form class="valuation-form" onsubmit="handleValuation(event)">
        <div>
          <label>Property address</label>
          <input name="address" placeholder="123 Main St, York PA 17402" required />
        </div>
        <div>
          <label>Email</label>
          <input type="email" name="email" placeholder="you@example.com" required />
        </div>
        <div>
          <label>Phone (optional)</label>
          <input type="tel" name="phone" placeholder="(717) 487-2579" />
        </div>
        <div>
          <label>Timeline</label>
          <select name="timeline">
            <option>Within 30 days</option>
            <option>1–3 months</option>
            <option>3–6 months</option>
            <option>Just curious for now</option>
          </select>
        </div>
        <button type="submit" class="btn btn--primary">Request My Valuation</button>
      </form>
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="section__inner">
    <div class="section__head" style="margin: 0 auto 4rem; text-align: center;">
      <p class="eyebrow">The Listing Process</p>
      <h2 class="section-title">
        Six steps. <span class="italic">One seamless sale.</span>
      </h2>
    </div>
    <div class="steps">
      <div class="step"><h3>Pricing Strategy</h3><p>Real comparable sales, real market positioning — engineered to drive multiple offers rather than chase the market down.</p></div>
      <div class="step"><h3>Pre-Listing Prep</h3><p>Stager consultation, paint and repair recommendations, and trusted contractor referrals to maximize your return.</p></div>
      <div class="step"><h3>Professional Marketing</h3><p>HDR photography, drone, walkthrough video, and 3D tours — paired with targeted social and search campaigns.</p></div>
      <div class="step"><h3>Strategic Launch</h3><p>Coordinated coming-soon, agent-network outreach, and timed open houses to concentrate demand on day one.</p></div>
      <div class="step"><h3>Offer Review</h3><p>We compare every offer side-by-side — net proceeds, terms, contingencies, and buyer strength — so you choose with clarity.</p></div>
      <div class="step"><h3>Smooth Close</h3><p>We manage inspection, appraisal, and timeline — so you can pack, not negotiate every detail.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="section__inner">
    <div class="two-col">
      <div>
        <p class="eyebrow">Marketing That Matters</p>
        <h2 class="section-title">Your home, <span class="italic">presented properly.</span></h2>
        <p style="color: var(--slate); font-size: 1.05rem; line-height: 1.7; max-width: 55ch;">
          A sign in the yard and an MLS upload is not a marketing plan. Every listing
          we take receives the full treatment — because the first two weeks on market
          determine how the next six will go.
        </p>
        <ul class="feature-list" style="margin-top: 2rem;">
          <li><div class="ico">—</div><div>
            <h3>Professional Photography</h3>
            <p>HDR-blended interior and exterior, shot at the right time of day for the right rooms.</p>
          </div></li>
          <li><div class="ico">—</div><div>
            <h3>Drone &amp; Video</h3>
            <p>Aerial context for the property and neighborhood, plus a walkthrough video buyers can share with their families.</p>
          </div></li>
          <li><div class="ico">—</div><div>
            <h3>Targeted Digital Campaigns</h3>
            <p>Paid placement on social and search platforms, targeted to active buyers in your price tier and geography.</p>
          </div></li>
          <li><div class="ico">—</div><div>
            <h3>Agent Network Outreach</h3>
            <p>Direct email and phone outreach to top-producing agents in your region — before the listing goes live.</p>
          </div></li>
        </ul>
      </div>
      <div style="background: var(--cream); padding: 3rem; border-left: 3px solid var(--celestial);">
        <p class="eyebrow">Recent Result</p>
        <p style="font-family: var(--serif); font-size: 1.35rem; line-height: 1.45; font-style: italic; color: var(--ink); margin: 0 0 1.5rem;">
          &ldquo;Adam was so helpful and professional during the sale of our home.
          He priced our home so we received multiple offers within a couple days —
          the offer we accepted was over our list price and we settled within 30 days.&rdquo;
        </p>
        <p style="margin: 0; font-size: 0.78rem; letter-spacing: 0.15em; text-transform: uppercase; font-weight: 600; color: var(--muted);">
          — Verified Seller, York PA &middot; Zillow
        </p>
      </div>
    </div>
  </div>
</section>

<script>
function handleValuation(e) {
  e.preventDefault();
  const data = Object.fromEntries(new FormData(e.target));
  const subject = encodeURIComponent('Home Valuation Request — ' + (data.address || ''));
  const body = encodeURIComponent(
    'Address: ' + (data.address || '') + '\\n' +
    'Email: ' + (data.email || '') + '\\n' +
    'Phone: ' + (data.phone || '') + '\\n' +
    'Timeline: ' + (data.timeline || '') + '\\n\\n' +
    'Please send a complimentary market valuation for the above property.'
  );
  window.location.href = 'mailto:yourrealtoradamd@gmail.com?subject=' + subject + '&body=' + body;
  const btn = e.target.querySelector('button[type="submit"]');
  const original = btn.textContent;
  btn.textContent = 'Opening Email...';
  btn.disabled = true;
  setTimeout(() => {
    btn.textContent = 'Request Sent ✓';
    setTimeout(() => { e.target.reset(); btn.textContent = original; btn.disabled = false; }, 2500);
  }, 600);
}
</script>
"""

# ======================================================================
# INVEST
# ======================================================================
invest_body = """
<section class="page-lead">
  <div class="page-lead__inner">
    <p class="eyebrow page-lead__eyebrow">For Investors</p>
    <h1 class="page-lead__title">
      Where serious investors <span class="italic">find the right deals.</span>
    </h1>
    <p class="page-lead__lede">
      Flips, BRRRRs, buy-and-hold, and long-term portfolio building — with an agent
      who can underwrite a deal in their head while standing in the basement.
      Fourth-generation construction family. Off-market flow. Real numbers.
    </p>
    <div class="page-lead__cta">
      <a href="/#contact" class="btn btn--primary">Get on the Deal List</a>
      <a href="tel:+17174872579" class="btn btn--ghost">(717) 487-2579</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="section__inner">
    <div class="two-col">
      <div>
        <p class="eyebrow">Why Investors Work With Us</p>
        <h2 class="section-title">An agent <span class="italic">in the trenches with you.</span></h2>
        <p style="color: var(--slate); font-size: 1.05rem; line-height: 1.7; max-width: 55ch;">
          Most agents send you Zillow links. We send spreadsheets. Adam has personally
          analyzed, funded, flipped, held, and sold York County deals — and brings that
          lens to every property you walk with us.
        </p>
        <p style="color: var(--slate); font-size: 1.05rem; line-height: 1.7; max-width: 55ch;">
          We don't just open the door. We tell you what the rehab will cost, what it
          should appraise for, and whether the numbers actually make sense — before
          you write the offer.
        </p>
        <a href="/#contact" class="btn btn--primary" style="margin-top: 1rem;">Request Deal Flow</a>
      </div>
      <div>
        <ul class="feature-list">
          <li><div class="ico">—</div><div>
            <h3>Off-Market Deal Flow</h3>
            <p>Pocket listings, distressed sellers, and pre-MLS opportunities surfaced through our local investor network.</p>
          </div></li>
          <li><div class="ico">—</div><div>
            <h3>Underwriting Support</h3>
            <p>ARV, rehab scope, holding costs, and exit modeling — worked through with you, not around you.</p>
          </div></li>
          <li><div class="ico">—</div><div>
            <h3>Vetted Contractor Network</h3>
            <p>General contractors, electricians, plumbers, and roofers we have personally used and would hire again.</p>
          </div></li>
          <li><div class="ico">—</div><div>
            <h3>Lender Connections</h3>
            <p>Hard money, DSCR, conventional, and portfolio lenders — matched to the capital structure your deal actually needs.</p>
          </div></li>
          <li><div class="ico">—</div><div>
            <h3>Cash-Flow Analysis</h3>
            <p>Real rents, real expenses, real cash-on-cash and DSCR figures — not pro-forma fantasy.</p>
          </div></li>
          <li><div class="ico">—</div><div>
            <h3>1031 &amp; Portfolio Strategy</h3>
            <p>Scale, refinance, exchange, exit. We help you build the portfolio — not just buy the property.</p>
          </div></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="section__inner">
    <div class="section__head" style="text-align: center; margin: 0 auto 3.5rem;">
      <p class="eyebrow">Investor FAQ</p>
      <h2 class="section-title">Straight answers <span class="italic">to the questions investors ask.</span></h2>
    </div>
    <div class="faq" style="max-width: 780px; margin: 0 auto;">
      <details open>
        <summary>Do you surface deals before they hit the MLS?</summary>
        <p>Yes. A meaningful portion of our investor closings come from off-market or pre-MLS sources we cultivate — pocket listings, wholesaler relationships, and direct seller leads. The first call is to decide what qualifies for you.</p>
      </details>
      <details>
        <summary>Can you estimate rehab costs before I submit an offer?</summary>
        <p>We'll walk the property with you, provide our honest scope estimate, and bring in our trusted general contractor for a formal bid — typically before your inspection period ends.</p>
      </details>
      <details>
        <summary>Do you work with out-of-state investors?</summary>
        <p>Yes. A significant share of our investor clients live outside Pennsylvania. We serve as your boots on the ground and quarterback the full project remotely — walkthroughs, inspections, contractor coordination, and closing.</p>
      </details>
      <details>
        <summary>What exit strategies do you help model?</summary>
        <p>Flip, BRRRR refinance, long-term hold, 1031 exchange, and owner-occupy-to-rental transitions. We build the model alongside you so the strategy and the property are chosen together.</p>
      </details>
      <details>
        <summary>What's your fee structure for active investors?</summary>
        <p>Standard buy-side commission, paid by the seller in the majority of transactions. For volume relationships there are flat-fee and rebate structures worth a direct conversation.</p>
      </details>
      <details>
        <summary>Do you also work with new-construction investors?</summary>
        <p>Yes — through our building arm we have direct experience with barndominium new builds and small-scale development in York County. Ask us about NHSG LLC projects.</p>
      </details>
    </div>
  </div>
</section>

<section class="section section--ink">
  <div class="section__inner" style="text-align: center; max-width: 720px;">
    <p class="eyebrow">Deal Flow Starts With a Call</p>
    <h2 class="section-title" style="color: var(--paper); margin-bottom: 1.5rem;">
      Tell us what you're <span class="italic" style="color: var(--celestial-light);">actually looking for.</span>
    </h2>
    <p style="color: rgba(253, 252, 248, 0.78); font-size: 1.1rem; line-height: 1.6; margin-bottom: 2.5rem; max-width: 55ch; margin-left: auto; margin-right: auto;">
      Target buy-box, capital available, timeline, and exit. We'll line up the opportunities
      that fit — and save you the ones that don't.
    </p>
    <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 1rem;">
      <a href="/#contact" class="btn btn--primary">Request Deal Flow</a>
      <a href="tel:+17174872579" class="btn btn--ghost" style="color: var(--paper); border-color: rgba(253,252,248,0.3);">(717) 487-2579</a>
    </div>
  </div>
</section>
"""

# ======================================================================
# COMMUNITIES
# ======================================================================
communities_body = """
<section class="page-lead">
  <div class="page-lead__inner">
    <p class="eyebrow page-lead__eyebrow">Communities</p>
    <h1 class="page-lead__title">
      Pennsylvania, Maryland, <span class="italic">Delaware.</span>
    </h1>
    <p class="page-lead__lede">
      Licensed in all three states, active across the region. School districts,
      commute times, and the character of each community — the context that
      doesn't show up in a listing photo.
    </p>
    <div class="page-lead__cta">
      <a href="https://adamdruck.sites.cbmoxi.com/search" target="_blank" rel="noopener" class="btn btn--primary">Search Homes</a>
      <a href="/#contact" class="btn btn--ghost">Tour a Neighborhood</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="section__inner">
    <div class="hoods-group">
      <h2 class="hoods-group__title">Pennsylvania</h2>
      <div class="hoods">
        <div class="hood">
          <div class="hood-bg" style="background: linear-gradient(135deg, var(--cb-blue), var(--celestial));"></div>
          <div class="hood__label"><h3>Spring Garden &middot; York</h3><p>Historic · Walkable</p></div>
        </div>
        <div class="hood">
          <div class="hood-bg" style="background: linear-gradient(135deg, var(--slate), var(--cb-blue));"></div>
          <div class="hood__label"><h3>Dover Township</h3><p>Family · Growing</p></div>
        </div>
        <div class="hood">
          <div class="hood-bg" style="background: linear-gradient(135deg, var(--cb-blue-deep), var(--celestial));"></div>
          <div class="hood__label"><h3>Dallastown</h3><p>Schools · Quiet</p></div>
        </div>
        <div class="hood">
          <div class="hood-bg" style="background: linear-gradient(135deg, var(--celestial), var(--cream-dark));"></div>
          <div class="hood__label"><h3>Red Lion</h3><p>Value · Acreage</p></div>
        </div>
        <div class="hood">
          <div class="hood-bg" style="background: linear-gradient(135deg, #3a5578, var(--celestial-light));"></div>
          <div class="hood__label"><h3>Hanover &amp; West Manchester</h3><p>Commuter · Active</p></div>
        </div>
        <div class="hood">
          <div class="hood-bg" style="background: linear-gradient(135deg, var(--cb-blue), var(--slate));"></div>
          <div class="hood__label"><h3>Stewartstown</h3><p>Rural · Maryland Border</p></div>
        </div>
        <div class="hood">
          <div class="hood-bg" style="background: linear-gradient(135deg, var(--cream-dark), var(--celestial));"></div>
          <div class="hood__label"><h3>East Berlin &amp; Wrightsville</h3><p>River · Character</p></div>
        </div>
        <div class="hood">
          <div class="hood-bg" style="background: linear-gradient(135deg, var(--cb-blue-deep), var(--cb-blue));"></div>
          <div class="hood__label"><h3>Harrisburg Metro</h3><p>Capital Region</p></div>
        </div>
      </div>
    </div>

    <div class="hoods-group">
      <h2 class="hoods-group__title">Maryland &amp; Delaware</h2>
      <div class="hoods">
        <div class="hood">
          <div class="hood-bg" style="background: linear-gradient(135deg, var(--slate), var(--celestial));"></div>
          <div class="hood__label"><h3>Aberdeen &middot; Harford County</h3><p>Commuter · APG-Adjacent</p></div>
        </div>
        <div class="hood">
          <div class="hood-bg" style="background: linear-gradient(135deg, var(--celestial-light), var(--cb-blue));"></div>
          <div class="hood__label"><h3>Bel Air &amp; Northern MD</h3><p>Family · Schools</p></div>
        </div>
        <div class="hood">
          <div class="hood-bg" style="background: linear-gradient(135deg, var(--cb-blue), var(--cream-dark));"></div>
          <div class="hood__label"><h3>Elkton &middot; Cecil County</h3><p>Value · Commuter Bridge</p></div>
        </div>
        <div class="hood">
          <div class="hood-bg" style="background: linear-gradient(135deg, var(--cb-blue-deep), var(--celestial));"></div>
          <div class="hood__label"><h3>Northern Delaware</h3><p>Licensed &amp; Active</p></div>
        </div>
      </div>
    </div>

    <p style="text-align: center; color: var(--muted); margin-top: 4rem; font-size: 1.05rem;">
      Don't see your area? We're licensed in
      <strong style="color: var(--cb-blue);">PA, MD, and DE</strong>
      and transact across the region regularly.
      <a href="/#contact" style="color: var(--cb-blue); text-decoration: underline; text-underline-offset: 3px;">Tell us where you're looking &rarr;</a>
    </p>
  </div>
</section>
"""

# ======================================================================
# INSIGHTS
# ======================================================================
insights_body = """
<section class="page-lead">
  <div class="page-lead__inner">
    <p class="eyebrow page-lead__eyebrow">Insights</p>
    <h1 class="page-lead__title">
      Real numbers. <span class="italic">Local context.</span>
    </h1>
    <p class="page-lead__lede">
      Market notes, buyer and seller guides, and investor playbooks — all
      grounded in actual York County transactions and data.
    </p>
    <p style="color: var(--muted); font-style: italic; font-family: var(--serif); font-size: 1.1rem;">
      First articles publishing soon. Want notes delivered as they go live?
      <a href="/#contact" style="color: var(--cb-blue); text-decoration: underline;">Join the list.</a>
    </p>
  </div>
</section>

<section class="section">
  <div class="section__inner">
    <div class="posts">
      <article class="post">
        <div class="post__cover post__cover--p1"><span class="post__cover-mark">&ldquo;</span></div>
        <div class="post__body">
          <p class="post__meta">Market Report &middot; Coming Soon</p>
          <h3 class="post__title">Q1 York County: Inventory, Pricing &amp; What Spring Actually Looks Like</h3>
          <p class="post__dek">A clear read on whether spring will behave like last year — with charts that actually matter to buyers, sellers, and investors.</p>
          <span class="post__tag">Coming Soon</span>
        </div>
      </article>

      <article class="post">
        <div class="post__cover post__cover--p2"><span class="post__cover-mark">&ldquo;</span></div>
        <div class="post__body">
          <p class="post__meta">Investor Guide &middot; Coming Soon</p>
          <h3 class="post__title">The 70% Rule, Reconsidered: Flip Math for York's Real Margins</h3>
          <p class="post__dek">Why the standard formula misses local realities — and how we actually underwrite the deals we bring investors.</p>
          <span class="post__tag">Coming Soon</span>
        </div>
      </article>

      <article class="post">
        <div class="post__cover post__cover--p3"><span class="post__cover-mark">&ldquo;</span></div>
        <div class="post__body">
          <p class="post__meta">First-Time Buyers &middot; Coming Soon</p>
          <h3 class="post__title">Pennsylvania First-Time Buyer Programs Most Lenders Won't Mention</h3>
          <p class="post__dek">Down-payment assistance, PHFA loan structures, and tax credits that quietly save thousands at closing.</p>
          <span class="post__tag">Coming Soon</span>
        </div>
      </article>

      <article class="post">
        <div class="post__cover post__cover--p4"><span class="post__cover-mark">&ldquo;</span></div>
        <div class="post__body">
          <p class="post__meta">Sellers &middot; Coming Soon</p>
          <h3 class="post__title">Pricing Strategy: Why &lsquo;Just List High&rsquo; Costs You Money</h3>
          <p class="post__dek">The data behind multiple-offer pricing — and what to actually do in a normalizing market.</p>
          <span class="post__tag">Coming Soon</span>
        </div>
      </article>

      <article class="post">
        <div class="post__cover post__cover--p5"><span class="post__cover-mark">&ldquo;</span></div>
        <div class="post__body">
          <p class="post__meta">Investor Case Study &middot; Coming Soon</p>
          <h3 class="post__title">BRRRR in York County: A Real Deal, From Acquisition to Refi</h3>
          <p class="post__dek">Walking through a single-family project with honest numbers — purchase, rehab, rent, refinance, and long-term hold economics.</p>
          <span class="post__tag">Coming Soon</span>
        </div>
      </article>

      <article class="post">
        <div class="post__cover post__cover--p6"><span class="post__cover-mark">&ldquo;</span></div>
        <div class="post__body">
          <p class="post__meta">Neighborhood Spotlight &middot; Coming Soon</p>
          <h3 class="post__title">Why Dover Township Deserves a Second Look</h3>
          <p class="post__dek">Rents, vacancies, schools, and the development pipeline — the full picture behind a market that's quietly moving.</p>
          <span class="post__tag">Coming Soon</span>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="section__inner" style="text-align: center; max-width: 680px;">
    <p class="eyebrow">Delivered When Published</p>
    <h2 class="section-title">Get notes <span class="italic">when they go live.</span></h2>
    <p style="color: var(--slate); font-size: 1.05rem; margin-bottom: 2rem;">
      A short monthly email with the latest report and one or two pieces worth reading. No noise.
    </p>
    <a href="/#contact" class="btn btn--primary">Join the List</a>
  </div>
</section>
"""

# ======================================================================
# ABOUT
# ======================================================================
about_body = """
<section class="page-lead">
  <div class="page-lead__inner">
    <p class="eyebrow page-lead__eyebrow">About</p>
    <h1 class="page-lead__title">
      Born in York. <span class="italic">Built for York real estate.</span>
    </h1>
    <p class="page-lead__lede">
      Four generations of York County roots. Two hundred-plus families served across
      Pennsylvania, Maryland, and Delaware. One commitment: do right by every
      client, every time.
    </p>
  </div>
</section>

<section class="section">
  <div class="section__inner">
    <div class="about-lead">
      <div class="about-lead__photo">
        <img src="/images/team/adam.jpg" alt="Adam Druck, REALTOR® and Team Owner of the Adam Druck Group at Coldwell Banker Realty" />
      </div>
      <div class="about-lead__body">
        <p class="eyebrow">Meet Adam</p>
        <h2>From the family workshop to the closing table.</h2>
        <p>
          Adam Druck is a York County native and the fourth generation of one of
          the area's oldest family businesses &mdash;
          <strong>Ben Druck Door Company</strong>.
          Growing up around blueprints, framing, and finish work gave him something
          most agents simply don't have: an instinct for what a house actually <em>is</em>
          &mdash; bones, systems, problems, and potential.
        </p>
        <p>
          He brought that instinct into real estate and has since closed
          <strong>200+ transactions</strong> across Pennsylvania, Maryland, and Delaware.
          He works with first-time buyers navigating their first inspection, sellers
          who deserve a market-beating result, and investors who need an agent who
          can underwrite a project in their head while standing in the basement.
        </p>
        <p>
          Adam is a licensed REALTOR® in <strong>Pennsylvania, Maryland, and Delaware</strong>
          at Coldwell Banker Realty, Team Owner of the Adam Druck Group, and a
          member of NAR, PAR, and RAYAC.
        </p>
        <a href="/#contact" class="btn btn--primary">Work With Adam</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="section__inner">
    <div class="section__head" style="text-align: center; margin: 0 auto 3.5rem;">
      <p class="eyebrow">Our Values</p>
      <h2 class="section-title">Why clients come back &mdash; <span class="italic">and send their friends.</span></h2>
    </div>
    <div class="values">
      <div class="value">
        <span class="value__marker">01</span>
        <h3>Honest Counsel</h3>
        <p>If a property doesn't make sense for you, we'll tell you. Our long game is your trust — not this transaction.</p>
      </div>
      <div class="value">
        <span class="value__marker">02</span>
        <h3>Fast Response</h3>
        <p>Calls, texts, and emails answered within the hour — evenings and weekends included, when the market moves.</p>
      </div>
      <div class="value">
        <span class="value__marker">03</span>
        <h3>Local Depth</h3>
        <p>Which streets flood, which schools are turning, which builders cut corners — the information you cannot Google.</p>
      </div>
      <div class="value">
        <span class="value__marker">04</span>
        <h3>Real Marketing</h3>
        <p>Professional photo, video, drone, social, and targeted paid campaigns on every listing — not just an MLS upload.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="section__inner" style="text-align: center; max-width: 680px;">
    <p class="eyebrow">The Full Team</p>
    <h2 class="section-title">A full bench. <span class="italic">Built around you.</span></h2>
    <p style="color: var(--slate); font-size: 1.1rem; line-height: 1.65; margin: 1rem 0 2.5rem;">
      Real estate touches dozens of specialists — lenders, inspectors, title officers, attorneys,
      contractors, stagers, photographers. Our team orchestrates all of them so you don't have to.
    </p>
    <a href="/#team" class="btn btn--primary">Meet the Team</a>
  </div>
</section>
"""

pages = [
    ('buy.html',         'Buy a Home in York County, PA | Adam Druck Group',           'Expert buyer representation across York County, PA and tri-state MD/DE. First-time buyers, luxury, relocation, and new construction.', 'buy.html',         buy_body),
    ('sell.html',        'Sell Your Home in York County | Adam Druck Group',           'Top-tier listing marketing and pricing strategy from the Adam Druck Group at Coldwell Banker Realty. Get a complimentary home valuation.', 'sell.html',        sell_body),
    ('invest.html',      'Real Estate Investment Services | Adam Druck Group',         'York County investor specialist: flips, BRRRR, buy-and-hold, and 1031 strategy. Off-market deal flow, underwriting, and contractor network.', 'invest.html',      invest_body),
    ('communities.html', 'Communities We Serve: PA, MD & DE | Adam Druck Group',       'York County communities and tri-state neighborhoods — Spring Garden, Dover, Dallastown, Aberdeen, Bel Air, and more.',               'communities.html', communities_body),
    ('insights.html',    'Market Insights & Reports | Adam Druck Group',               'York County market reports, investor playbooks, and buyer/seller guides from the Adam Druck Group at Coldwell Banker Realty.',       'insights.html',    insights_body),
    ('about.html',       'About Adam Druck & the Adam Druck Group | Coldwell Banker',  'Four generations of York County roots. 200+ transactions. Licensed in PA, MD, DE. Meet Adam Druck and the Adam Druck Group team.',    'about.html',       about_body),
]

for slug, title, desc, canonical, body in pages:
    html = shell(title, desc, canonical, body)
    with open(os.path.join(OUT, slug), 'w') as f:
        f.write(html)
    print(f'✓ {slug} ({len(html):,} bytes)')

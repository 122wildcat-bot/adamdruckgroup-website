#!/usr/bin/env python3
"""Build the /review.html review-hub page."""
import os, importlib.util

HERE = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location("shell_mod", os.path.join(HERE, "_page-shell.py"))
shell_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(shell_mod)
shell = shell_mod.shell

BODY = """
<section class="page-lead">
  <div class="page-lead__inner">
    <p class="eyebrow page-lead__eyebrow">Thank You</p>
    <h1 class="page-lead__title">
      Share your experience. <span class="italic">In one click.</span>
    </h1>
    <p class="page-lead__lede">
      If we helped you buy, sell, or invest, a short review means the world to us —
      and to the next person deciding who to trust with their move. Pick the platform
      you use most. It should take about sixty seconds.
    </p>
  </div>
</section>

<section class="section">
  <div class="section__inner">
    <div class="review-grid" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:1.25rem; max-width:1000px; margin:0 auto;">

      <a href="https://g.page/r/YOUR_GOOGLE_PLACE_ID/review" target="_blank" rel="noopener" class="review-card" style="display:block; padding:1.75rem; background:#fff; border:1px solid #E5E7EB; border-radius:14px; text-decoration:none; color:inherit; transition:transform 0.15s ease, box-shadow 0.15s ease;">
        <p style="font-family:'Fraunces', serif; font-size:1.35rem; font-weight:500; margin:0 0 0.35rem; color:#012169;">Google</p>
        <p style="font-size:0.9rem; color:#64748b; margin:0 0 1rem;">Most helpful for local search</p>
        <p style="font-size:0.95rem; color:#0f172a; margin:0;">Leave a Google review →</p>
      </a>

      <a href="https://www.zillow.com/profile/adruck6/#reviews" target="_blank" rel="noopener" class="review-card" style="display:block; padding:1.75rem; background:#fff; border:1px solid #E5E7EB; border-radius:14px; text-decoration:none; color:inherit; transition:transform 0.15s ease, box-shadow 0.15s ease;">
        <p style="font-family:'Fraunces', serif; font-size:1.35rem; font-weight:500; margin:0 0 0.35rem; color:#012169;">Zillow</p>
        <p style="font-size:0.9rem; color:#64748b; margin:0 0 1rem;">Best if you searched homes on Zillow</p>
        <p style="font-size:0.95rem; color:#0f172a; margin:0;">Leave a Zillow review →</p>
      </a>

      <a href="https://www.realtor.com/realestateagents/62294176ff484fb0381df987" target="_blank" rel="noopener" class="review-card" style="display:block; padding:1.75rem; background:#fff; border:1px solid #E5E7EB; border-radius:14px; text-decoration:none; color:inherit; transition:transform 0.15s ease, box-shadow 0.15s ease;">
        <p style="font-family:'Fraunces', serif; font-size:1.35rem; font-weight:500; margin:0 0 0.35rem; color:#012169;">Realtor.com</p>
        <p style="font-size:0.9rem; color:#64748b; margin:0 0 1rem;">Best for future buyers researching agents</p>
        <p style="font-size:0.95rem; color:#0f172a; margin:0;">Leave a Realtor.com review →</p>
      </a>

      <a href="https://www.homes.com/real-estate-agents/adam-druck/l2j0s8e/" target="_blank" rel="noopener" class="review-card" style="display:block; padding:1.75rem; background:#fff; border:1px solid #E5E7EB; border-radius:14px; text-decoration:none; color:inherit; transition:transform 0.15s ease, box-shadow 0.15s ease;">
        <p style="font-family:'Fraunces', serif; font-size:1.35rem; font-weight:500; margin:0 0 0.35rem; color:#012169;">Homes.com</p>
        <p style="font-size:0.9rem; color:#64748b; margin:0 0 1rem;">Adds to our team's syndicated feed</p>
        <p style="font-size:0.95rem; color:#0f172a; margin:0;">Leave a Homes.com review →</p>
      </a>

      <a href="https://www.facebook.com/AdamDruckRealtor/reviews" target="_blank" rel="noopener" class="review-card" style="display:block; padding:1.75rem; background:#fff; border:1px solid #E5E7EB; border-radius:14px; text-decoration:none; color:inherit; transition:transform 0.15s ease, box-shadow 0.15s ease;">
        <p style="font-family:'Fraunces', serif; font-size:1.35rem; font-weight:500; margin:0 0 0.35rem; color:#012169;">Facebook</p>
        <p style="font-size:0.9rem; color:#64748b; margin:0 0 1rem;">Fastest if you're already on Facebook</p>
        <p style="font-size:0.95rem; color:#0f172a; margin:0;">Recommend us on Facebook →</p>
      </a>

      <a href="mailto:yourrealtoradamd@gmail.com?subject=My%20experience%20with%20the%20Adam%20Druck%20Group&body=Hi%20Adam%2C%0A%0AHere's%20a%20bit%20about%20my%20experience%20working%20with%20the%20Adam%20Druck%20Group%3A%0A%0A" class="review-card" style="display:block; padding:1.75rem; background:#012169; border:1px solid #012169; border-radius:14px; text-decoration:none; color:#fff; transition:transform 0.15s ease, box-shadow 0.15s ease;">
        <p style="font-family:'Fraunces', serif; font-size:1.35rem; font-weight:500; margin:0 0 0.35rem; color:#fff;">Email Adam Directly</p>
        <p style="font-size:0.9rem; color:#c7d6ee; margin:0 0 1rem;">Prefer to send privately? Just email.</p>
        <p style="font-size:0.95rem; color:#fff; margin:0;">Open a new email →</p>
      </a>

    </div>

    <p style="text-align:center; margin-top:3rem; font-size:0.95rem; color:#64748b; max-width:60ch; margin-left:auto; margin-right:auto;">
      Thank you for taking the time. Every review helps a future York County
      buyer or seller find real help \u2014 and it never goes unnoticed on our end.
    </p>
  </div>
</section>
"""

TITLE = "Leave a Review | Adam Druck Group"
DESC = "Share your experience with the Adam Druck Group. Leave a review on Google, Zillow, Realtor.com, Homes.com, or Facebook — it takes about a minute and helps the next York County buyer or seller."

html = shell(TITLE, DESC, "review.html", BODY)
with open(os.path.join(HERE, "review.html"), "w", encoding="utf-8") as f:
    f.write(html)
print(f"\u2713 review.html ({len(html)} bytes)")

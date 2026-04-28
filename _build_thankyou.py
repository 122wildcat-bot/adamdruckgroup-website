#!/usr/bin/env python3
"""Generate the post-submission thank-you page."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from importlib import import_module
shell = import_module('_page-shell').shell

body = """
<section class=\"page-lead\">
  <div class=\"page-lead__inner\">
    <p class=\"page-lead__eyebrow\">Thank You</p>
    <h1 class=\"page-lead__title\">Message <span class=\"italic\">received.</span></h1>
    <p class=\"page-lead__lede\">
      Thanks for reaching out. Adam will review your inquiry personally and get back to you
      within one business day \u2014 often much sooner. If something is time-sensitive, feel free
      to call directly at <a href=\"tel:+17174872579\">(717) 487-2579</a>.
    </p>
    <div class=\"page-lead__cta\">
      <a href=\"/\" class=\"btn btn--primary\">Back to Home</a>
      <a href=\"/communities.html\" class=\"btn btn--ghost\">Explore Communities</a>
    </div>
  </div>
</section>
"""

html = shell(
    title='Message Received | Adam Druck Group',
    description='Thanks for reaching out. Adam will be in touch within one business day.',
    canonical_slug='thank-you.html',
    body_html=body,
)

out_path = os.path.join(os.path.dirname(__file__), 'thank-you.html')
with open(out_path, 'w') as f:
    f.write(html)
print(f'\u2713 thank-you.html ({len(html):,} bytes)')

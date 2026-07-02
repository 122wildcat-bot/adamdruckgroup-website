#!/usr/bin/env python3
"""Generate the "My Home by ADG" client portal page (myhome.html).

A homeowner opens their private link — adamdruckgroup.com/myhome.html?t=TOKEN
— and this page fetches their data from the MVE portal API (CORS-allowed for
this origin): current estimated value + range, the value-over-time history
(drawn as an inline SVG, no chart library), optional equity, and a talk-to-
Adam CTA. Unknown/expired tokens get a friendly message. NOT linked from the
site nav — these links are private, handed out per client.

Distinct from my-home.html (the public "What's My Home Worth?" lead-magnet
form). This page is the logged-out client experience those leads graduate to.
"""
import os
import importlib.util

spec = importlib.util.spec_from_file_location(
    "shell_mod", os.path.join(os.path.dirname(__file__), "_page-shell.py")
)
shell_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(shell_mod)
shell = shell_mod.shell

PORTAL_API_BASE = "https://web-production-3c320.up.railway.app"

body = """
<section class="page-lead" id="mh-lead">
  <div class="page-lead__inner">
    <p class="eyebrow page-lead__eyebrow">My Home by ADG</p>
    <h1 class="page-lead__title" id="mh-title">Loading your <span class="italic">home&rsquo;s story&hellip;</span></h1>
    <p class="page-lead__lede" id="mh-sub"></p>
  </div>
</section>

<section class="section" id="mh-error" style="display:none;">
  <div class="section__inner" style="max-width: 640px; text-align: center;">
    <h2 class="section-title">This link isn&rsquo;t <span class="italic">available.</span></h2>
    <p style="color: var(--slate); font-size: 1.05rem; margin: 1rem 0 2rem;">
      It may have been replaced with a newer one. Reach out and we&rsquo;ll send you a fresh link
      &mdash; or a brand-new valuation.
    </p>
    <a href="/home-value.html" class="btn btn--primary">Request a Free Valuation</a>
    <a href="tel:+17174872579" class="btn btn--ghost" style="margin-left:.5rem;">(717) 487-2579</a>
  </div>
</section>

<section class="section" id="mh-main" style="display:none;">
  <div class="section__inner" style="max-width: 860px;">

    <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 1.5rem;">
      <div style="background: var(--cb-blue); color: #fff; padding: 2.2rem; border-radius: 10px;">
        <p class="eyebrow" style="color: #9cc4f5;">Estimated value today</p>
        <p id="mh-value" style="font-family: var(--serif); font-size: 3rem; font-weight: 600; margin: .3rem 0 .4rem; letter-spacing: -0.01em;"></p>
        <p id="mh-range" style="margin: 0; opacity: .85; font-size: .95rem;"></p>
        <p id="mh-asof" style="margin: .8rem 0 0; opacity: .6; font-size: .8rem; text-transform: uppercase; letter-spacing: .12em;"></p>
      </div>
      <div id="mh-equity-card" style="background: var(--cream); padding: 2.2rem; border-radius: 10px; border-left: 3px solid var(--celestial); display:none;">
        <p class="eyebrow">Estimated equity</p>
        <p id="mh-equity" style="font-family: var(--serif); font-size: 3rem; font-weight: 600; margin: .3rem 0 .4rem; color: var(--cb-blue);"></p>
        <p id="mh-equity-note" style="margin: 0; color: var(--slate); font-size: .9rem;"></p>
      </div>
      <div id="mh-noequity-card" style="background: var(--cream); padding: 2.2rem; border-radius: 10px; display:none;">
        <p class="eyebrow">Curious about your equity?</p>
        <p style="color: var(--slate); margin: .5rem 0 0; font-size: 1rem; line-height: 1.6;">
          Tell us your rough loan balance and this page will track your equity over time, too.
        </p>
      </div>
    </div>

    <div style="background: #fff; border: 1px solid #e7e2d9; border-radius: 10px; padding: 2rem; margin-bottom: 1.5rem;">
      <p class="eyebrow">Value over time</p>
      <div id="mh-chart" style="margin-top: 1rem;"></div>
      <p id="mh-trend" style="margin: 1rem 0 0; color: var(--slate); font-size: .95rem;"></p>
    </div>

    <div style="background: var(--cream); padding: 2rem; border-radius: 10px; display: flex; gap: 1.5rem; align-items: center; flex-wrap: wrap;">
      <div style="flex: 1; min-width: 260px;">
        <p class="eyebrow">Your agent</p>
        <p style="font-family: var(--serif); font-size: 1.35rem; margin: .3rem 0 .2rem; color: var(--ink);" id="mh-agent-name"></p>
        <p style="margin: 0; color: var(--slate); font-size: .9rem;" id="mh-agent-team"></p>
      </div>
      <div style="display: flex; gap: .6rem; flex-wrap: wrap;">
        <a id="mh-call" class="btn btn--primary" href="tel:+17174872579">Talk to Adam</a>
        <a id="mh-email" class="btn btn--ghost" href="mailto:yourrealtoradamd@gmail.com?subject=My%20home%27s%20value">Email</a>
      </div>
    </div>

    <p style="margin: 2rem 0 0; color: var(--muted); font-size: .8rem; line-height: 1.6;">
      These figures are broker price estimates prepared by the Adam Druck Group from comparable
      sales and market data &mdash; not an appraisal. Values are opinions, change with the market,
      and shouldn&rsquo;t be the sole basis for financial decisions. Equal Housing Opportunity.
    </p>
  </div>
</section>

<script>
(async () => {
  const API_BASE = "__PORTAL_API_BASE__";
  const token = new URLSearchParams(location.search).get("t");
  const show = (id, on) => { document.getElementById(id).style.display = on ? "" : "none"; };
  const set = (id, text) => { document.getElementById(id).textContent = text; };
  const money = (n) => "$" + Math.round(n).toLocaleString("en-US");

  const fail = () => {
    set("mh-title", "Hmm.");
    document.getElementById("mh-title").innerHTML = 'We couldn\\u2019t open <span class="italic">that link.</span>';
    show("mh-error", true);
  };

  if (!token) return fail();
  let d;
  try {
    const r = await fetch(API_BASE + "/api/portal/" + encodeURIComponent(token));
    if (!r.ok) return fail();
    d = await r.json();
  } catch (e) { return fail(); }

  document.getElementById("mh-title").innerHTML =
    "Hi " + escHtml(d.homeowner_first_name) + ' \\u2014 here\\u2019s your <span class="italic">home\\u2019s story.</span>';
  set("mh-sub", d.address);

  set("mh-value", money(d.current.value));
  set("mh-range", "Likely range: " + money(d.current.low) + " \\u2013 " + money(d.current.high));
  set("mh-asof", d.current.as_of ? "As of " + d.current.as_of : "");

  if (d.equity) {
    set("mh-equity", money(d.equity.estimated_equity));
    set("mh-equity-note", "Estimated value minus your ~" + money(d.equity.loan_balance) + " loan balance.");
    show("mh-equity-card", true);
  } else {
    show("mh-noequity-card", true);
  }

  // Value-over-time: inline SVG polyline, no library.
  const hist = (d.history || []).filter((h) => h.value != null);
  if (hist.length >= 2) {
    const W = 760, H = 220, PX = 46, PY = 26;
    const vals = hist.map((h) => h.value);
    const min = Math.min(...vals), max = Math.max(...vals);
    const span = (max - min) || 1;
    const x = (i) => PX + (i * (W - 2 * PX)) / (hist.length - 1);
    const y = (v) => H - PY - ((v - min) * (H - 2 * PY)) / span;
    const pts = hist.map((h, i) => x(i) + "," + y(h.value)).join(" ");
    const dots = hist.map((h, i) =>
      '<circle cx="' + x(i) + '" cy="' + y(h.value) + '" r="4.5" fill="#012169"></circle>' +
      '<text x="' + x(i) + '" y="' + (y(h.value) - 12) + '" text-anchor="middle" font-size="12" fill="#012169" font-weight="600">' + money(h.value) + "</text>" +
      '<text x="' + x(i) + '" y="' + (H - 6) + '" text-anchor="middle" font-size="11" fill="#8a8378">' + escHtml(fmtDate(h.date)) + "</text>"
    ).join("");
    document.getElementById("mh-chart").innerHTML =
      '<svg viewBox="0 0 ' + W + " " + H + '" style="width:100%;height:auto;" role="img" aria-label="Home value over time">' +
      '<polyline points="' + pts + '" fill="none" stroke="#418FDE" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"></polyline>' +
      dots + "</svg>";
    const first = hist[0].value, last = hist[hist.length - 1].value;
    const diff = last - first;
    set("mh-trend",
      diff >= 0
        ? "Up " + money(diff) + " since " + fmtDate(hist[0].date) + " \\u2014 " + pct(diff, first) + " growth across " + hist.length + " valuations."
        : "Down " + money(-diff) + " since " + fmtDate(hist[0].date) + " \\u2014 markets move; let\\u2019s talk strategy.");
  } else {
    document.getElementById("mh-chart").innerHTML =
      '<p style="color: var(--slate); margin: 0;">Your value history starts here \\u2014 the chart appears after your next update.</p>';
  }

  set("mh-agent-name", d.agent.name + " \\u00b7 " + d.agent.title);
  set("mh-agent-team", d.agent.team);
  document.getElementById("mh-call").href = "tel:" + d.agent.phone.replace(/[^0-9+]/g, "");
  document.getElementById("mh-email").href = "mailto:" + d.agent.email + "?subject=" + encodeURIComponent("My home's value \\u2014 " + d.address);

  show("mh-main", true);

  function escHtml(v) {
    return String(v == null ? "" : v).replace(/[&<>"']/g, (c) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
    }[c]));
  }
  function fmtDate(iso) {
    if (!iso) return "";
    const [yr, mo] = iso.split("-");
    const names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
    return names[Number(mo) - 1] + " " + yr;
  }
  function pct(diff, base) {
    return base > 0 ? (100 * diff / base).toFixed(1) + "%" : "";
  }
})();
</script>
""".replace("__PORTAL_API_BASE__", PORTAL_API_BASE)


def main() -> None:
    html = shell(
        title="My Home by ADG | Adam Druck Group",
        description="Your home's current estimated value, trend over time, and equity — a private page from the Adam Druck Group at Coldwell Banker Realty.",
        canonical_slug="myhome.html",
        body_html=body,
        extra_head='<meta name="robots" content="noindex, nofollow" />',
    )
    out = os.path.join(os.path.dirname(__file__), "myhome.html")
    with open(out, "w") as f:
        f.write(html)
    print(f"✓ myhome.html ({len(html):,} bytes)")


if __name__ == "__main__":
    main()

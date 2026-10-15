// ==========================================================
// Adam Druck Group — interactive behaviors
// ==========================================================

// Scroll-triggered nav background (only on homepage with transparent hero nav)
const nav = document.getElementById('nav');
const isSubpage = document.body.classList.contains('subpage');
if (nav && !isSubpage) {
  const onScroll = () => {
    if (window.scrollY > 40) nav.classList.add('is-scrolled');
    else nav.classList.remove('is-scrolled');
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

// Mobile menu
const navToggle = document.getElementById('navToggle');
let mobileMenu = null;
function buildMobileMenu() {
  if (mobileMenu) return mobileMenu;
  mobileMenu = document.createElement('div');
  mobileMenu.className = 'mobile-menu';
  mobileMenu.innerHTML = `
    <nav aria-label="Mobile">
      <a href="/buy.html">Buy</a>
      <a href="/sell.html">Sell</a>
      <a href="/invest.html">Invest</a>
      <a href="/communities.html">Communities</a>
      <a href="/home-value.html">Home Value</a>
      <a href="/insights.html">Insights</a>
      <a href="/about.html">About</a>
      <a href="/contact.html">Contact</a>
      <a href="https://adamdruck.sites.cbmoxi.com/search" target="_blank" rel="noopener">Search Homes</a>
    </nav>
  `;
  document.body.appendChild(mobileMenu);
  mobileMenu.addEventListener('click', (e) => {
    if (e.target.tagName === 'A' || e.target === mobileMenu) {
      mobileMenu.classList.remove('is-open');
      navToggle.setAttribute('aria-expanded', 'false');
    }
  });
  return mobileMenu;
}
navToggle?.addEventListener('click', () => {
  const menu = buildMobileMenu();
  const isOpen = menu.classList.toggle('is-open');
  navToggle.setAttribute('aria-expanded', String(isOpen));
});

// Current year in footer (may not exist on every page)
const _yearEl = document.getElementById('year');
if (_yearEl) _yearEl.textContent = new Date().getFullYear();

// Contact form is handled natively by Netlify Forms via POST + redirect to /thank-you.html.
// No JS submit handler needed.

// Smooth-scroll for internal anchors (in case smooth behavior is off)
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener('click', (e) => {
    const target = document.querySelector(link.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// ==========================================================
// Rotating testimonials — verified reviews from Zillow & Homes.com
// ==========================================================
const TESTIMONIALS = [
  {
    quote: "Adam is by far the best realtor I have ever worked with. His knowledge of home construction and eye for potential problems is invaluable.",
    name: "K. Garvin", meta: "York, PA — Buyer", agent: "Adam Druck", source: "Zillow"
  },
  {
    quote: "Adam was so helpful and professional during the sale of our home. He priced our home so we received multiple offers within a couple days — the offer we accepted was over our list price and we settled within 30 days.",
    name: "Townhouse Seller", meta: "York, PA — Seller", agent: "Adam Druck", source: "Zillow"
  },
  {
    quote: "As first-time homebuyers, we couldn’t have asked for a better experience than working with Zach. He was incredibly kind, patient, and supportive throughout the entire process.",
    name: "Kelsey Groff", meta: "First-Time Buyer", agent: "Zachery Keller", source: "Zillow"
  },
  {
    quote: "Trevor went above and beyond to get the deal done. It didn’t matter what time of day it was — he was always extremely responsive. He sold our house in a day and helped us buy our dream home.",
    name: "Verified Client", meta: "Dover, PA — Buyer & Seller", agent: "Trevor Stuck", source: "Zillow"
  },
  {
    quote: "I was a first-time home buyer with some nerves going into the process. Adam took me under his wing and guided me throughout the entire process.",
    name: "S. Eaton", meta: "York, PA — First-Time Buyer", agent: "Adam Druck", source: "Zillow"
  },
  {
    quote: "Could not recommend Zach enough. My wife and I got married and settled on this property within 5 days. Zach went above and beyond for us.",
    name: "Luke O.", meta: "Central PA — Buyer", agent: "Zachery Keller", source: "Zillow"
  },
  {
    quote: "We were extremely pleased with Amanda’s expertise in selling my mother’s home. She was always available to answer questions and give sound advice.",
    name: "Verified Client", meta: "York, PA — Seller", agent: "Amanda Eisenhart", source: "Zillow"
  },
  {
    quote: "Adam was very attentive to the transaction, specifically because I purchased the home from California. I would recommend him in the future.",
    name: "Out-of-State Buyer", meta: "York, PA — Relocation", agent: "Adam Druck", source: "Zillow"
  },
  {
    quote: "Zachery did an outstanding job helping us sell our house in MD and buy a house in PA. He listened to our needs and was always available.",
    name: "Phil Byle", meta: "MD → PA — Relocation", agent: "Zachery Keller", source: "Zillow"
  },
  {
    quote: "Amanda is very organized and patient. She returns calls and messages in a timely manner — great to work with and has an eye for layout and design.",
    name: "Verified Client", meta: "York, PA — Buyer", agent: "Amanda Eisenhart", source: "Zillow"
  }
];

(function initTestimonials() {
  const track = document.getElementById('testimonials-track');
  const controls = document.querySelector('.testimonials__controls');
  if (!track || !controls) return;

  // Shuffle so the order feels fresh on each visit (Fisher–Yates)
  const deck = TESTIMONIALS.slice();
  for (let i = deck.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [deck[i], deck[j]] = [deck[j], deck[i]];
  }

  // Render
  deck.forEach((t, i) => {
    const slide = document.createElement('figure');
    slide.className = 'testimonial' + (i === 0 ? ' is-active' : '');
    slide.innerHTML = `
      <blockquote>“${t.quote}”</blockquote>
      <figcaption class="testimonial__cite">
        — ${t.name}, ${t.meta}<br>
        On working with <strong>${t.agent}</strong>
      </figcaption>
    `;
    track.appendChild(slide);

    const dot = document.createElement('button');
    dot.type = 'button';
    dot.className = 'testimonials__dot' + (i === 0 ? ' is-active' : '');
    dot.setAttribute('role', 'tab');
    dot.setAttribute('aria-label', `Show review ${i + 1} of ${deck.length}`);
    dot.dataset.idx = String(i);
    controls.appendChild(dot);
  });

  const slides = Array.from(track.querySelectorAll('.testimonial'));
  const dots = Array.from(controls.querySelectorAll('.testimonials__dot'));
  let idx = 0;
  let timer = null;
  const INTERVAL = 6500;

  function show(n) {
    idx = (n + slides.length) % slides.length;
    slides.forEach((s, i) => s.classList.toggle('is-active', i === idx));
    dots.forEach((d, i) => {
      d.classList.toggle('is-active', i === idx);
      d.setAttribute('aria-selected', i === idx ? 'true' : 'false');
    });
  }
  function next() { show(idx + 1); }
  function start() { stop(); timer = setInterval(next, INTERVAL); }
  function stop()  { if (timer) { clearInterval(timer); timer = null; } }

  dots.forEach(d => d.addEventListener('click', () => {
    show(parseInt(d.dataset.idx, 10));
    start(); // restart the cycle on manual nav
  }));

  // Pause on hover / focus
  const section = document.getElementById('testimonials');
  section.addEventListener('mouseenter', stop);
  section.addEventListener('mouseleave', start);
  section.addEventListener('focusin', stop);
  section.addEventListener('focusout', start);

  // Only auto-cycle when visible — saves battery on long pages
  const vis = new IntersectionObserver((entries) => {
    entries.forEach(e => e.isIntersecting ? start() : stop());
  }, { threshold: 0.2 });
  vis.observe(section);

  // Respect user’s motion preference — still rotate, but the CSS transition is shorter
  start();
})();

// Subtle reveal on scroll (cheap, no library)
const revealEls = document.querySelectorAll('.section-title, .agent, .area-card, .stat, .editorial__image, .editorial__caption, .hero__title');
const io = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('is-in');
      io.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });
revealEls.forEach(el => io.observe(el));

// ── CRM lead beacon ──────────────────────────────────────────────────────────
// Every FormSubmit form also posts a copy of the lead to the ADG CRM, where it
// becomes a contact + follow-up task automatically (POST /api/web-lead).
// fetch({ keepalive }) lets the request finish while the form's own submission
// navigates away to FormSubmit. Failures are silent by design — the email
// submission remains the source of truth.
(() => {
  const CRM_LEAD_URL = 'https://adg-crm-production.up.railway.app/api/web-lead';
  document.querySelectorAll('form[action*="formsubmit.co"]').forEach((form) => {
    form.addEventListener('submit', () => {
      try {
        const payload = { page: location.pathname || '/' };
        new FormData(form).forEach((value, key) => {
          if (typeof value !== 'string') return;
          if (key.startsWith('_') && key !== '_honey') return; // FormSubmit config fields
          payload[key] = value;
        });
        // text/plain is CORS-safelisted: no preflight round-trip, so the
        // request can't lose a race against the form's navigation to
        // FormSubmit. sendBeacon is queued by the browser itself and
        // survives the page unload; keepalive fetch is the fallback.
        const body = JSON.stringify(payload);
        const sent = navigator.sendBeacon
          && navigator.sendBeacon(CRM_LEAD_URL, new Blob([body], { type: 'text/plain;charset=UTF-8' }));
        if (!sent) {
          fetch(CRM_LEAD_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'text/plain;charset=UTF-8' },
            body,
            keepalive: true,
            mode: 'cors',
          }).catch(() => {});
        }
      } catch (e) { /* never block the real submit */ }
    });
  });
})();

// ==========================================================
// Listings — one listings.json, split by status. No IDX feed.
// ==========================================================
(() => {
  const grids = [...document.querySelectorAll('[data-group]')];
  if (!grids.length) return;

  const SEARCH_URL = 'https://adamdruck.sites.cbmoxi.com/search';
  const BROKERAGE = 'Coldwell Banker Realty';
  const money = new Intl.NumberFormat('en-US', {
    style: 'currency', currency: 'USD', maximumFractionDigits: 0
  });
  const num = new Intl.NumberFormat('en-US');

  const groupOf = (listing) => {
    const status = String(listing.status || '').toLowerCase();
    if (status.includes('sold')) return 'sold';
    if (status.includes('pending') || status.includes('contract')) return 'pending';
    return 'newest';
  };

  const statusClass = (status) => {
    const statusText = String(status || '').toLowerCase();
    if (statusText.includes('sold')) return 'is-sold';
    if (statusText.includes('coming')) return 'is-soon';
    if (statusText.includes('contract') || statusText.includes('pending')) return 'is-pending';
    if (statusText.includes('new')) return 'is-new';
    return 'is-active';
  };

  const safeUrl = (url) => {
    try {
      const parsed = new URL(url, window.location.origin);
      if (parsed.protocol === 'http:' || parsed.protocol === 'https:') return parsed.href;
    } catch (e) { /* fall through */ }
    return '';
  };

  const safeImage = (src) => {
    if (typeof src !== 'string') return '';
    const value = src.trim();
    if (!value || /^\s*javascript:/i.test(value) || value.startsWith('//')) return '';
    return value;
  };

  const canShowPhoto = (listing) => {
    if (String(listing.side || '').toLowerCase() === 'buyer') return false;
    if (listing.photoAllowed === false) return false;
    return !!safeImage(listing.image);
  };

  const formatDate = (iso) => {
    if (typeof iso !== 'string' || !iso) return '';
    const parts = iso.split('-').map(Number);
    if (parts.length < 3 || parts.some((part) => !part)) return '';
    return new Date(parts[0], parts[1] - 1, parts[2]).toLocaleDateString('en-US', {
      month: 'short', day: 'numeric', year: 'numeric'
    });
  };

  const sideLabel = (listing) => {
    const side = String(listing.side || '').toLowerCase();
    if (side === 'buyer') return 'Represented the Buyer';
    if (side === 'listing' || side === 'both') return 'Listed by Adam Druck Group';
    return '';
  };

  const sortKey = (listing, group) => {
    if (group === 'sold') return String(listing.closeDate || '');
    if (group === 'pending') return String(listing.pendingDate || listing.listed || '');
    return String(listing.listed || '');
  };

  const bathsLabel = (listing) => {
    const full = Number(listing.bathsFull ?? listing.baths ?? 0);
    const half = Number(listing.bathsHalf ?? 0);
    const total = full + half * 0.5;
    return Number.isInteger(total) ? String(total) : String(total);
  };

  const el = (tag, className, text) => {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = text;
    return node;
  };

  const placeholder = () => {
    const wrap = el('div', 'listing-card__placeholder');
    wrap.innerHTML = '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M6 20 L24 7 L42 20 V40 H6 Z"/><path d="M19 40 V28 H29 V40"/></svg>';
    wrap.appendChild(el('span', null, 'Photo coming soon'));
    return wrap;
  };

  const card = (listing) => {
    const sold = groupOf(listing) === 'sold';
    const showPhoto = canShowPhoto(listing);
    const textOnly = sold && !showPhoto;
    const article = el('article', textOnly ? 'listing-card listing-card--text' : 'listing-card');
    const href = safeUrl(listing.url || '');
    const linked = Boolean(href) && (!sold || /\/listing\//.test(href));
    const destination = linked ? href : (sold ? '' : SEARCH_URL);
    const shell = document.createElement(destination ? 'a' : 'div');
    shell.className = 'listing-card__link';
    if (destination) {
      shell.href = destination;
      shell.target = '_blank';
      shell.rel = 'noopener';
    }

    const street = listing.address || 'Listing';
    const place = [listing.city, listing.state].filter(Boolean).join(', ');
    const placeLine = [place, listing.zip].filter(Boolean).join(' ');

    if (!textOnly) {
      const media = el('div', 'listing-card__media');
      if (showPhoto) {
        const img = document.createElement('img');
        img.src = safeImage(listing.image);
        img.alt = listing.imageAlt || `Photo of ${street}`;
        img.width = 1280;
        img.height = 854;
        img.loading = 'lazy';
        img.decoding = 'async';
        img.addEventListener('error', () => {
          img.remove();
          media.appendChild(placeholder());
        });
        media.appendChild(img);
      } else {
        media.appendChild(placeholder());
      }
      media.appendChild(el('span', `listing-card__status ${statusClass(listing.status)}`, listing.status || 'Listing'));
      shell.appendChild(media);
    }

    const body = el('div', 'listing-card__body');
    if (textOnly) {
      const meta = el('div', 'listing-card__meta');
      meta.appendChild(el('span', `listing-card__status ${statusClass(listing.status)}`, listing.status || 'Sold'));
      if (listing.propertyType) meta.appendChild(el('span', 'listing-card__type', listing.propertyType));
      body.appendChild(meta);
    }

    const amount = sold ? listing.soldPrice : listing.price;
    if (amount != null && amount !== '') {
      body.appendChild(el('p', 'listing-card__price', money.format(Number(amount))));
    }
    body.appendChild(el('h3', 'listing-card__address', street));
    if (placeLine) body.appendChild(el('p', 'listing-card__place', placeLine));
    if (sold && !textOnly && listing.propertyType) {
      body.appendChild(el('p', 'listing-card__type listing-card__type--inline', listing.propertyType));
    }

    const facts = [];
    if (listing.beds != null && listing.beds !== '') facts.push(`${listing.beds} bd`);
    if (listing.bathsFull != null || listing.bathsHalf != null) facts.push(`${bathsLabel(listing)} ba`);
    if (listing.sqft) facts.push(`${num.format(Number(listing.sqft))} sq ft`);
    if (facts.length) body.appendChild(el('p', 'listing-card__facts', facts.join(' · ')));

    if (sold && listing.closeDate) {
      body.appendChild(el('p', 'listing-card__closed', `Closed ${formatDate(listing.closeDate)}`));
    }
    if (sold) {
      const label = sideLabel(listing);
      if (label) body.appendChild(el('p', 'listing-card__side', label));
    }

    body.appendChild(el('p', 'listing-card__broker', String(listing.brokerage || BROKERAGE).trim() || BROKERAGE));
    if (listing.mls) body.appendChild(el('p', 'listing-card__mls', `MLS #${listing.mls}`));
    if (destination && !sold) {
      shell.appendChild(body);
      const onListingPage = /\/listing\//.test(destination);
      body.appendChild(el('p', 'listing-card__cta', onListingPage ? 'View listing' : 'Search listings'));
    } else {
      shell.appendChild(body);
    }

    article.appendChild(shell);
    return article;
  };

  const showMessage = (grid, text) => {
    grid.replaceChildren(el('p', 'listings__status', text));
  };

  fetch('/listings.json', { cache: 'no-cache' })
    .then((res) => {
      if (!res.ok) throw new Error(String(res.status));
      return res.json();
    })
    .then((data) => {
      const listings = Array.isArray(data.listings) ? data.listings : [];
      const grouped = { newest: [], pending: [], sold: [] };
      listings.forEach((listing) => {
        const group = groupOf(listing);
        (grouped[group] || grouped.newest).push(listing);
      });

      document.querySelectorAll('[data-listing-section]').forEach((section) => {
        const group = section.dataset.listingSection;
        const count = (grouped[group] || []).length;
        if ((group === 'pending' || group === 'sold') && count === 0) section.hidden = true;
      });

      grids.forEach((grid) => {
        const group = grid.dataset.group;
        let rows = (grouped[group] || []).slice();
        rows.sort((a, b) => sortKey(b, group).localeCompare(sortKey(a, group)));
        if (group === 'sold' && grid.dataset.limit !== 'all') {
          const limit = Number(data.homepageSoldLimit) || 6;
          rows = rows.slice(0, limit);
        }
        if (!rows.length) {
          showMessage(grid, group === 'newest' ? 'No listings to show right now.' : 'Nothing to show yet.');
          return;
        }
        grid.replaceChildren(...rows.map(card));
      });

      const summary = document.getElementById('sold-summary');
      if (summary && grouped.sold.length) {
        const dates = grouped.sold.map((row) => row.closeDate).filter(Boolean).sort();
        const span = dates.length
          ? `, ${formatDate(dates[0])} through ${formatDate(dates[dates.length - 1])}`
          : '';
        summary.textContent = `${grouped.sold.length} closings${span}. Newest first.`;
      }
    })
    .catch(() => {
      grids.forEach((grid) => showMessage(grid, 'Listings could not be loaded.'));
    });
})();


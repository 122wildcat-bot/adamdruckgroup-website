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

// Contact form — front-end stub (Coldwell Banker / CRM integration to be wired by IT)
function handleSubmit(e) {
  e.preventDefault();
  const form = e.target;
  const formData = Object.fromEntries(new FormData(form));
  // For now, open a pre-filled email. Replace with API endpoint when ready.
  const subject = encodeURIComponent(`Website Inquiry — ${formData.interest || 'General'}`);
  const body = encodeURIComponent(
    `Name: ${formData.name || ''}\n` +
    `Email: ${formData.email || ''}\n` +
    `Phone: ${formData.phone || ''}\n` +
    `Interest: ${formData.interest || ''}\n\n` +
    `Message:\n${formData.message || ''}`
  );
  window.location.href = `mailto:yourrealtoradamd@gmail.com?subject=${subject}&body=${body}`;

  // Visual feedback
  const btn = form.querySelector('button[type="submit"]');
  const original = btn.textContent;
  btn.textContent = 'Opening Email...';
  btn.disabled = true;
  setTimeout(() => {
    btn.textContent = 'Message Sent ✓';
    setTimeout(() => {
      form.reset();
      btn.textContent = original;
      btn.disabled = false;
    }, 2500);
  }, 600);
}

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

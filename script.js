// ==========================================================
// Adam Druck Group — interactive behaviors
// ==========================================================

// Scroll-triggered nav background
const nav = document.getElementById('nav');
const onScroll = () => {
  if (window.scrollY > 40) nav.classList.add('is-scrolled');
  else nav.classList.remove('is-scrolled');
};
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

// Mobile menu
const navToggle = document.getElementById('navToggle');
let mobileMenu = null;
function buildMobileMenu() {
  if (mobileMenu) return mobileMenu;
  mobileMenu = document.createElement('div');
  mobileMenu.className = 'mobile-menu';
  mobileMenu.innerHTML = `
    <nav aria-label="Mobile">
      <a href="#about">About</a>
      <a href="#team">Team</a>
      <a href="#areas">Areas</a>
      <a href="#contact">Contact</a>
      <a href="https://www.coldwellbanker.com/pa/york/agents/adam-druck-team/tid-P01700000000031wusBTjt7u1DgtW12T3cpXAJ4X" target="_blank" rel="noopener">Search Homes</a>
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

// Current year in footer
document.getElementById('year').textContent = new Date().getFullYear();

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
  window.location.href = `mailto:adam.druck@cbrealty.com?subject=${subject}&body=${body}`;

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

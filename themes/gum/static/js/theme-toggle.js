(function () {
  const html = document.documentElement;
  const toggleButton = document.getElementById('theme-toggle');
  const darkCss = document.getElementById('pygment-dark-link');
  const lightCss = document.querySelector('link[href*="pygment.css"]:not([href*="dark"])');
  const navToggle = document.querySelector('.nav-toggle');
  const nav = document.getElementById('site-nav');
  const progress = document.querySelector('.progress');

  function applyTheme(theme) {
    if (theme === 'dark') {
      html.setAttribute('data-theme', 'dark');
      if (darkCss) darkCss.disabled = false;
      if (lightCss && darkCss) lightCss.media = 'not all';
      if (toggleButton) toggleButton.setAttribute('aria-label', 'Switch to light theme');
    } else {
      html.removeAttribute('data-theme');
      if (darkCss) darkCss.disabled = true;
      if (lightCss) lightCss.media = 'all';
      if (toggleButton) toggleButton.setAttribute('aria-label', 'Switch to dark theme');
    }
    try { localStorage.setItem('theme', theme); } catch (e) { /* ignored */ }
  }

  function getInitialTheme() {
    try {
      const stored = localStorage.getItem('theme');
      if (stored === 'dark' || stored === 'light') return stored;
    } catch (e) { /* ignored */ }
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) return 'dark';
    return 'light';
  }

  if (toggleButton) {
    toggleButton.addEventListener('click', function () {
      applyTheme(html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
    });
  }
  applyTheme(getInitialTheme());

  if (navToggle && nav) {
    navToggle.addEventListener('click', function () {
      const open = nav.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') {
        nav.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  function updateProgress() {
    if (!progress) return;
    const body = document.querySelector('.prose-body');
    if (!body) { progress.style.width = '0'; return; }
    const start = body.offsetTop;
    const height = Math.max(1, body.offsetHeight - window.innerHeight);
    const pct = Math.max(0, Math.min(1, (window.scrollY - start + 200) / height));
    progress.style.width = (pct * 100).toFixed(2) + '%';
  }
  window.addEventListener('scroll', updateProgress, { passive: true });
  window.addEventListener('resize', updateProgress);
  updateProgress();
})();

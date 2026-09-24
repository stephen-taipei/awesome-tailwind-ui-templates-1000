/* Kept small and synchronous to avoid a flash of the wrong appearance. */
(() => {
  let mode = 'light';
  try { mode = localStorage.getItem('atlas-appearance') || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'); } catch {}
  document.documentElement.dataset.appearance = mode === 'dark' ? 'dark' : 'light';
  const ready = () => {
    const button = document.getElementById('theme-toggle');
    if (!button) return;
    const sync = () => {
      const dark = document.documentElement.dataset.appearance === 'dark';
      button.setAttribute('aria-pressed', String(dark));
      button.setAttribute('aria-label', `Use ${dark ? 'light' : 'dark'} appearance`);
    };
    button.addEventListener('click', () => {
      const value = document.documentElement.dataset.appearance === 'dark' ? 'light' : 'dark';
      document.documentElement.dataset.appearance = value;
      try { localStorage.setItem('atlas-appearance', value); } catch {}
      sync();
    });
    sync();
  };
  document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', ready, { once: true }) : ready();
})();

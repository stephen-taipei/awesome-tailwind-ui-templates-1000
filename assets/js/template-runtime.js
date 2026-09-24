/* Shared demo safeguards; does not replace template-specific business interactions. */
(() => {
  'use strict';
  document.addEventListener('submit', (event) => {
    const form = event.target;
    if (!(form instanceof HTMLFormElement) || event.defaultPrevented) return;
    const action = form.getAttribute('action');
    if (action && action !== '#') return;
    event.preventDefault();
    let status = form.querySelector('[data-demo-status]');
    if (!status) {
      status = document.createElement('p');
      status.dataset.demoStatus = '';
      status.setAttribute('role', 'status');
      status.style.cssText = 'margin-top:1rem;padding:.75rem;border:1px solid currentColor;border-radius:.5rem';
      form.append(status);
    }
    status.textContent = 'Demo only — no information was submitted. Connect your own backend before use.';
  });
  for (const button of document.querySelectorAll('[aria-controls][aria-expanded]')) {
    const region = document.getElementById(button.getAttribute('aria-controls'));
    if (!region?.classList.contains('mobile-menu')) continue;
    const sync = () => { region.inert = button.getAttribute('aria-expanded') !== 'true'; };
    sync();
    new MutationObserver(sync).observe(button, { attributes: true, attributeFilter: ['aria-expanded'] });
    region.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') button.focus();
    });
  }
})();

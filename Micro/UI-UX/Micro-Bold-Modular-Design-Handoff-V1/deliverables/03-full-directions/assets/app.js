(function () {
  'use strict';
  var params = new URLSearchParams(location.search);
  if (params.get('scale') === 'text200') document.documentElement.classList.add('text200');
  if (params.get('static') === '1') document.documentElement.classList.add('staticnav');
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Sale form: immediate press feedback -> saving state (prevents double submit) -> success.
  var form = document.querySelector('form.sale-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = form.querySelector('.btn-primary[type="submit"]');
      if (!btn || btn.dataset.busy) return;
      btn.dataset.busy = '1';
      btn.setAttribute('aria-busy', 'true');
      btn.textContent = 'جارٍ التسجيل…';
      setTimeout(function () { location.href = 'sale-success.html'; }, reduced ? 50 : 600);
    });
  }

  // Sheet/dialog close affordances.
  document.querySelectorAll('[data-close-sheet]').forEach(function (el) {
    el.addEventListener('click', function () { location.href = 'home-positive.html'; });
  });
  var backdrop = document.querySelector('.sheet-backdrop, .menu-backdrop');
  if (backdrop) {
    backdrop.addEventListener('click', function (e) {
      if (e.target === backdrop) location.href = 'home-positive.html';
    });
  }

  // Choice chips: visible selected state with text + container (never color alone).
  document.querySelectorAll('.choice-row').forEach(function (row) {
    row.querySelectorAll('.choice').forEach(function (ch) {
      ch.addEventListener('click', function () {
        row.querySelectorAll('.choice').forEach(function (c) {
          c.setAttribute('aria-pressed', 'false');
          delete c.dataset.selected;
        });
        ch.setAttribute('aria-pressed', 'true');
        ch.dataset.selected = 'true';
      });
    });
  });
})();
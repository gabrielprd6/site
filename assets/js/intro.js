/* =============================================================================
   Croisia — rideau d'intro (loader)
   Compteur 0 → 100 %, barre qui se remplit, puis le rideau se lève sur le hero.
   Indépendant de GSAP. Respecte prefers-reduced-motion. Filets de sécurité pour
   ne jamais rester bloqué sur le loader.
   ========================================================================== */
(function () {
  'use strict';

  var loader = document.getElementById('loader');
  if (!loader) return;

  var num  = document.getElementById('loader-num');
  var bar  = document.getElementById('loader-bar');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var body = document.body;

  var done = false;
  function finish() {
    if (done) return;
    done = true;
    if (num) num.textContent = '100';
    if (bar) bar.style.transform = 'scaleX(1)';
    loader.classList.add('is-done');
    body.classList.remove('is-loading');
    // Retire le rideau du DOM une fois l'animation de levée terminée.
    var remove = function () { loader.setAttribute('hidden', ''); };
    if (reduce) remove();
    else window.setTimeout(remove, 950);
    // Signale au reste (main.js/motion.js) que l'intro est finie.
    document.documentElement.classList.add('intro-done');
    window.dispatchEvent(new CustomEvent('croisia:intro-done'));
  }

  if (reduce) { finish(); return; }

  body.classList.add('is-loading');

  // Compteur animé (easeOutCubic) sur ~1.1 s.
  var duration = 1100;
  var start = null;
  function frame(ts) {
    if (start === null) start = ts;
    var p = Math.min(1, (ts - start) / duration);
    var eased = 1 - Math.pow(1 - p, 3);
    if (num) num.textContent = String(Math.round(eased * 100));
    if (bar) bar.style.transform = 'scaleX(' + eased.toFixed(3) + ')';
    if (p < 1) {
      window.requestAnimationFrame(frame);
    } else {
      // Petite respiration avant de lever le rideau.
      window.setTimeout(finish, 220);
    }
  }
  window.requestAnimationFrame(frame);

  // Filets : on ne reste jamais coincé sur le loader.
  window.addEventListener('load', function () { window.setTimeout(finish, 400); });
  window.setTimeout(finish, 3000);
})();

/* =============================================================================
   Altiora — couche de motion « signature Apple » (additive, progressive)
   ---------------------------------------------------------------------------
   S'ajoute par-dessus main.js. Ne s'active QUE si GSAP + ScrollTrigger sont là
   et si l'utilisateur n'a pas demandé « moins d'animations ». Sinon, rien :
   main.js gère déjà les révélations, et le contenu reste entièrement visible.

   Principe (WWDC « Designing Fluid Interfaces ») : le mouvement part de la
   valeur à l'écran, suit le doigt/scroll en continu, et reste léger —
   uniquement transform / opacity (+ un flou ponctuel sur 3 visuels).
   ========================================================================== */
(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var gsap   = window.gsap;
  var ST     = window.ScrollTrigger;
  if (reduce || !gsap || !ST) return;

  gsap.registerPlugin(ST);

  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ------------------------------------------------ Hero : recul en profondeur */
  /* Pendant qu'on dépasse le hero, son contenu monte légèrement et s'estompe —
     l'effet « caméra qui recule » d'Apple. Le fond a déjà sa parallaxe (main.js). */
  function heroPush() {
    var hero  = $('.hero');
    var inner = $('.hero__inner');
    if (!hero || !inner) return;

    gsap.to(inner, {
      yPercent: -14, opacity: .28, ease: 'none',
      scrollTrigger: { trigger: hero, start: 'top top', end: 'bottom top', scrub: .6 }
    });
  }

  /* --------------------------------------- Services : le visuel se « résout » */
  /* Chaque visuel entre flou + agrandi + décalé, puis se pose net (échelle 1)
     au fil du scroll. C'est la révélation d'image des pages produit Apple. */
  function featureVisuals() {
    $$('.feature__visual').forEach(function (fig) {
      var img = $('img', fig);
      if (!img) return;

      /* transform seul (pas de filtre pendant le scroll : évite le jank) */
      gsap.fromTo(img,
        { scale: 1.12, yPercent: 6 },
        {
          scale: 1, yPercent: 0, ease: 'none',
          scrollTrigger: { trigger: fig, start: 'top 85%', end: 'top 42%', scrub: .6 }
        });
    });
  }

  /* ----------------------------- Services : les items de liste montent en cascade */
  function featureLists() {
    $$('.feature__list').forEach(function (ul) {
      var items = $$('li', ul);
      if (!items.length) return;

      gsap.fromTo(items,
        { opacity: 0, y: 16 },
        {
          opacity: 1, y: 0, duration: .6, ease: 'power3.out', stagger: .08,
          scrollTrigger: { trigger: ul, start: 'top 84%', once: true }
        });
    });
  }

  /* --------------------------------- Méthode : timeline qui se remplit + étapes */
  function steps() {
    var ol = $('[data-steps]');
    if (!ol) return;

    var fill = $('.steps__rail i', ol);
    if (fill) {
      gsap.fromTo(fill,
        { scaleX: 0 },
        {
          scaleX: 1, ease: 'none',
          scrollTrigger: { trigger: ol, start: 'top 78%', end: 'bottom 62%', scrub: .5 }
        });
    }

    // Chaque étape s'allume quand elle atteint le centre haut de l'écran,
    // et le reste (étape « franchie »), comme les timelines produit d'Apple.
    $$('.step', ol).forEach(function (li) {
      ST.create({
        trigger: li, start: 'top 70%',
        onEnter:     function () { li.classList.add('is-active'); },
        onEnterBack: function () { li.classList.add('is-active'); }
      });
    });
  }

  /* -------------------------------------- Résultats : les valeurs montent d'un cran */
  function stats() {
    $$('.stat__value').forEach(function (v) {
      var card = v.closest('.stat') || v;
      gsap.fromTo(v,
        { yPercent: 32 },
        {
          yPercent: 0, ease: 'expo.out', duration: 1.1,
          scrollTrigger: { trigger: card, start: 'top 82%', once: true }
        });
    });
  }

  /* --------------------------------------- Équipe : parallaxe interne des photos */
  function teamParallax() {
    $$('.team__photo img').forEach(function (img) {
      var member = img.closest('.team__member') || img;
      gsap.fromTo(img,
        { yPercent: -9, scale: 1.09 },
        {
          yPercent: 9, scale: 1.09, ease: 'none',
          scrollTrigger: { trigger: member, start: 'top bottom', end: 'bottom top', scrub: .6 }
        });
    });
  }

  /* ------------------------------- Ticker : légère inclinaison selon la vitesse */
  /* Cohabite avec le défilement continu de main.js (xPercent) : GSAP compose les
     deux propriétés de transform indépendamment. Amplitude volontairement faible. */
  function tickerSkew() {
    var track = $('[data-ticker]');
    if (!track) return;

    var setSkew = gsap.quickTo(track, 'skewX', { duration: .45, ease: 'power3' });
    var clamp = gsap.utils.clamp(-6, 6);

    ST.create({
      onUpdate: function (self) { setSkew(clamp(self.getVelocity() / -320)); }
    });
  }

  /* ------------------------- Scène « flux » épinglée (l'équivalent de la canette) */
  /* Au scroll dans la section, le flux se construit : les outils apparaissent, se
     relient au hub, puis le hub alimente les sorties automatisées — pendant que
     les légendes défilent. Tout est scrubbé sur la progression de la section. */
  /* Le visuel de la scène est l'écosystème canvas (ecosystem.js), qui tourne en
     continu et réagit au scroll. Ici on ne pilote que le défilé des légendes,
     synchronisé sur la progression de la section épinglée. */
  function fluxScene() {
    var flux = $('[data-flux]');
    if (!flux) return;
    var caps = $$('.flux__cap', flux);
    if (!caps.length) return;

    gsap.set(caps, { opacity: 0 });
    gsap.set(caps[0], { opacity: 1 });

    var tl = gsap.timeline({
      scrollTrigger: {
        trigger: flux, start: 'top top', end: 'bottom bottom',
        scrub: .6, invalidateOnRefresh: true
      }
    });

    for (var i = 1; i < caps.length; i++) {
      tl.to(caps[i - 1], { opacity: 0, duration: .5 }, i)
        .to(caps[i],     { opacity: 1, duration: .5 }, i + 0.15);
    }
  }

  /* ---------------------------------------------------------------- Amorçage */
  var started = false;
  function init() {
    if (started) return;
    started = true;

    // Effets « scrubés » (parallaxes, zoom liés au scroll) DÉSACTIVÉS :
    // ils repeignaient à chaque frame de scroll et rendaient le scroll saccadé,
    // surtout au trackpad. On ne garde que des révélations one-shot (à l'entrée).
    // heroPush(); featureVisuals(); teamParallax(); tickerSkew();

    featureLists();   // apparition en cascade, une seule fois
    fluxScene();      // légendes de la scène flux (opacité only, section visible)
    steps();          // activation des étapes, une seule fois
    stats();          // montée des chiffres, une seule fois

    ST.refresh();
  }

  // Comme main.js : on attend les polices (le calcul des positions en dépend),
  // avec un filet de sécurité si la promesse traîne.
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(function () { window.setTimeout(init, 80); });
    window.setTimeout(init, 1400);
  } else {
    init();
  }
})();

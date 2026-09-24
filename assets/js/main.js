/* =============================================================================
   Croisia — interactions & animations
   Dépendances optionnelles (CDN) : GSAP + ScrollTrigger, Lenis.
   Aucune n'est obligatoire : sans GSAP un fallback IntersectionObserver prend
   le relais, sans Lenis le scroll natif suffit, sans JS tout reste visible.
   ========================================================================== */
(function () {
  'use strict';

  var root = document.documentElement;
  var reduceMotionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
  var reduceMotion = reduceMotionQuery.matches;

  var gsap    = window.gsap;
  var ST      = window.ScrollTrigger;
  var hasGSAP = typeof gsap !== 'undefined';
  var hasST   = hasGSAP && typeof ST !== 'undefined';
  var animate = hasST && !reduceMotion;

  // Les états initiaux (opacity 0, lignes masquées) ne sont appliqués que si JS
  // tourne : sans JS, aucune règle ne masque le contenu.
  if (!reduceMotion) {
    root.classList.add('js-anim');
    if (!hasST) root.classList.add('no-gsap');
    root.classList.add('anim-ready'); // désarme le filet de sécurité du <head>
  }
  if (hasST) gsap.registerPlugin(ST);

  var $  = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); };

  var headerOffset = function () {
    return parseFloat(getComputedStyle(root).getPropertyValue('--header-h')) || 76;
  };

  /* ------------------------------------------------- Scroll fluide (Lenis) */
  var lenis = null;

  (function smoothScroll() {
    // Scroll natif du navigateur : réponse instantanée, aucune latence.
    // (Le scroll fluide Lenis accumulait des secondes de retard sur machine chargée.)
    return;
    /* eslint-disable no-unreachable */
    if (reduceMotion || typeof window.Lenis === 'undefined') return;
    // Le scroll fluide se pilote au doigt sur mobile : on le laisse au natif.
    if (!window.matchMedia('(min-width: 900px)').matches) return;

    lenis = new window.Lenis({
      lerp: 0.09,          // glissé plus soyeux, mais toujours réactif (loin du flottement)
      wheelMultiplier: 1,
      smoothWheel: true,
      touchMultiplier: 1.5
    });

    if (hasST) {
      lenis.on('scroll', ST.update);
      gsap.ticker.add(function (time) { lenis.raf(time * 1000); });
      gsap.ticker.lagSmoothing(0);
    } else {
      var raf = function (t) { lenis.raf(t); window.requestAnimationFrame(raf); };
      window.requestAnimationFrame(raf);
    }
  })();

  // Ancres : Lenis ne capte pas les sauts natifs, on les prend en charge.
  (function anchors() {
    document.addEventListener('click', function (e) {
      var a = e.target.closest('a[href^="#"]');
      if (!a) return;

      var href = a.getAttribute('href');
      // Liens encore vides (Calendly, LinkedIn, mentions légales).
      if (href === '#') { e.preventDefault(); return; }

      var target = document.querySelector(href);
      if (!target) return;

      if (lenis) {
        e.preventDefault();
        lenis.scrollTo(target, { offset: -(headerOffset() + 16) });
        history.replaceState(null, '', href);
      }
    });
  })();

  /* ------------------------------------------- Découpe d'un titre en lignes */
  /* Chaque mot est enveloppé, on regroupe par position verticale, puis chaque
     ligne reçoit un masque (.ln) et un contenu translatable (.ln__i). */
  function wrapWords(node) {
    var walker = document.createTreeWalker(node, NodeFilter.SHOW_TEXT, null, false);
    var texts = [];
    var n;
    while ((n = walker.nextNode())) texts.push(n);

    texts.forEach(function (t) {
      if (!t.nodeValue.trim()) return;
      var frag = document.createDocumentFragment();
      t.nodeValue.split(/(\s+)/).forEach(function (part) {
        if (part === '') return;
        if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
        var s = document.createElement('span');
        s.className = 'w';
        s.textContent = part;
        frag.appendChild(s);
      });
      t.parentNode.replaceChild(frag, t);
    });
  }

  function splitLines(el) {
    if (el.__srcHTML === undefined) el.__srcHTML = el.innerHTML;
    el.innerHTML = el.__srcHTML;

    wrapWords(el);

    var words = $$('.w', el);
    if (!words.length) return [];

    // Regroupement par ligne : même position verticale à 2px près.
    var lines = [];
    var current = null;
    var lastTop = null;
    words.forEach(function (w) {
      var top = Math.round(w.getBoundingClientRect().top);
      if (lastTop === null || Math.abs(top - lastTop) > 2) {
        current = [];
        lines.push(current);
        lastTop = top;
      }
      current.push(w);
    });

    lines.forEach(function (ws) {
      var range = document.createRange();
      range.setStartBefore(ws[0]);
      range.setEndAfter(ws[ws.length - 1]);

      var inner = document.createElement('span');
      inner.className = 'ln__i';
      var outer = document.createElement('span');
      outer.className = 'ln';

      inner.appendChild(range.extractContents());
      outer.appendChild(inner);
      range.insertNode(outer);
    });

    return $$('.ln__i', el);
  }

  /* ------------------------------------------------------------ Animations */
  var splitTargets = $$('[data-split]');

  function reveals() {
    if (reduceMotion) return;

    var heroItems  = $$('[data-anim="hero"]');
    var heroTitle  = $('.hero__title');
    // Les panneaux de services ont leur propre déclenchement (galerie figée).
    var revealItems = $$('[data-reveal]').filter(function (el) {
      return !el.classList.contains('panel');
    });

    /* ---- Sans GSAP : IntersectionObserver + transitions CSS ------------- */
    if (!hasST) {
      splitTargets.forEach(function (el) { splitLines(el); });

      var showAll = function (el) {
        el.classList.add('is-visible');
        $$('.ln__i', el).forEach(function (i) { i.classList.add('is-visible'); });
      };

      heroItems.concat(heroTitle ? [heroTitle] : []).forEach(function (el, n) {
        window.setTimeout(function () { showAll(el); }, 100 * n);
      });

      var targets = revealItems.concat(splitTargets).concat($$('.panel'));

      if (!('IntersectionObserver' in window)) { targets.forEach(showAll); return; }

      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          showAll(entry.target);
          io.unobserve(entry.target);
        });
      }, { threshold: 0.15, rootMargin: '0px 0px -8% 0px' });

      targets.forEach(function (el) { io.observe(el); });
      return;
    }

    /* ---- Avec GSAP ------------------------------------------------------ */
    /* Deux pièges, d'où le fromTo avec `y` explicite :
       1. GSAP lit le translateY(110%) posé en CSS via la matrice calculée,
          donc en pixels : il le range dans `y`, pas dans `yPercent`.
       2. `y` et `yPercent` sont deux composants additionnés. Animer le seul
          `yPercent` vers 0 laisserait les 110% initiaux dans `y` — la ligne
          resterait sous son masque. On remet donc `y` à 0 des deux côtés. */
    var FROM = { yPercent: 110, y: 0 };

    function revealSplit(el) {
      var lines = splitLines(el);
      if (!lines.length) return;

      // Déjà révélé (re-découpe après redimensionnement) : on repose l'état final.
      if (el.dataset.splitShown === '1') { gsap.set(lines, { yPercent: 0, y: 0 }); return; }

      if (el.__splitTween) {
        if (el.__splitTween.scrollTrigger) el.__splitTween.scrollTrigger.kill();
        el.__splitTween.kill();
      }

      el.__splitTween = gsap.fromTo(lines, FROM,
        {
          yPercent: 0, y: 0, duration: 1.05, ease: 'expo.out', stagger: 0.09,
          scrollTrigger: {
            trigger: el, start: 'top 88%', once: true,
            onEnter: function () { el.dataset.splitShown = '1'; }
          }
        });
    }

    // Le hero se joue au chargement, sans attendre le scroll.
    var heroLines = heroTitle ? splitLines(heroTitle) : [];
    var tl = gsap.timeline({ defaults: { ease: 'expo.out' }, delay: 0.1 });
    if (heroLines.length) {
      heroTitle.dataset.splitShown = '1';
      tl.fromTo(heroLines, FROM, { yPercent: 0, y: 0, duration: 1.15, stagger: 0.1 });
    }
    tl.to(heroItems, { opacity: 1, y: 0, duration: 0.9, stagger: 0.09 }, heroLines.length ? '-=0.85' : 0);

    // Les autres titres se révèlent ligne par ligne à l'entrée dans l'écran.
    splitTargets.forEach(function (el) {
      if (el === heroTitle) return;
      revealSplit(el);
    });

    // Re-découpe au redimensionnement : le retour à la ligne change.
    var lastW = window.innerWidth;
    var resizeTimer = null;
    window.addEventListener('resize', function () {
      if (window.innerWidth === lastW) return; // ignore la barre d'URL mobile
      lastW = window.innerWidth;
      window.clearTimeout(resizeTimer);
      resizeTimer = window.setTimeout(function () {
        splitTargets.forEach(revealSplit);
        ST.refresh();
      }, 220);
    }, { passive: true });

    // Blocs courants : révélés par lots, avec un décalage naturel.
    ST.batch(revealItems, {
      start: 'top 88%',
      once: true,
      onEnter: function (batch) {
        gsap.to(batch, { opacity: 1, y: 0, duration: 0.9, ease: 'expo.out', stagger: 0.08 });
      }
    });
  }

  /* --------------------------------- Panneau qui s'ouvre en plein écran */
  function plate() {
    var frame = $('[data-plate]');
    var inner = $('[data-plate-inner]');
    if (!frame || !animate) return;

    // --plate-o passe de 1 (cadre inséré) à 0 (plein écran) : le clip-path et
    // le rayon sont composés en CSS à partir de cette seule variable.
    gsap.to(frame, {
      '--plate-o': 0,
      ease: 'none',
      scrollTrigger: {
        trigger: frame.parentElement,
        start: 'top top',
        end: '+=60%',
        scrub: 0.5
      }
    });

    if (inner) {
      gsap.to(inner, {
        scale: 1,
        ease: 'none',
        scrollTrigger: {
          trigger: frame.parentElement,
          start: 'top top',
          end: '+=60%',
          scrub: 0.5
        }
      });
    }
  }

  /* ------------------------------------- Étapes du flux qui s'allument */
  (function flowDemo() {
    var steps = $$('.flow__step');
    var bar = $('.plate__bar i');
    var saved = $('#flow-saved');
    if (!steps.length) return;

    if (reduceMotion) {
      steps.forEach(function (s) { s.classList.add('is-live'); });
      if (bar) bar.style.transform = 'scaleX(1)';
      if (saved) saved.textContent = '18';
      return;
    }

    var idx = 0;
    var timer = null;

    function tick() {
      if (idx === 0) steps.forEach(function (s) { s.classList.remove('is-live'); });
      steps[idx].classList.add('is-live');

      if (bar) bar.style.transform = 'scaleX(' + ((idx + 1) / steps.length) + ')';
      if (saved) saved.textContent = String(Math.round(((idx + 1) / steps.length) * 18));

      idx = (idx + 1) % steps.length;
      timer = window.setTimeout(tick, idx === 0 ? 2400 : 1200);
    }

    function start() { if (!timer) tick(); }
    function stop() { window.clearTimeout(timer); timer = null; }

    // La boucle ne tourne que si le panneau est visible et l'onglet actif.
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) { entry.isIntersecting ? start() : stop(); });
      }, { threshold: 0.25 }).observe(steps[0].closest('.plate__inner') || steps[0]);
    } else {
      start();
    }

    document.addEventListener('visibilitychange', function () {
      document.hidden ? stop() : start();
    });
  })();

  /* ------------------------------------ Services : galerie horizontale */
  function rail() {
    var rail = $('[data-rail]');
    var track = $('[data-rail-track]');
    var panels = $$('.panel', rail || document);
    if (!rail || !track) return;

    // Révélation des panneaux, valable dans les deux dispositions.
    if (animate) {
      gsap.to(panels, {
        opacity: 1, y: 0, duration: 0.9, ease: 'expo.out', stagger: 0.1,
        scrollTrigger: { trigger: rail, start: 'top 75%', once: true }
      });
    }

    if (!animate) return;

    var distance = function () {
      var styles = getComputedStyle(track);
      var pad = parseFloat(styles.paddingLeft) + parseFloat(styles.paddingRight);
      return Math.max(0, track.scrollWidth - window.innerWidth + pad);
    };

    /* matchMedia explicite plutôt que gsap.matchMedia() : ce dernier ne s'est
       pas réveillé de façon fiable quand la fenêtre passe de mobile à desktop
       après le chargement. On double la bascule avec l'événement resize. */
    var mq = window.matchMedia('(min-width: 1024px)');
    var teardown = null;

    function enable() {
      rail.classList.add('is-rail');

      var sticky = $('.rail__sticky', rail);
      var head = $('.rail__head', rail);

      // Le titre défile avant l'épinglage : sa hauteur s'ajoute à la course.
      var setHeight = function () {
        rail.style.height =
          ((head ? head.offsetHeight : 0) + window.innerHeight + distance()) + 'px';
      };
      setHeight();
      ST.addEventListener('refreshInit', setHeight);

      var tween = gsap.to(track, {
        x: function () { return -distance(); },
        ease: 'none',
        scrollTrigger: {
          // Déclenché sur la zone épinglée, pas sur la section : sinon le
          // défilement horizontal démarrerait pendant que le titre monte.
          trigger: sticky,
          start: 'top top',
          end: function () { return '+=' + distance(); },
          scrub: 0.6,
          invalidateOnRefresh: true
        }
      });

      /* La piste avance par transform, pas par scroll : au clavier, le panneau
         qui prend le focus resterait hors écran. On traduit sa position
         horizontale en position de scroll verticale. */
      var sticky = $('.rail__sticky', rail);
      var onFocus = function (e) {
        var panel = e.target.closest('.panel');
        if (!panel) return;
        // Le navigateur peut tenter de faire défiler le conteneur clippé.
        if (sticky) sticky.scrollLeft = 0;

        var gutter = parseFloat(getComputedStyle(track).paddingLeft) || 0;
        var wanted = rail.offsetTop + Math.min(distance(), Math.max(0, panel.offsetLeft - gutter));
        if (lenis) lenis.scrollTo(wanted, { immediate: true });
        else window.scrollTo(0, wanted);
      };
      rail.addEventListener('focusin', onFocus);

      return function cleanup() {
        ST.removeEventListener('refreshInit', setHeight);
        rail.removeEventListener('focusin', onFocus);
        if (tween.scrollTrigger) tween.scrollTrigger.kill();
        tween.kill();
        gsap.set(track, { clearProps: 'transform' });
        rail.style.height = '';
        rail.classList.remove('is-rail');
      };
    }

    function sync() {
      if (mq.matches && !teardown) { teardown = enable(); ST.refresh(); }
      else if (!mq.matches && teardown) { teardown(); teardown = null; ST.refresh(); }
    }

    if (mq.addEventListener) mq.addEventListener('change', sync);
    else if (mq.addListener) mq.addListener(sync);

    var resizeTimer = null;
    window.addEventListener('resize', function () {
      window.clearTimeout(resizeTimer);
      resizeTimer = window.setTimeout(sync, 240);
    }, { passive: true });

    sync();
  }

  /* ------------------------------------------------------------ Parallaxe */
  function parallax() {
    return;   // désactivé : la parallaxe scrubée du hero alourdissait le scroll
    /* eslint-disable no-unreachable */
    if (!animate) return;

    $$('[data-parallax]').forEach(function (el) {
      var amount = parseFloat(el.dataset.parallax) || 0.1;
      var shift = amount * 100;
      gsap.fromTo(el,
        { yPercent: -shift / 2, scale: 1.12 },
        {
          yPercent: shift / 2, scale: 1.12, ease: 'none',
          scrollTrigger: {
            trigger: el.parentElement,
            start: 'top bottom',
            end: 'bottom top',
            scrub: 0.5
          }
        });
    });
  }

  /* Le découpe-lignes mesure des positions : tant que les polices ne sont pas
     appliquées, les retours à la ligne sont ceux de la police de secours.
     On attend donc `fonts.ready`, avec un garde-fou si la promesse traîne. */
  (function boot() {
    var started = false;
    var go = function () {
      if (started) return;
      started = true;
      reveals();
      plate();
      rail();
      parallax();
      if (hasST) ST.refresh();
    };

    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(go);
      window.setTimeout(go, 1200);
    } else {
      go();
    }
  })();

  /* -------------------------------------------------------------- Ticker */
  (function ticker() {
    var track = $('[data-ticker]');
    if (!track || reduceMotion) return;

    // On double le contenu : la boucle à -50% devient invisible.
    var items = $$('li', track);
    items.forEach(function (li) {
      var clone = li.cloneNode(true);
      clone.setAttribute('aria-hidden', 'true');
      track.appendChild(clone);
    });

    if (hasGSAP) {
      gsap.to(track, { xPercent: -50, duration: 32, ease: 'none', repeat: -1 });
    }
  })();

  /* ------------------------------------------------------------ Compteurs */
  (function counters() {
    var els = $$('.counter');
    if (!els.length) return;

    function run(el) {
      var target = parseFloat(el.dataset.to || '0');
      if (reduceMotion) { el.textContent = String(target); return; }

      var duration = 1600;
      var start = null;

      function frame(ts) {
        if (start === null) start = ts;
        var p = Math.min(1, (ts - start) / duration);
        var eased = 1 - Math.pow(1 - p, 3);           // easeOutCubic
        el.textContent = String(Math.round(target * eased));
        if (p < 1) window.requestAnimationFrame(frame);
      }
      window.requestAnimationFrame(frame);
    }

    if (!('IntersectionObserver' in window)) { els.forEach(run); return; }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        run(entry.target);
        io.unobserve(entry.target);
      });
    }, { threshold: 0.4 });

    els.forEach(function (el) { io.observe(el); });
  })();

  /* ------------------------------------------------- Mot pivotant du hero */
  (function rotator() {
    var el = $('#rotator');
    if (!el) return;

    var words = ['perdre du temps', 'faire à la main', 'rater des clients'];
    var i = 0;

    if (reduceMotion) { el.textContent = words[0]; return; }

    var wrap = el.parentNode;

    function widthOf(text) {
      var ghost = el.cloneNode(false);
      ghost.textContent = text;
      ghost.style.position = 'absolute';
      ghost.style.visibility = 'hidden';
      ghost.style.whiteSpace = 'nowrap';
      wrap.appendChild(ghost);
      var w = ghost.getBoundingClientRect().width;
      wrap.removeChild(ghost);
      return w;
    }

    if (!hasGSAP) {
      window.setInterval(function () {
        i = (i + 1) % words.length;
        el.textContent = words[i];
      }, 2600);
      return;
    }

    wrap.style.width = widthOf(words[0]) + 'px';

    function next() {
      var n = (i + 1) % words.length;
      gsap.timeline({ onComplete: function () { i = n; window.setTimeout(next, 2000); } })
        .to(el, { yPercent: -110, opacity: 0, duration: 0.42, ease: 'power2.in' })
        .to(wrap, { width: widthOf(words[n]), duration: 0.6, ease: 'expo.out' }, '<0.1')
        .set(el, { textContent: words[n], yPercent: 110, opacity: 1 })
        .to(el, { yPercent: 0, duration: 0.65, ease: 'expo.out' });
    }

    window.setTimeout(next, 2400);

    // La largeur figée en px doit suivre les changements de taille de police.
    window.addEventListener('resize', function () {
      wrap.style.width = widthOf(words[i]) + 'px';
    }, { passive: true });
  })();

  /* --------------------------------------------------- Boutons magnétiques */
  (function magnetic() {
    if (reduceMotion || !hasGSAP) return;
    if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;

    $$('[data-magnetic]').forEach(function (el) {
      var reset = function () {
        gsap.to(el, { x: 0, y: 0, duration: 0.6, ease: 'elastic.out(1, 0.4)' });
      };

      el.addEventListener('pointermove', function (e) {
        var r = el.getBoundingClientRect();
        gsap.to(el, {
          x: (e.clientX - (r.left + r.width / 2)) * 0.22,
          y: (e.clientY - (r.top + r.height / 2)) * 0.35,
          duration: 0.5, ease: 'power3.out'
        });
      });
      el.addEventListener('pointerleave', reset);
      el.addEventListener('blur', reset);
    });
  })();

  /* ------------------------------------------ Header : état + progression */
  (function header() {
    var header = $('#header');
    var progress = $('#scroll-progress');
    if (!header) return;

    var ticking = false;

    function update() {
      ticking = false;
      var y = window.scrollY || window.pageYOffset;
      header.classList.toggle('is-scrolled', y > 12);

      if (progress) {
        var max = document.documentElement.scrollHeight - window.innerHeight;
        var pct = max > 0 ? Math.min(100, (y / max) * 100) : 0;
        progress.style.width = pct.toFixed(2) + '%';
      }
    }

    window.addEventListener('scroll', function () {
      if (!ticking) { ticking = true; window.requestAnimationFrame(update); }
    }, { passive: true });

    update();
  })();

  /* --------------------------------------------------------- Menu mobile */
  (function mobileNav() {
    var toggle = $('#nav-toggle');
    var panel = $('#mobile-nav');
    if (!toggle || !panel) return;

    var lastFocused = null;

    function open() {
      lastFocused = document.activeElement;
      panel.hidden = false;
      // Reflow forcé : la transition doit partir de l'état fermé.
      void panel.offsetWidth;
      panel.classList.add('is-open');
      toggle.setAttribute('aria-expanded', 'true');
      toggle.setAttribute('aria-label', 'Fermer le menu');
      document.body.classList.add('is-locked');
      if (lenis) lenis.stop();
      var first = $('a', panel);
      if (first) first.focus();
    }

    function close(restoreFocus) {
      panel.classList.remove('is-open');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-label', 'Ouvrir le menu');
      document.body.classList.remove('is-locked');
      if (lenis) lenis.start();

      var hide = function () { panel.hidden = true; };
      if (reduceMotion) hide();
      else window.setTimeout(hide, 300);

      if (restoreFocus && lastFocused) lastFocused.focus();
    }

    toggle.addEventListener('click', function () {
      if (toggle.getAttribute('aria-expanded') === 'true') close(true);
      else open();
    });

    panel.addEventListener('click', function (e) {
      if (e.target.closest('a')) close(false);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') close(true);
    });

    // Le panneau n'existe qu'en dessous de 900px : on referme au passage desktop.
    var desktop = window.matchMedia('(min-width: 900px)');
    var onDesktop = function (e) {
      if (e.matches && toggle.getAttribute('aria-expanded') === 'true') close(false);
    };
    if (desktop.addEventListener) desktop.addEventListener('change', onDesktop);
    else if (desktop.addListener) desktop.addListener(onDesktop);
  })();

  /* ------------------------------------------- Lien de nav actif au scroll */
  (function scrollSpy() {
    var links = $$('.nav__list a');
    if (!links.length || !('IntersectionObserver' in window)) return;

    var map = {};
    var sections = [];

    links.forEach(function (link) {
      var id = link.getAttribute('href');
      if (!id || id.charAt(0) !== '#') return;
      var section = document.querySelector(id);
      if (!section) return;
      map[id.slice(1)] = link;
      sections.push(section);
    });

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var link = map[entry.target.id];
        if (!link) return;
        if (entry.isIntersecting) {
          links.forEach(function (l) { l.classList.remove('is-active'); });
          link.classList.add('is-active');
        }
      });
    }, { rootMargin: '-45% 0px -50% 0px' });

    sections.forEach(function (s) { io.observe(s); });
  })();

  /* ----------------------------------------------------------------- FAQ */
  (function faq() {
    var buttons = $$('.faq__q');
    if (!buttons.length) return;

    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var item = btn.closest('.faq__item');
        var isOpen = btn.getAttribute('aria-expanded') === 'true';

        // Accordéon : une seule réponse ouverte à la fois.
        buttons.forEach(function (other) {
          other.setAttribute('aria-expanded', 'false');
          other.closest('.faq__item').classList.remove('is-open');
        });

        if (!isOpen) {
          btn.setAttribute('aria-expanded', 'true');
          item.classList.add('is-open');
        }
        // La hauteur change : les déclencheurs suivants doivent se recalculer.
        if (hasST) window.setTimeout(function () { ST.refresh(); }, 420);
      });
    });
  })();

  /* ---------------------------------------------------------- Formulaire */
  (function auditForm() {
    var form = $('#audit-form');
    if (!form) return;

    var success = $('#form-success');
    var status = $('#form-status');
    var submit = $('#submit-btn');
    var resetBtn = $('#form-reset');

    var RULES = {
      nom: {
        el: $('#f-nom'), err: $('#e-nom'),
        test: function (v) { return v.trim().length >= 2; },
        message: 'Merci d’indiquer votre nom.'
      },
      email: {
        el: $('#f-email'), err: $('#e-email'),
        test: function (v) { return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim()); },
        message: 'Cette adresse email ne semble pas valide.'
      },
      entreprise: {
        el: $('#f-entreprise'), err: $('#e-entreprise'),
        test: function (v) { return v.trim().length >= 2; },
        message: 'Merci d’indiquer le nom de votre entreprise.'
      },
      telephone: {
        el: $('#f-tel'), err: $('#e-tel'),
        test: function (v) { return v.trim() === '' || /^[+0-9 ().-]{8,20}$/.test(v.trim()); },
        message: 'Ce numéro ne semble pas valide (ou laissez le champ vide).'
      },
      tache: {
        el: $('#f-tache'), err: $('#e-tache'),
        test: function (v) { return v.trim().length >= 10; },
        message: 'Décrivez la tâche en quelques mots (10 caractères minimum).'
      }
    };

    function setError(rule, message) {
      if (!rule.el || !rule.err) return;
      if (message) {
        rule.el.setAttribute('aria-invalid', 'true');
        rule.err.textContent = message;
        rule.err.hidden = false;
      } else {
        rule.el.removeAttribute('aria-invalid');
        rule.err.textContent = '';
        rule.err.hidden = true;
      }
    }

    function validate(rule) {
      if (!rule.el) return true;
      var ok = rule.test(rule.el.value);
      setError(rule, ok ? null : rule.message);
      return ok;
    }

    // Validation inline : au blur, puis en direct une fois le champ en erreur.
    Object.keys(RULES).forEach(function (key) {
      var rule = RULES[key];
      if (!rule.el) return;
      rule.el.addEventListener('blur', function () { validate(rule); });
      rule.el.addEventListener('input', function () {
        if (rule.el.getAttribute('aria-invalid') === 'true') validate(rule);
      });
    });

    function showSuccess() {
      form.classList.add('is-hidden');
      success.hidden = false;

      if (!reduceMotion && hasGSAP) {
        gsap.fromTo(success, { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.7, ease: 'expo.out' });
        gsap.fromTo($('.form-success__badge', success),
          { scale: 0.5, opacity: 0 },
          { scale: 1, opacity: 1, duration: 0.6, ease: 'back.out(2)', delay: 0.1 });
      }
      if (hasST) window.setTimeout(function () { ST.refresh(); }, 300);

      var heading = $('h3', success);
      if (heading) {
        heading.setAttribute('tabindex', '-1');
        heading.focus();
      }
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (status) status.textContent = '';

      // Honeypot : rempli = bot. On simule un succès sans rien envoyer.
      var hp = $('#f-site');
      if (hp && hp.value.trim() !== '') { showSuccess(); return; }

      var firstInvalid = null;
      Object.keys(RULES).forEach(function (key) {
        var ok = validate(RULES[key]);
        if (!ok && !firstInvalid) firstInvalid = RULES[key].el;
      });

      if (firstInvalid) {
        if (status) status.textContent = 'Quelques champs sont à corriger avant l’envoi.';
        firstInvalid.focus();
        if (!reduceMotion && hasGSAP) {
          gsap.fromTo(firstInvalid, { x: -6 }, { x: 0, duration: 0.5, ease: 'elastic.out(1, 0.35)' });
        }
        return;
      }

      var endpoint = form.dataset.endpoint;
      submit.classList.add('is-loading');
      submit.setAttribute('aria-disabled', 'true');

      // Sans endpoint configuré, le site tourne en mode démo :
      // le formulaire valide et confirme, mais rien n'est envoyé.
      if (!endpoint) {
        window.setTimeout(function () {
          submit.classList.remove('is-loading');
          submit.removeAttribute('aria-disabled');
          showSuccess();
          console.info('[Croisia] Aucun endpoint configuré (data-endpoint vide) : envoi simulé.');
        }, 700);
        return;
      }

      fetch(endpoint, {
        method: 'POST',
        headers: { Accept: 'application/json' },
        body: new FormData(form)
      })
        .then(function (res) {
          if (!res.ok) throw new Error('HTTP ' + res.status);
          showSuccess();
        })
        .catch(function () {
          if (status) {
            status.textContent =
              'L’envoi a échoué. Écrivez-moi directement à contact@croisia.com, je vous réponds sous 24 h.';
          }
        })
        .then(function () {
          submit.classList.remove('is-loading');
          submit.removeAttribute('aria-disabled');
        });
    });

    if (resetBtn) {
      resetBtn.addEventListener('click', function () {
        form.reset();
        Object.keys(RULES).forEach(function (key) { setError(RULES[key], null); });
        success.hidden = true;
        form.classList.remove('is-hidden');
        if (status) status.textContent = '';
        var first = $('#f-nom');
        if (first) first.focus();
      });
    }
  })();

  /* -------------------------------------------------------------- Divers */
  (function misc() {
    var year = $('#year');
    if (year) year.textContent = String(new Date().getFullYear());
  })();

  /* ----------------------- Si l'utilisateur active « moins d'animations » */
  var onReduceChange = function (e) { if (e.matches) window.location.reload(); };
  if (reduceMotionQuery.addEventListener) reduceMotionQuery.addEventListener('change', onReduceChange);
  else if (reduceMotionQuery.addListener) reduceMotionQuery.addListener(onReduceChange);
})();

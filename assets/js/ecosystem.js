/* =============================================================================
   Altiora — Écosystème (l'effet « wow » qui bouge sur lui-même)
   ---------------------------------------------------------------------------
   Un réseau de nœuds répartis sur une sphère (vos outils) relié par des lignes
   fines, tournant en continu autour d'un cœur « Altiora ». Il s'accélère, zoome
   et s'illumine au fil du scroll dans la section, et s'incline avec la souris.

   Vanilla canvas, sans dépendance. Perf : DPR plafonné, boucle en pause hors
   écran / onglet inactif, rendu unique en reduced-motion. Le scroll ne fait que
   mettre à jour une cible (lissée dans la boucle) — donc aucun jank au scroll.
   ========================================================================== */
(function () {
  'use strict';

  var canvas = document.getElementById('eco-canvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  if (!ctx) return;

  var reduce  = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var section = canvas.closest('.flux');

  var ACCENT  = [167, 139, 250];   // #A78BFA (sombre)
  var ACCENT2 = [124, 196, 250];   // #7CC4FA
  var LIGHT   = [245, 245, 247];
  // Variante thème clair
  var INK           = [22, 22, 26];    // encre
  var ACCENT_LIGHT  = [109, 40, 217];  // #6D28D9
  var ACCENT2_LIGHT = [79, 70, 229];   // #4F46E5
  var GOLD_DARK     = [240, 200, 130];
  var GOLD_LIGHT    = [176, 120, 20];  // ambre profond (contraste sur clair)

  function rgba(c, a) { return 'rgba(' + c[0] + ',' + c[1] + ',' + c[2] + ',' + a + ')'; }
  function mix(a, b, t) { return [a[0]+(b[0]-a[0])*t, a[1]+(b[1]-a[1])*t, a[2]+(b[2]-a[2])*t]; }

  var DPR = Math.min(window.devicePixelRatio || 1, 1.5);   // plafonné : moins de pixels à composer au scroll
  var W = 0, H = 0, cx = 0, cy = 0, R = 0;

  function resize() {
    var rect = canvas.getBoundingClientRect();
    W = rect.width; H = rect.height;
    if (!W || !H) return;
    canvas.width  = Math.round(W * DPR);
    canvas.height = Math.round(H * DPR);
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    cx = W / 2; cy = H / 2;
    R = Math.min(W * 0.62, H) * 0.46;
  }

  /* ---- Modèle : sphère de Fibonacci + étiquettes d'outils --------------- */
  var N = window.innerWidth < 720 ? 38 : 60;
  var TASKS = [
    'Gestion des leads', 'Qualification des leads', 'Scoring des prospects', 'Nurturing',
    'Prospection', 'Prise de RDV', 'Suivi des devis', 'Envoi des devis', 'Relances commerciales',
    'Suivi du pipeline', 'Réponses aux demandes', 'Onboarding client', 'Suivi client',
    'Support 24/7', 'Tri des demandes', 'Tickets support', 'Collecte d’avis', 'Satisfaction client',
    'FAQ dynamique', 'Facturation', 'Relances d’impayés', 'Recouvrement', 'Rapprochement bancaire',
    'Notes de frais', 'Suivi des paiements', 'Bons de commande', 'Export comptable', 'Devis automatiques',
    'Saisie automatisée', 'Synchronisation CRM', 'Mise à jour CRM', 'Reporting hebdo', 'Tableaux de bord',
    'Alertes & notifications', 'Sauvegardes', 'Import / export', 'Archivage', 'Suivi des stocks',
    'Suivi des commandes', 'Suivi des livraisons', 'Planning & rappels', 'Comptes-rendus', 'Veille concurrentielle',
    'Génération de documents', 'Signatures électroniques', 'Gestion des contrats', 'Newsletter',
    'Publication réseaux', 'Séquences e-mail', 'Segmentation', 'Campagnes e-mail', 'Relance panier',
    'Demandes de congés', 'Suivi des candidatures', 'Résumés de réunion', 'Gestion documentaire',
    'Suivi SAV', 'Qualification entrante', 'Réponses e-mail', 'Facturation récurrente', 'Suivi des abonnements',
    'Enquêtes de satisfaction', 'Rapports clients', 'Mises à jour projet'
  ];
  var nodes = [];
  var GA = Math.PI * (3 - Math.sqrt(5));
  for (var i = 0; i < N; i++) {
    var y = 1 - (i / (N - 1)) * 2;
    var r = Math.sqrt(Math.max(0, 1 - y * y));
    var phi = i * GA;
    nodes.push({ x: Math.cos(phi) * r, y: y, z: Math.sin(phi) * r, tool: null });
  }
  // Beaucoup d'étiquettes : on en pose sur une large majorité des sommets,
  // réparties régulièrement sur la sphère.
  var LABELED = Math.min(TASKS.length, Math.round(N * 0.75));
  for (var t = 0; t < LABELED; t++) {
    var idx = Math.round((t + 0.5) * (N / LABELED)) % N;
    while (nodes[idx].tool) idx = (idx + 1) % N;   // évite d'écraser une étiquette
    nodes[idx].tool = TASKS[t % TASKS.length];
  }
  // Quelques nœuds « primaires » reliés au cœur (structure + relation au hub).
  var PRIM = window.innerWidth < 720 ? 6 : 8;
  var labeledIdx0 = [];
  nodes.forEach(function (n, ix) { if (n.tool) labeledIdx0.push(ix); });
  for (var pI = 0; pI < PRIM && labeledIdx0.length > 1; pI++) {
    nodes[labeledIdx0[Math.round(pI * (labeledIdx0.length - 1) / (PRIM - 1))]].primary = true;
  }

  // Connexions (voisins proches en 3D), plafonnées pour rester fines.
  var links = [];
  var THRESH = 0.62, MAXPER = 3;
  for (var a = 0; a < N; a++) {
    var cand = [];
    for (var b = 0; b < N; b++) {
      if (a === b) continue;
      var dx = nodes[a].x - nodes[b].x, dy = nodes[a].y - nodes[b].y, dz = nodes[a].z - nodes[b].z;
      var d = Math.sqrt(dx*dx + dy*dy + dz*dz);
      if (d < THRESH) cand.push({ b: b, d: d });
    }
    cand.sort(function (p, q) { return p.d - q.d; });
    for (var k = 0; k < Math.min(MAXPER, cand.length); k++) {
      var j = cand[k].b;
      if (a < j) links.push([a, j]);
    }
  }
  // Nœuds primaires : liés au cœur (0,0,0) pour matérialiser le hub.
  var toolIdx = [];
  nodes.forEach(function (n, ix) { if (n.primary) toolIdx.push(ix); });

  // Adjacence (pour le fil doré qui marche de sommet en sommet).
  var adj = [];
  for (var ai = 0; ai < N; ai++) adj[ai] = [];
  links.forEach(function (l) { adj[l[0]].push(l[1]); adj[l[1]].push(l[0]); });

  /* ---- État animé ------------------------------------------------------- */
  var rotY = 0.6, rotX = -0.32;
  var yawOff = 0, yawTgt = 0, tiltOff = 0, tiltTgt = 0;
  var energy = 0, energyTgt = 0;
  var zoom = 1, zoomTgt = 1;
  var tPrev = 0, clock = 0, lastDt = 0;
  var scrolling = false, scrollTO = null;   // on gèle le rendu pendant le scroll

  /* ---- Fil doré : une étincelle qui court d'un sommet à l'autre ---------- */
  var GOLD = [240, 200, 130];
  var sparks = [];
  function pickStart() {
    for (var tries = 0; tries < 24; tries++) {
      var s = Math.floor(Math.random() * N);
      if (adj[s].length) return s;
    }
    return 0;
  }
  function newSpark() {
    var f = pickStart();
    var to = adj[f][Math.floor(Math.random() * adj[f].length)];
    return { from: f, to: to, prev: -1, t: 0, trail: [] };
  }
  function stepSpark(sp, P) {
    sp.trail.push({ a: sp.from, b: sp.to, life: 1 });
    if (sp.trail.length > 3) sp.trail.shift();
    sp.prev = sp.from; sp.from = sp.to;
    var opts = adj[sp.from].filter(function (n) { return n !== sp.prev; });
    if (!opts.length) opts = adj[sp.from];
    // on privilégie les sommets face à nous (arêtes visibles) → rendu propre
    opts.sort(function (a, b) { return P[b].z - P[a].z; });
    sp.to = opts[Math.floor(Math.random() * Math.min(opts.length, 3))];
  }

  function scrollProgress() {
    if (!section) return 0;
    var r = section.getBoundingClientRect();
    var total = section.offsetHeight - window.innerHeight;
    if (total <= 0) return 0;
    return Math.max(0, Math.min(1, (-r.top) / total));
  }

  function project(n) {
    var ry = rotY + yawOff, rx = rotX + tiltOff;
    var cY = Math.cos(ry), sY = Math.sin(ry);
    var x1 =  n.x * cY - n.z * sY;
    var z1 =  n.x * sY + n.z * cY;
    var cX = Math.cos(rx), sX = Math.sin(rx);
    var y1 =  n.y * cX - z1 * sX;
    var z2 =  n.y * sX + z1 * cX;
    var persp = 1 / (1 - z2 * 0.32);
    return {
      sx: cx + x1 * R * zoom * persp,
      sy: cy + y1 * R * zoom * persp,
      z: z2, persp: persp
    };
  }

  function draw() {
    if (!W || !H) return;
    ctx.clearRect(0, 0, W, H);

    // Palette dérivée du thème (clair / sombre)
    var dark = document.documentElement.dataset.theme !== 'light';
    var ACC  = dark ? ACCENT : ACCENT_LIGHT;
    var ACC2 = dark ? ACCENT2 : ACCENT2_LIGHT;
    var FG   = dark ? [255, 255, 255] : INK;   // premier plan (labels, cœur)
    var NODE = dark ? LIGHT : INK;
    var gold = dark ? GOLD_DARK : GOLD_LIGHT;

    var lineCol = mix(FG, ACC, 0.25 + energy * 0.65);

    // Cœur : halo lumineux qui respire
    var pulse = 1 + Math.sin(clock * 1.6) * 0.06 + energy * 0.25;
    var coreR = R * 0.17 * pulse;
    var grad = ctx.createRadialGradient(cx, cy, 0, cx, cy, coreR * 2.4);
    grad.addColorStop(0, rgba(mix(ACC, [255, 255, 255], dark ? 0.3 : 0.1), dark ? 0.9 : 0.55));
    grad.addColorStop(0.35, rgba(ACC, (dark ? 0.5 : 0.32) + energy * 0.3));
    grad.addColorStop(1, rgba(ACC, 0));
    ctx.fillStyle = grad;
    ctx.beginPath(); ctx.arc(cx, cy, coreR * 2.4, 0, Math.PI * 2); ctx.fill();

    // Projections
    var P = new Array(N);
    for (var i = 0; i < N; i++) P[i] = project(nodes[i]);

    // Liens cœur → outils (le hub), + impulsions qui voyagent avec l'énergie
    for (var ti = 0; ti < toolIdx.length; ti++) {
      var p = P[toolIdx[ti]];
      var a = (0.10 + energy * 0.5) * (0.5 + (p.z + 1) / 2 * 0.5);
      ctx.strokeStyle = rgba(mix(ACC, ACC2, (ti % 2)), a);
      ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(p.sx, p.sy); ctx.stroke();
      if (energy > 0.02) {
        var tt = (clock * 0.5 + ti * 0.13) % 1;
        var dx = cx + (p.sx - cx) * tt, dy = cy + (p.sy - cy) * tt;
        ctx.fillStyle = rgba(ACC, energy * 0.9 * (p.z + 1) / 2);
        ctx.beginPath(); ctx.arc(dx, dy, 1.6 + energy, 0, Math.PI * 2); ctx.fill();
      }
    }

    // Mailles fines entre nœuds voisins
    for (var l = 0; l < links.length; l++) {
      var pa = P[links[l][0]], pb = P[links[l][1]];
      var depth = ((pa.z + pb.z) / 2 + 1) / 2;      // 0 arrière, 1 avant
      var alpha = (0.05 + depth * 0.22) * (0.6 + energy * 0.8);
      ctx.strokeStyle = rgba(lineCol, alpha);
      ctx.lineWidth = 0.6 + depth * 0.7;
      ctx.beginPath(); ctx.moveTo(pa.sx, pa.sy); ctx.lineTo(pb.sx, pb.sy); ctx.stroke();
    }

    // Nœuds (triés arrière → avant pour un rendu correct)
    var order = [];
    for (var o = 0; o < N; o++) order.push(o);
    order.sort(function (m, n) { return P[m].z - P[n].z; });

    for (var oi = 0; oi < order.length; oi++) {
      var ix = order[oi], pp = P[ix], nd = nodes[ix];
      var depth2 = (pp.z + 1) / 2;                   // 0..1
      var isPrimary = !!nd.primary, isLabeled = !!nd.tool;
      var rad = (isPrimary ? 3.0 : isLabeled ? 2.1 : 1.6) * pp.persp * (0.55 + depth2 * 0.6);
      var col = isLabeled ? (dark ? mix(ACCENT, [255, 255, 255], 0.2) : ACC) : NODE;
      ctx.fillStyle = rgba(col, (isLabeled ? 0.5 : 0.28) + depth2 * 0.5);
      ctx.beginPath(); ctx.arc(pp.sx, pp.sy, rad, 0, Math.PI * 2); ctx.fill();
      if (isPrimary) {
        ctx.fillStyle = rgba(ACC, 0.12 * depth2 + energy * 0.08);
        ctx.beginPath(); ctx.arc(pp.sx, pp.sy, rad * 2.4, 0, Math.PI * 2); ctx.fill();
      }
    }

    // Étiquettes : nombreuses, mais celles de l'avant priment et on masque
    // celles qui se chevauchent → dense mais lisible.
    var labeled = [];
    for (var li = 0; li < N; li++) if (nodes[li].tool && P[li].z > 0.06) labeled.push(li);
    labeled.sort(function (a, b) { return P[b].z - P[a].z; });
    ctx.font = '500 11px Inter, system-ui, sans-serif';
    ctx.textAlign = 'left'; ctx.textBaseline = 'middle';
    var boxes = [];
    for (var lj = 0; lj < labeled.length; lj++) {
      var pi = labeled[lj], p2 = P[pi], word = nodes[pi].tool;
      var tw = ctx.measureText(word).width;
      // Près du bord droit (téléphone), l'étiquette passe à gauche du point
      var flip = p2.sx + 6 + tw > W - 4;
      var bx = flip ? p2.sx - 6 - tw - 6 : p2.sx + 6, by = p2.sy - 6, bw = tw + 6, bh = 13;
      if (bx < 2) continue;
      var ok = true;
      for (var bk = 0; bk < boxes.length; bk++) {
        var d = boxes[bk];
        if (bx < d.x + d.w && bx + bw > d.x && by < d.y + d.h && by + bh > d.y) { ok = false; break; }
      }
      if (!ok) continue;
      boxes.push({ x: bx, y: by, w: bw, h: bh });
      ctx.fillStyle = rgba(FG, Math.min(0.95, (p2.z - 0.06) * 1.15));
      ctx.textAlign = flip ? 'right' : 'left';
      ctx.fillText(word, flip ? p2.sx - 6 : p2.sx + 6, p2.sy);
    }

    // Cœur : le symbole Croisia (pyramide de losanges)
    ctx.textAlign = 'left';
    var LOGO = [[50,24,1],[36,38,.62],[64,38,.62],[22,52,.36],[50,52,.36],[78,52,.36],[8,66,.18],[36,66,.18],[64,66,.18],[92,66,.18]];
    var ls = coreR * 0.62 / 44, lc = [42, 33, 25];   // #2A2119
    for (var lg = 0; lg < LOGO.length; lg++) {
      var gx = cx + (LOGO[lg][0] - 50) * ls, gy = cy + (LOGO[lg][1] - 45) * ls, gh = 11 * ls;
      ctx.fillStyle = rgba(dark ? [255, 255, 255] : lc, LOGO[lg][2] * 0.95);
      ctx.beginPath();
      ctx.moveTo(gx, gy - gh); ctx.lineTo(gx + gh, gy); ctx.lineTo(gx, gy + gh); ctx.lineTo(gx - gh, gy);
      ctx.closePath(); ctx.fill();
    }

    // ---- Fil doré (sombre) / ambre (clair) : l'automatisation qui circule --
    var want = energy > 0.55 ? 2 : 1;
    while (sparks.length < want) sparks.push(newSpark());
    while (sparks.length > want) sparks.pop();

    var edgeTime = 0.72 - energy * 0.30;            // secondes par arête
    for (var s = 0; s < sparks.length; s++) {
      var sp = sparks[s];
      sp.t += lastDt / edgeTime;
      while (sp.t >= 1) { sp.t -= 1; stepSpark(sp, P); }

      // traînée qui s'efface
      for (var q = 0; q < sp.trail.length; q++) {
        var seg = sp.trail[q]; seg.life *= 0.90;
        var qa = P[seg.a], qb = P[seg.b];
        ctx.strokeStyle = rgba(gold, seg.life * (dark ? 0.35 : 0.5));
        ctx.lineWidth = 1.3;
        ctx.beginPath(); ctx.moveTo(qa.sx, qa.sy); ctx.lineTo(qb.sx, qb.sy); ctx.stroke();
      }

      var pf = P[sp.from], pt = P[sp.to];
      var hx = pf.sx + (pt.sx - pf.sx) * sp.t, hy = pf.sy + (pt.sy - pf.sy) * sp.t;

      // segment déjà parcouru sur l'arête en cours
      ctx.strokeStyle = rgba(gold, dark ? 0.7 : 0.9); ctx.lineWidth = 1.6;
      ctx.beginPath(); ctx.moveTo(pf.sx, pf.sy); ctx.lineTo(hx, hy); ctx.stroke();

      // tête lumineuse + halo
      var gg = ctx.createRadialGradient(hx, hy, 0, hx, hy, 11);
      gg.addColorStop(0, rgba(dark ? [255, 244, 210] : [190, 140, 40], dark ? 0.95 : 1));
      gg.addColorStop(0.4, rgba(gold, dark ? 0.7 : 0.85));
      gg.addColorStop(1, rgba(gold, 0));
      ctx.fillStyle = gg;
      ctx.beginPath(); ctx.arc(hx, hy, 11, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = rgba(dark ? [255, 246, 214] : [120, 80, 0], 0.95);
      ctx.beginPath(); ctx.arc(hx, hy, 2, 0, Math.PI * 2); ctx.fill();
    }
  }

  /* ---- Boucle ----------------------------------------------------------- */
  function tick(ts) {
    if (!running) return;
    if (!tPrev) tPrev = ts;
    // Pendant que l'utilisateur scrolle, on ne dessine rien : le scroll garde
    // toutes les ressources → fluide. La sphère reprend dès qu'on s'arrête.
    if (scrolling) { tPrev = ts; raf = window.requestAnimationFrame(tick); return; }
    var dt = Math.min(0.05, (ts - tPrev) / 1000); tPrev = ts; clock += dt; lastDt = dt;

    energyTgt = scrollProgress();
    // easing (smoothstep) pour une montée douce
    var e = energyTgt * energyTgt * (3 - 2 * energyTgt);
    energy += (e - energy) * 0.08;
    zoomTgt = 1 + energy * 0.22;
    zoom += (zoomTgt - zoom) * 0.08;

    yawOff  += (yawTgt  - yawOff)  * 0.06;
    tiltOff += (tiltTgt - tiltOff) * 0.06;

    rotY += dt * (0.14 + energy * 0.55);   // tourne toujours sur elle-même
    rotX += dt * 0.03;

    draw();
    raf = window.requestAnimationFrame(tick);
  }

  var raf = null, running = false;
  function start() { if (running) return; running = true; tPrev = 0; raf = window.requestAnimationFrame(tick); }
  function stop()  { running = false; if (raf) window.cancelAnimationFrame(raf); raf = null; }

  /* ---- Entrées : souris + visibilité ----------------------------------- */
  if (!reduce) {
    window.addEventListener('pointermove', function (ev) {
      var rect = canvas.getBoundingClientRect();
      if (rect.bottom < 0 || rect.top > window.innerHeight) return;
      var nx = (ev.clientX - (rect.left + rect.width / 2)) / rect.width;
      var ny = (ev.clientY - (rect.top + rect.height / 2)) / rect.height;
      yawTgt  = nx * 0.6;
      tiltTgt = -ny * 0.4;
    }, { passive: true });

    document.addEventListener('visibilitychange', function () {
      if (document.hidden) stop(); else if (onScreen) start();
    });

    // Gèle le rendu du canvas tant que le scroll bouge (reprise à l'arrêt).
    window.addEventListener('scroll', function () {
      scrolling = true;
      if (scrollTO) window.clearTimeout(scrollTO);
      scrollTO = window.setTimeout(function () { scrolling = false; }, 140);
    }, { passive: true });
  }

  var onScreen = false, booted = false;
  function boot() {
    if (booted) return;
    booted = true;
    resize();
    if (reduce) { draw(); return; }   // une image fixe, pas de boucle
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        onScreen = entries[0].isIntersecting;
        if (onScreen && !document.hidden) start(); else stop();
      }, { rootMargin: '120px' }).observe(canvas);
    } else { onScreen = true; start(); }
  }

  var rzTimer = null;
  window.addEventListener('resize', function () {
    window.clearTimeout(rzTimer);
    rzTimer = window.setTimeout(function () { resize(); if (reduce) draw(); }, 200);
  }, { passive: true });

  // Changement de thème clair/sombre : on redessine tout de suite (utile quand
  // la boucle est en pause ou en reduced-motion).
  window.addEventListener('croisia:theme', function () { if (W && H) draw(); }, { passive: true });

  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(boot);
    window.setTimeout(boot, 1200);
  } else {
    boot();
  }
})();

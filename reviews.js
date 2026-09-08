/* ─────────────────────────────────────────────────────────────
   Schuiver voor surrontours.com (reviews en de fotostrip)

   Het vegen zelf doet de browser met scroll-snap; dit script zet
   alleen de bolletjes en pijlen aan als er echt iets te schuiven
   valt, houdt ze gelijk met waar je bent, en laat de kaarten
   vanzelf doorlopen tot iemand er zelf aan zit. Laadt het script
   niet, dan staan de reviews er nog steeds — dan schuif je ze
   gewoon met je vinger zonder bolletjes.
   ───────────────────────────────────────────────────────────── */
(function () {
// Reviewschuiver. Het vegen doet de browser zelf (scroll-snap); dit
// script zet alleen de bolletjes en pijlen aan als er iets te schuiven
// valt, en houdt ze gelijk met waar je bent.
document.querySelectorAll('[data-slider]').forEach(function (slider) {
  var spoor = slider.querySelector('.slider-track');
  var dots  = slider.querySelector('.slider-dots');
  var knop  = dots ? [].slice.call(dots.children) : [];
  var vorig = slider.querySelector('.slider-prev');
  var volgend = slider.querySelector('.slider-next');
  var kaarten = [].slice.call(spoor.querySelectorAll('[data-slide]'));
  var timer = null, aangeraakt = false;
  var rustig = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function schuifbaar() { return spoor.scrollWidth - spoor.clientWidth > 8; }

  function huidig() {
    var midden = spoor.scrollLeft + spoor.clientWidth / 2, beste = 0, kleinste = Infinity;
    kaarten.forEach(function (k, i) {
      var c = k.offsetLeft + k.offsetWidth / 2 - spoor.offsetLeft;
      var d = Math.abs(c - midden);
      if (d < kleinste) { kleinste = d; beste = i; }
    });
    return beste;
  }

  function teken() {
    var aan = schuifbaar();
    if (dots) dots.hidden = !aan;
    if (vorig) vorig.hidden = !aan;
    if (volgend) volgend.hidden = !aan;
    if (!aan) return;
    var n = huidig();
    knop.forEach(function (b, i) {
      b.classList.toggle('on', i === n);
      b.setAttribute('aria-current', i === n ? 'true' : 'false');
    });
    if (vorig) vorig.disabled = spoor.scrollLeft < 8;
    if (volgend) volgend.disabled = spoor.scrollLeft > spoor.scrollWidth - spoor.clientWidth - 8;
  }

  function naar(i) {
    var k = kaarten[Math.max(0, Math.min(kaarten.length - 1, i))];
    if (k) spoor.scrollTo({ left: k.offsetLeft - spoor.offsetLeft, behavior: rustig ? 'auto' : 'smooth' });
  }

  knop.forEach(function (b, i) {
    b.addEventListener('click', function () { stop(); naar(i); });
  });
  if (vorig) vorig.addEventListener('click', function () { stop(); naar(huidig() - 1); });
  if (volgend) volgend.addEventListener('click', function () { stop(); naar(huidig() + 1); });

  var bezig = false;
  spoor.addEventListener('scroll', function () {
    if (bezig) return;
    bezig = true;
    requestAnimationFrame(function () { bezig = false; teken(); });
  }, { passive: true });

  // Vanzelf doorlopen tot iemand er zelf aan zit; daarna nooit meer,
  // want niets is vervelender dan een pagina die onder je duim wegschuift.
  function stop() { aangeraakt = true; if (timer) { clearInterval(timer); timer = null; } }
  function start() {
    if (aangeraakt || rustig || timer || !schuifbaar() || kaarten.length < 2) return;
    timer = setInterval(function () {
      if (document.hidden) return;
      var n = huidig();
      naar(n >= kaarten.length - 1 ? 0 : n + 1);
    }, 6000);
  }
  ['pointerdown', 'touchstart', 'wheel', 'keydown'].forEach(function (e) {
    spoor.addEventListener(e, stop, { passive: true });
  });
  slider.addEventListener('mouseenter', function () { if (timer) { clearInterval(timer); timer = null; } });
  slider.addEventListener('mouseleave', start);

  window.addEventListener('resize', teken);
  teken();

  // Pas beginnen als het blok in beeld komt.
  // De tweede en derde foto staan buiten beeld en zouden pas laden als je
  // er al heen geveegd hebt. Zodra het blok in zicht komt halen we ze op,
  // anders veeg je naar een wit vlak.
  function fotosNu() {
    spoor.querySelectorAll('img[loading="lazy"]').forEach(function (i) { i.loading = 'eager'; });
  }
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (e) {
      if (e[0].isIntersecting) { fotosNu(); start(); }
      else if (timer) { clearInterval(timer); timer = null; }
    }, { threshold: 0.2 }).observe(slider);
  } else { fotosNu(); start(); }
});
})();

/* ─────────────────────────────────────────────────────────────
   Surron Tours Tarragona — Meta Pixel met toestemmingsvraag
   Pixel ID: 2038328800192468 (dataset "surrontarragona")

   De pixel laadt PAS nadat de bezoeker akkoord gaat. Dat is geen
   nettigheid maar de Spaanse/EU-cookiewet (AEPD handhaaft hierop).
   Weigert iemand, dan wordt er niets van Meta geladen.

   Gebruik per pagina:
     <script src="/pixel.js" data-event="ViewContent"></script>
     <script src="/pixel.js" data-event="Lead"></script>
   ───────────────────────────────────────────────────────────── */
(function () {
  var PIXEL_ID = '2038328800192468';
  var KEY = 'st_consent';

  var me = document.currentScript ||
           document.querySelector('script[src*="pixel.js"]');
  var extraEvent = me ? me.getAttribute('data-event') : null;

  var taal = (document.documentElement.lang || 'en').toLowerCase().slice(0, 2);

  var TEKSTEN = {
    es: {
      text: 'Cookies solo para ver qué anuncios funcionan.',
      yes: 'Aceptar', no: 'Rechazar'
    },
    ca: {
      text: 'Galetes només per veure quins anuncis funcionen.',
      yes: 'Acceptar', no: 'Rebutjar'
    },
    en: {
      text: 'Cookies only to see which ads work.',
      yes: 'Accept', no: 'Decline'
    }
  };
  var T = TEKSTEN[taal] || TEKSTEN.en;

  function loadPixel() {
    if (window.fbq) return;
    !function (f, b, e, v, n, t, s) {
      if (f.fbq) return; n = f.fbq = function () {
        n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments)
      };
      if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = '2.0';
      n.queue = []; t = b.createElement(e); t.async = !0; t.src = v;
      s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s)
    }(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');

    fbq('init', PIXEL_ID);
    fbq('track', 'PageView');
    if (extraEvent) fbq('track', extraEvent);
  }

  /* ── cookieloze teller ─────────────────────────────────────────
     De pixel laadt pas na toestemming. Wie de balk negeert en meteen
     op WhatsApp tikt levert dus géén enkel Meta-event op, terwijl dat
     juist je warmste bezoeker is. Deze teller telt die wel: geen
     cookie, geen opslag op het apparaat, geen identificatie — alleen
     een streepje op de server. Uitlezen in de Railway-logs.

     tel('balk')      de balk is getoond
     tel('ja')        toestemming gegeven
     tel('nee')       geweigerd
     tel('wa')        WhatsApp aangetikt mét toestemming
     tel('wa-zonder') WhatsApp aangetikt zónder toestemming  ← het lek  */
  function tel(soort) {
    try {
      var u = '/t?e=' + soort;
      if (navigator.sendBeacon) navigator.sendBeacon(u);
      else new Image().src = u + '&r=' + Math.random();
    } catch (e) {}
  }

  /* ── WhatsApp-klik = Contact ───────────────────────────────────
     Het gesprek zelf mag Meta niet zien; de klik ernaartoe wel, en
     wie klikt stuurt vrijwel altijd ook. Elke wa.me-knop op de site
     heeft target="_blank", dus de pagina blijft staan en de pixel
     krijgt gegarandeerd de tijd om af te vuren.

     De luisteraar hangt aan document en wordt meteen gezet, niet pas
     bij het laden van de pixel: zo maakt de volgorde niet uit. Eén
     Contact per bezoek — iemand die drie knoppen aanraakt is één
     geïnteresseerde, geen drie, en drie tellingen sturen Meta's
     optimalisatie de verkeerde kant op. */
  /* Twee losse merktekens: iemand die eerst zonder toestemming tikt en
     daarna alsnog accepteert, moet zijn Contact nog kunnen opleveren. */
  function eenmalig(sleutel) {
    try {
      if (sessionStorage.getItem(sleutel) === '1') return false;
      sessionStorage.setItem(sleutel, '1');
    } catch (e) {}
    return true;
  }

  function waLink(el) {
    /* geen element.closest() gebruiken: op een <svg> binnen de knop
       bestaat die in oudere Safari niet */
    while (el && el !== document) {
      if (el.tagName && el.tagName.toLowerCase() === 'a' &&
          (el.getAttribute('href') || '').indexOf('wa.me') !== -1) return el;
      el = el.parentNode;
    }
    return null;
  }

  document.addEventListener('click', function (e) {
    if (!waLink(e.target)) return;
    if (eenmalig('st_wa')) tel(window.fbq ? 'wa' : 'wa-zonder');
    if (window.fbq && eenmalig('st_contact')) {
      fbq('track', 'Contact', { content_name: 'whatsapp_button' });
    }
  }, true);

  function saveAndGo(value) {
    tel(value === 'yes' ? 'ja' : 'nee');
    try { localStorage.setItem(KEY, value); } catch (e) {}
    var bar = document.getElementById('st-consent');
    if (bar) bar.parentNode.removeChild(bar);
    document.body.style.paddingBottom = '';
    if (value === 'yes') loadPixel();
  }

  var stored = null;
  try { stored = localStorage.getItem(KEY); } catch (e) {}

  if (stored === 'yes') { loadPixel(); return; }
  if (stored === 'no') { return; }

  /* ── toestemmingsbalk ── */
  function build() {
    var css = document.createElement('style');
    css.textContent =
      '#st-consent{position:fixed;left:0;right:0;bottom:0;z-index:9999;background:rgba(12,12,12,.97);' +
      'backdrop-filter:blur(8px);border-top:1px solid rgba(255,255,255,.12);color:#e6e6e6;' +
      'font-family:"Open Sans",system-ui,sans-serif;font-size:14px;line-height:1.5;' +
      'padding:16px 20px;display:flex;gap:16px;align-items:center;justify-content:center;flex-wrap:wrap}' +
      '#st-consent p{margin:0;max-width:560px}' +
      '#st-consent button{font-family:"Montserrat",system-ui,sans-serif;font-weight:700;font-size:14px;' +
      'border:0;border-radius:6px;padding:11px 26px;cursor:pointer;transition:.2s}' +
      '#st-consent .y{background:#ff6b35;color:#fff}' +
      '#st-consent .y:hover{background:#e2551f}' +
      '#st-consent .n{background:transparent;color:#9a9a9a;border:1px solid rgba(255,255,255,.22)}' +
      '#st-consent .n:hover{color:#fff;border-color:rgba(255,255,255,.5)}' +
      /* Op een kleine telefoon stond de balk precies over de WhatsApp-knop
         in de hero. Daarom hier één regel, kleinere knoppen, en onderaan
         de pagina evenveel ruimte terug zodat er niets achter verdwijnt. */
      '@media(max-width:640px){#st-consent{gap:8px;padding:10px 12px;font-size:12.5px;' +
      'line-height:1.35;flex-wrap:nowrap;text-align:left}' +
      '#st-consent p{flex:1 1 auto;min-width:0}' +
      '#st-consent button{flex:0 0 auto;font-size:12.5px;padding:9px 14px;border-radius:5px}}';
    document.head.appendChild(css);

    var bar = document.createElement('div');
    bar.id = 'st-consent';

    var p = document.createElement('p');
    p.textContent = T.text;

    var yes = document.createElement('button');
    yes.className = 'y'; yes.textContent = T.yes;
    yes.onclick = function () { saveAndGo('yes'); };

    var no = document.createElement('button');
    no.className = 'n'; no.textContent = T.no;
    no.onclick = function () { saveAndGo('no'); };

    bar.appendChild(p); bar.appendChild(yes); bar.appendChild(no);
    document.body.appendChild(bar);
    tel('balk');

    /* De balk staat vast onderaan. Zonder deze ruimte ligt hij over de
       knop waar het hele bezoek om draait. */
    document.body.style.paddingBottom = bar.offsetHeight + 'px';
    window.addEventListener('resize', function () {
      if (document.getElementById('st-consent')) {
        document.body.style.paddingBottom = bar.offsetHeight + 'px';
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', build);
  } else {
    build();
  }
})();

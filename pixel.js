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
      text: 'Usamos cookies de medición para saber qué anuncios traen reservas. Nada más.',
      yes: 'Aceptar', no: 'Rechazar'
    },
    ca: {
      text: 'Fem servir galetes de mesura per saber quins anuncis porten reserves. Res més.',
      yes: 'Acceptar', no: 'Rebutjar'
    },
    en: {
      text: 'We use measurement cookies to see which ads bring bookings. Nothing else.',
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
  var CONTACT_KEY = 'st_contact';
  function alGeteld() {
    try { return sessionStorage.getItem(CONTACT_KEY) === '1'; } catch (e) { return false; }
  }
  function noteer() {
    try { sessionStorage.setItem(CONTACT_KEY, '1'); } catch (e) {}
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
    if (!window.fbq || alGeteld()) return;
    noteer();
    fbq('track', 'Contact', { content_name: 'whatsapp_button' });
  }, true);

  function saveAndGo(value) {
    try { localStorage.setItem(KEY, value); } catch (e) {}
    var bar = document.getElementById('st-consent');
    if (bar) bar.parentNode.removeChild(bar);
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
      '@media(max-width:640px){#st-consent{gap:10px;padding:14px 16px}#st-consent button{flex:1}}';
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
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', build);
  } else {
    build();
  }
})();

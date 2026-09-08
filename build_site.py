#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bouwt surrontours.com: per taal een korte landingspagina en een infopagina.

De landingspagina heeft één taak: iemand een bericht laten sturen. Daarom
staat er bewust weinig op. Alles wat je pas wilt weten nadat je
geïnteresseerd bent — leeftijden, kleding, betaling, regen, de moto —
staat op /info/. Wie het wil lezen klikt door; wie wil boeken hoeft dat
niet eerst door te ploegen.

De drie talen mikken op verschillende mensen: Engels op iemand die hier
op vakantie is, Spaans op iemand uit de regio die iets zoekt voor het
weekend, Catalaans op iemand die vlakbij woont.

Draaien:  python3 build_site.py
"""
import io
import json
import os
from urllib.parse import quote

from content_info import INFO

PIXEL_DOMEIN_VERIFICATIE = "gn4ay5faop5r913kbmelxx791i2kgo"
WA_NUMMER = "34657390564"
WA_WEERGAVE = "+34 657 390 564"
FORM_MAIL = "chimobous01@gmail.com"
BASIS = "https://surrontours.com"
CSS = "/style.css?v=7"

HIER = os.path.dirname(os.path.abspath(__file__))

# Catalaanse infoteksten: vertaald uit het Spaans, zie ca_info.json
_CA_MAP = json.load(io.open(os.path.join(HIER, "ca_info.json"), encoding="utf-8"))


def _vertaal(v):
    if isinstance(v, str):
        return _CA_MAP[v]
    if isinstance(v, tuple):
        return tuple(_vertaal(x) for x in v)
    if isinstance(v, list):
        return [_vertaal(x) for x in v]
    return v


INFO["ca"] = {k: _vertaal(v) for k, v in INFO["es"].items()}

# ──────────────────────────────────────────────────────────────────────
#  REVIEWS — echte klanten. Nooit aanvullen met verzonnen tekst.
# ──────────────────────────────────────────────────────────────────────
REVIEWS = [
    {
        "naam": "Miguel Guadalajara",
        "foto": "/img/rider-trio.jpg",
        "origineel": "es",
        "es": "Hoy hemos estado realizando un circuito con Surron Tours, de dos horas, "
              "con mi pareja y mi hijo de 14 años. Nos lo hemos pasado muy bien, todo "
              "súper bien organizado y las motos van súper bien para cualquier nivel. "
              "Lo repetiremos sin duda.",
        "en": "We did a two-hour circuit with Surron Tours today, with my partner and my "
              "14-year-old son. We had a brilliant time — everything superbly organised, "
              "and the bikes work really well for any level. We'll definitely do it again.",
        "ca": "Avui hem fet un circuit amb Surron Tours, de dues hores, amb la meva parella "
              "i el meu fill de 14 anys. Ens ho hem passat molt bé, tot súper ben organitzat "
              "i les motos van molt bé per a qualsevol nivell. Ho repetirem sens dubte.",
    },
    {
        "naam": "José Manuel Quero",
        "foto": "/img/rider-duo.jpg",
        "origineel": "es",
        "es": "Una aventura espectacular. Nada más llegar ya nos estaban esperando, con los "
              "cascos, los guantes y las motos. Hicimos una ruta bastante larga, las motos "
              "iban perfectas, como nuevas. Una flipada lo bien que van las Surron por la "
              "montaña. ¡Estoy seguro de que volveremos a vernos! ¡Gasssss!",
        "en": "A spectacular adventure. The moment we arrived they were waiting for us with "
              "the helmets, the gloves and the bikes. We did a pretty long route and the "
              "bikes were perfect, like new. It's unreal how well the Surrons go up the "
              "mountain. I'm sure we'll be seeing each other again!",
        "ca": "Una aventura espectacular. Just arribar ja ens estaven esperant, amb els cascos, "
              "els guants i les motos. Vam fer una ruta bastant llarga, les motos anaven "
              "perfectes, com noves. És una passada com van les Surron per la muntanya. "
              "Segur que ens tornarem a veure!",
    },
    {
        "naam": "Jill",
        "foto": "/img/rider-sunset.jpg",
        "origineel": "nl",
        "en": "I surprised my boyfriend with a two-hour tour today. He had no idea what we "
              "were doing and he loved it — finally a plan he won't forget. Not karting, "
              "not paintball, not dinner again. I'd recommend this to anyone.",
        "es": "Hoy sorprendí a mi novio con una ruta de dos horas. No tenía ni idea de lo que "
              "íbamos a hacer y le encantó — por fin un plan que no va a olvidar. Ni karts, "
              "ni paintball, ni otra vez a cenar. Se lo recomiendo a cualquiera.",
        "ca": "Avui vaig sorprendre el meu xicot amb una ruta de dues hores. No tenia ni idea "
              "del que faríem i li va encantar — per fi un pla que no oblidarà. Ni karts, ni "
              "paintball, ni tornar a sopar fora. Ho recomano a tothom.",
    },
]

VERTAALD_UIT = {
    "en": {"es": "Translated from Spanish", "nl": "Translated from Dutch"},
    "es": {"es": None, "nl": "Traducido del neerlandés"},
    "ca": {"es": "Traduït del castellà", "nl": "Traduït del neerlandès"},
}

# ──────────────────────────────────────────────────────────────────────
#  LANDINGSPAGINA PER TAAL
# ──────────────────────────────────────────────────────────────────────
T = {}

T["en"] = dict(
    code="en", pad="/", map="", info="/info/", dank="/thanks.html", locale="en_GB",
    titel="Surron Tours Tarragona | Ride an Electric Dirt Bike on 200 Private Hectares",
    meta="One hour on an electric dirt bike across 200 private hectares near Tarragona. "
         "No licence, no experience, all gear included. €100. Message us and we'll tell "
         "you which dates are free.",
    og_titel="The Best Hour of Your Holiday | Surron Tours Tarragona",
    og_meta="Ride an electric dirt bike across 200 private hectares near Tarragona. "
            "No licence needed. All gear included. From €100.",
    badge="Tarragona · Private Estate",
    h1_1="The Day You'll", h1_2="Actually Remember.",
    lead="One hour on an electric dirt bike across 200 private hectares of vineyard and "
         "pine forest, with a guide the whole way. No licence. No experience. €100.",
    cta_wa="Ask which dates are free",
    cta_form="Or send the form",
    trust=["No licence required", "Beginners from 12", "All gear included", "100% private land"],
    feiten=[("€100", "per person"), ("1 or 2 h", "riding time"),
            ("200 ha", "private estate"), ("0", "licence needed")],

    kort_label="In Thirty Seconds",
    kort_h="Here's the whole thing.",
    kort=[
        ("What it is",
         "One hour, one electric dirt bike each, across 200 private hectares of vineyard "
         "and pine forest. A guide rides with you the whole way."),
        ("What you need",
         "Nothing. No licence, no experience, no kit — helmet, body armour, gloves and the "
         "bike are all here waiting. From 12 years old."),
        ("What it costs",
         "€100 for one hour, €175 for two. Everything included. You pay on the day and can "
         "cancel free up to 24 hours before."),
    ],
    kort_meer="Ages, what to wear, how it works, what if it rains —",
    kort_meer_link="read every detail →",

    rev_label="Riders",
    rev_h="What people say after.",
    rev_intro="Three people who rode with us, in their own words.",

    book_label="Two Minutes",
    book_h="Send us a message.",
    book_intro="Tell us roughly when you'd like to come and how many of you there are. "
               "We'll come straight back with the dates that are free. Nothing to pay, "
               "nothing to commit to.",
    wa_cta="Message us on WhatsApp",
    wa_note="Fastest way — we usually reply within minutes.",
    wa_of="or leave your number here",
    wa_txt="Hi! Which dates do you have free for the Surron ride?",
    wa_vraag="Hi! I have a question about the Surron ride.",
    f_naam="Your name", f_naam_ph="Alex",
    f_tel="WhatsApp number", f_tel_ph="+34 600 000 000",
    f_aantal="How many of you", f_wanneer="Roughly when",
    f_wanneer_ph="Next weekend, or a weekday evening",
    f_send="Send — and we'll reply with the free dates",
    f_klein="No payment, no obligation. We just reply with what's open.",
    book_vraag="Rather ask something first?",
    form_subject="🏍️ New Surron Tour enquiry (EN)",
    form_taal="English",

    foot_over="Guided electric dirt bike tours on a private 200-hectare organic estate in "
              "the Tarragona countryside, Catalonia, Spain.",
    foot_k1="More", foot_info="Everything you need to know",
    foot_k2="Bookings", foot_boek="Send a message →",
    foot_note="We reply to every message personally to confirm your date.",
    foot_talen="English · Español · Català · Nederlands",
    foot_bottom="© 2026 Surron Tours Tarragona · Riding takes place on private property · "
                "No driving licence required",
    ld_beschrijving="Guided electric dirt bike tours on a private 200-hectare estate near "
                    "Tarragona, Spain. Ride a Surron Light Bee through vineyards, forest and "
                    "off-road terrain. No driving licence required. All safety gear included.",
    ld_aanbod="Guided 1-hour ride on a Surron Light Bee",
)

T["es"] = dict(
    code="es", pad="/es/", map="es", info="/es/info/", dank="/es/gracias.html", locale="es_ES",
    titel="Surron Tours Tarragona | Moto eléctrica por 200 hectáreas privadas",
    meta="Una hora en moto eléctrica por 200 hectáreas privadas cerca de Tarragona. Sin "
         "carnet, sin experiencia, equipo incluido. 100 €. Escríbenos y te decimos qué "
         "días quedan libres.",
    og_titel="Un plan que no se olvida | Surron Tours Tarragona",
    og_meta="Conduce una moto eléctrica por 200 hectáreas privadas cerca de Tarragona. "
            "Sin carnet. Equipo incluido. Desde 100 €.",
    badge="Tarragona · Finca privada",
    h1_1="Un Plan Que", h1_2="No Se Olvida.",
    lead="Una hora conduciendo tú mismo una moto eléctrica por 200 hectáreas privadas de "
         "viñedo y pinar, con guía todo el rato. Sin carnet. Sin experiencia. 100 €.",
    cta_wa="Pregunta qué días quedan libres",
    cta_form="O rellena el formulario",
    trust=["Sin carnet", "Desde los 12 años", "Equipo incluido", "Terreno 100 % privado"],
    feiten=[("100 €", "por persona"), ("1 o 2 h", "conduciendo"),
            ("200 ha", "finca privada"), ("0", "carnet necesario")],

    kort_label="En treinta segundos",
    kort_h="Esto es todo.",
    kort=[
        ("Qué es",
         "Una hora, una moto eléctrica para cada uno, por 200 hectáreas privadas de viñedo "
         "y pinar. Un guía va contigo todo el rato."),
        ("Qué necesitas",
         "Nada. Ni carnet, ni experiencia, ni equipo — casco, peto, guantes y la moto ya "
         "están aquí esperándote. Desde los 12 años."),
        ("Cuánto cuesta",
         "100 € una hora, 175 € dos horas. Todo incluido. Se paga el mismo día y puedes "
         "cancelar gratis hasta 24 horas antes."),
    ],
    kort_meer="Edades, qué ponerte, cómo va, qué pasa si llueve —",
    kort_meer_link="léelo todo aquí →",

    rev_label="Quien ya ha venido",
    rev_h="Lo que dicen después.",
    rev_intro="Tres personas que han rodado con nosotros, con sus propias palabras.",

    book_label="Dos minutos",
    book_h="Escríbenos.",
    book_intro="Dinos más o menos cuándo te iría bien y cuántos sois. Te contestamos con "
               "los días que quedan libres. Sin pagar nada y sin compromiso.",
    wa_cta="Escríbenos por WhatsApp",
    wa_note="Lo más rápido — solemos contestar en minutos.",
    wa_of="o déjanos tu número aquí",
    wa_txt="¡Hola! ¿Qué días tenéis libres para la ruta en Surron?",
    wa_vraag="¡Hola! Tengo una duda sobre la ruta en Surron.",
    f_naam="Tu nombre", f_naam_ph="Marc",
    f_tel="Número de WhatsApp", f_tel_ph="+34 600 000 000",
    f_aantal="Cuántos sois", f_wanneer="Más o menos cuándo",
    f_wanneer_ph="El finde que viene, o entre semana",
    f_send="Enviar — y te decimos qué días quedan",
    f_klein="Sin pagar nada y sin compromiso. Solo te contestamos con lo que queda libre.",
    book_vraag="¿Prefieres preguntar antes?",
    form_subject="🏍️ Nueva consulta Surron Tours (ES)",
    form_taal="Español",

    foot_over="Rutas guiadas en moto eléctrica por una finca ecológica privada de 200 "
              "hectáreas en el campo de Tarragona, Cataluña.",
    foot_k1="Más", foot_info="Todo lo que necesitas saber",
    foot_k2="Reservas", foot_boek="Escribir un mensaje →",
    foot_note="Contestamos todos los mensajes personalmente para confirmar tu día.",
    foot_talen="Español · Català · English · Nederlands",
    foot_bottom="© 2026 Surron Tours Tarragona · La actividad se realiza en propiedad "
                "privada · No se necesita carnet de conducir",
    ld_beschrijving="Rutas guiadas en moto eléctrica por una finca privada de 200 hectáreas "
                    "en Tarragona. Conduce una Surron Light Bee entre viñedos, bosque y "
                    "terreno off-road. Sin carnet de conducir. Equipo de protección incluido.",
    ld_aanbod="Ruta guiada de 1 hora en Surron Light Bee",
)

T["ca"] = dict(
    code="ca", pad="/ca/", map="ca", info="/ca/info/", dank="/ca/gracies.html", locale="ca_ES",
    titel="Surron Tours Tarragona | Moto elèctrica per 200 hectàrees privades",
    meta="Una hora en moto elèctrica per 200 hectàrees privades al camp de Tarragona. "
         "Sense carnet, sense experiència, equip inclòs. 100 €. Escriu-nos i et diem "
         "quins dies queden lliures.",
    og_titel="Ho tens aquí mateix | Surron Tours Tarragona",
    og_meta="Condueix una moto elèctrica per 200 hectàrees privades al camp de Tarragona. "
            "Sense carnet. Equip inclòs. Des de 100 €.",
    badge="Tarragona · Finca privada",
    h1_1="Ho Tens Aquí.", h1_2="I No Ho Sabies.",
    lead="Una hora conduint tu mateix una moto elèctrica per 200 hectàrees privades de "
         "vinya i pinede, amb guia tota l'estona. Sense carnet. Sense experiència. 100 €.",
    cta_wa="Pregunta quins dies queden lliures",
    cta_form="O omple el formulari",
    trust=["Sense carnet", "A partir dels 12 anys", "Equip inclòs", "Terreny 100 % privat"],
    feiten=[("100 €", "per persona"), ("1 o 2 h", "conduint"),
            ("200 ha", "finca privada"), ("0", "carnet necessari")],

    kort_label="En trenta segons",
    kort_h="Això és tot.",
    kort=[
        ("Què és",
         "Una hora, una moto elèctrica per a cadascú, per 200 hectàrees privades de vinya i "
         "pinede. Un guia va amb tu tota l'estona."),
        ("Què necessites",
         "Res. Ni carnet, ni experiència, ni equip — casc, pitrera, guants i la moto ja són "
         "aquí esperant-te. A partir dels 12 anys."),
        ("Quant costa",
         "100 € una hora, 175 € dues hores. Tot inclòs. Es paga el mateix dia i pots "
         "anul·lar gratis fins a 24 hores abans."),
    ],
    kort_meer="Edats, què posar-te, com va, què passa si plou —",
    kort_meer_link="llegeix-ho tot aquí →",

    rev_label="Qui ja ha vingut",
    rev_h="El que diuen després.",
    rev_intro="Tres persones que han rodat amb nosaltres, amb les seves pròpies paraules.",

    book_label="Dos minuts",
    book_h="Escriu-nos.",
    book_intro="Digues-nos més o menys quan et aniria bé i quants sou. Et contestem amb els "
               "dies que queden lliures. Sense pagar res i sense compromís.",
    wa_cta="Escriu-nos per WhatsApp",
    wa_note="El més ràpid — solem contestar en minuts.",
    wa_of="o deixa'ns el teu número aquí",
    wa_txt="Hola! Quins dies teniu lliures per a la ruta en Surron?",
    wa_vraag="Hola! Tinc un dubte sobre la ruta en Surron.",
    f_naam="El teu nom", f_naam_ph="Marc",
    f_tel="Número de WhatsApp", f_tel_ph="+34 600 000 000",
    f_aantal="Quants sou", f_wanneer="Més o menys quan",
    f_wanneer_ph="El cap de setmana vinent, o entre setmana",
    f_send="Enviar — i et diem quins dies queden",
    f_klein="Sense pagar res i sense compromís. Només et contestem amb el que queda lliure.",
    book_vraag="Prefereixes preguntar abans?",
    form_subject="🏍️ Nova consulta Surron Tours (CA)",
    form_taal="Català",

    foot_over="Rutes guiades en moto elèctrica per una finca ecològica privada de 200 "
              "hectàrees al camp de Tarragona, Catalunya.",
    foot_k1="Més", foot_info="Tot el que necessites saber",
    foot_k2="Reserves", foot_boek="Escriure un missatge →",
    foot_note="Contestem tots els missatges personalment per confirmar el teu dia.",
    foot_talen="Català · Español · English · Nederlands",
    foot_bottom="© 2026 Surron Tours Tarragona · L'activitat es fa en propietat privada · "
                "No cal carnet de conduir",
    ld_beschrijving="Rutes guiades en moto elèctrica per una finca privada de 200 hectàrees "
                    "al camp de Tarragona. Condueix una Surron Light Bee entre vinyes, bosc "
                    "i terreny off-road. Sense carnet de conduir. Equip de protecció inclòs.",
    ld_aanbod="Ruta guiada d'1 hora en Surron Light Bee",
)

WA_SVG = ('<svg viewBox="0 0 24 24" width="{w}" height="{w}" aria-hidden="true"><path '
          'fill="currentColor" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471'
          '-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255'
          '-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134'
          '-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075'
          '-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 '
          '0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 '
          '3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 '
          '1.872.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124'
          '-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741'
          '.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884a'
          '9.82 9.82 0 0 1 6.988 2.896 9.83 9.83 0 0 1 2.893 6.994c-.003 5.45-4.437 9.885-9.885 '
          '9.885M20.52 3.449C18.24 1.245 15.24 0 12.045 0 5.463 0 .104 5.334.101 11.893c0 2.096'
          '.549 4.142 1.595 5.945L0 24l6.305-1.654a11.9 11.9 0 0 0 5.683 1.448h.005c6.582 0 '
          '11.94-5.335 11.943-11.893a11.8 11.8 0 0 0-3.416-8.402"/></svg>')

FAVICON = ("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>"
           "<rect width='100' height='100' rx='22' fill='%230f0f0f'/><text y='72' x='50' "
           "font-size='60' text-anchor='middle' fill='%23ff6b35' font-family='Arial,sans-serif' "
           "font-weight='bold'>S</text></svg>")

REDIRECT = """// Wie in het Catalaans of Spaans browst, sturen we één keer door naar
// die versie. ?lang=en zet dat voorgoed uit, en zoekmachines nooit.
(function () {
  try {
    var p = new URLSearchParams(location.search);
    if (p.get('lang') === 'en') return;
    if (document.referrer.indexOf(location.host) !== -1) return;
    var l = (navigator.languages || [navigator.language || '']).join(',').toLowerCase();
    if (/\\bca\\b|ca-/.test(l)) location.replace('/ca/');
    else if (/\\bes\\b|es-/.test(l)) location.replace('/es/');
  } catch (e) {}
})();
"""


def wa_url(tekst):
    return f"https://wa.me/{WA_NUMMER}?text={quote(tekst)}"


def taalbalk(actief, achtervoegsel=""):
    def knop(code, href, label):
        cls = ' class="on"' if code == actief else ''
        return f'<a href="{href}"{cls} hreflang="{code}">{label}</a>'
    return ('<span class="lang">' + knop('en', '/' + achtervoegsel, 'EN')
            + knop('es', '/es/' + achtervoegsel, 'ES')
            + knop('ca', '/ca/' + achtervoegsel, 'CA') + '</span>')


def kop(c, titel, meta, url, extra_alt="", robots=""):
    """Gedeelde <head>. Eén plek, zodat pixel en verificatie nooit ontbreken."""
    return f'''<!DOCTYPE html>
<html lang="{c["code"]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="facebook-domain-verification" content="{PIXEL_DOMEIN_VERIFICATIE}">
{robots}
<title>{titel}</title>
<meta name="description" content="{meta}">
<meta name="theme-color" content="#0f0f0f">
<link rel="canonical" href="{url}">
{extra_alt}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Surron Tours Tarragona">
<meta property="og:title" content="{c["og_titel"]}">
<meta property="og:description" content="{c["og_meta"]}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASIS}/img/hero-vineyard-action.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="896">
<meta property="og:locale" content="{c["locale"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{c["og_titel"]}">
<meta name="twitter:description" content="{c["og_meta"]}">
<meta name="twitter:image" content="{BASIS}/img/hero-vineyard-action.jpg">

<link rel="icon" href="{FAVICON}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800;900&family=Open+Sans:wght@400;600;700&display=swap" rel="stylesheet">

<link rel="stylesheet" href="{CSS}">
</head>
<body>
'''


def voettekst(c, op_info=False):
    info_regel = ('' if op_info else
                  f'        <a href="{c["info"]}">{c["foot_info"]}</a>\n')
    return f'''
<footer>
  <div class="container">
    <div class="foot-grid">
      <div>
        <a href="{c["pad"]}" class="logo">SURRON <span>TOURS</span><small>Tarragona</small></a>
        <p>{c["foot_over"]}</p>
      </div>
      <div class="foot">
        <h4>{c["foot_k1"]}</h4>
{info_regel}        <a href="{c["pad"]}#book">{c["foot_boek"]}</a>
      </div>
      <div class="foot">
        <h4>{c["foot_k2"]}</h4>
        <a class="wa-foot" href="{wa_url(c["wa_txt"])}" target="_blank" rel="noopener">WhatsApp {WA_WEERGAVE}</a>
        <p style="margin-top:12px">{c["foot_note"]}</p>
        <p style="margin-top:12px">{c["foot_talen"]}</p>
        <p style="margin-top:12px">Tarragona, Catalunya · Espanya</p>
      </div>
    </div>
    <div class="foot-bottom">{c["foot_bottom"]}</div>
  </div>
</footer>
'''


SCRIPTS = """
<script>
{redirect}
// FAQ
document.querySelectorAll('.faq-q').forEach(function (q) {{
  q.addEventListener('click', function () {{
    var item = q.parentElement;
    var wasOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item').forEach(function (i) {{ i.classList.remove('open'); }});
    if (!wasOpen) item.classList.add('open');
  }});
}});
</script>

<script src="/pixel.js" data-event="{event}"></script>
</body>
</html>
"""


def reviewblok(taal):
    kaarten = []
    for r in REVIEWS:
        bron = VERTAALD_UIT[taal].get(r["origineel"])
        noot = f'<div class="rev-src">{bron}</div>' if bron else ''
        kaarten.append(f'''      <figure class="rev">
        <img src="{r["foto"]}" alt="{r["naam"]}" loading="lazy" width="900" height="900">
        <blockquote>
          <div class="rev-stars">★★★★★</div>
          <p>{r[taal]}</p>
        </blockquote>
        <figcaption>{r["naam"]}{noot}</figcaption>
      </figure>''')
    return "\n".join(kaarten)


# ══════════════════════════════════════════════════════════════════════
#  LANDINGSPAGINA
# ══════════════════════════════════════════════════════════════════════
def bouw_landing(taal):
    c = T[taal]
    url = BASIS + c["pad"]
    alt = (f'<link rel="alternate" hreflang="en" href="{BASIS}/">\n'
           f'<link rel="alternate" hreflang="es" href="{BASIS}/es/">\n'
           f'<link rel="alternate" hreflang="ca" href="{BASIS}/ca/">\n'
           f'<link rel="alternate" hreflang="x-default" href="{BASIS}/">')

    trust = "".join(f"<span>{x}</span>" for x in c["trust"])
    feiten = "".join(f'<div class="fact"><b>{a}</b><span>{b}</span></div>'
                     for a, b in c["feiten"])
    kort = "\n".join(f'''      <div class="kort-card">
        <h3>{t}</h3>
        <p>{p}</p>
      </div>''' for t, p in c["kort"])

    ld = json.dumps({
        "@context": "https://schema.org", "@type": "TouristAttraction",
        "name": "Surron Tours Tarragona", "description": c["ld_beschrijving"],
        "url": url, "image": BASIS + "/img/hero-vineyard-action.jpg",
        "address": {"@type": "PostalAddress", "addressRegion": "Tarragona",
                    "addressCountry": "ES"},
        "isAccessibleForFree": False,
        "availableLanguage": ["Spanish", "Catalan", "English", "Dutch"],
        "makesOffer": {"@type": "Offer", "name": c["ld_aanbod"], "price": "100",
                       "priceCurrency": "EUR",
                       "availability": "https://schema.org/InStock"},
    }, ensure_ascii=False, indent=2)

    return kop(c, c["titel"], c["meta"], url, alt) + f'''
<script type="application/ld+json">
{ld}
</script>

<header>
  <div class="nav-wrap">
    <a href="{c["pad"]}" class="logo">SURRON <span>TOURS</span><small>Tarragona</small></a>
    <a href="{wa_url(c["wa_txt"])}" class="btn btn-sm hdr-wa" target="_blank" rel="noopener">
      {WA_SVG.format(w=17)} WhatsApp
    </a>
    {taalbalk(taal)}
  </div>
</header>

<section class="hero" id="top">
  <div class="hero-inner">
    <div class="hero-badge">{c["badge"]}</div>
    <h1>{c["h1_1"]}<br><em>{c["h1_2"]}</em></h1>
    <p class="lead">{c["lead"]}</p>
    <div class="hero-cta">
      <a href="{wa_url(c["wa_txt"])}" class="btn btn-lg btn-wa" target="_blank" rel="noopener">
        {WA_SVG.format(w=22)} {c["cta_wa"]}
      </a>
      <a href="#book" class="btn btn-lg btn-ghost">{c["cta_form"]}</a>
    </div>
    <div class="hero-trust">{trust}</div>
  </div>
</section>

<section class="factbar" style="padding:0">
  <div class="factbar-grid">{feiten}</div>
</section>

<section class="kort">
  <div class="container">
    <div class="section-label">{c["kort_label"]}</div>
    <h2 class="section-title">{c["kort_h"]}</h2>
    <div class="kort-grid">
{kort}
    </div>
    <p class="kort-meer">{c["kort_meer"]} <a href="{c["info"]}">{c["kort_meer_link"]}</a></p>
  </div>
</section>

<section class="reviews" id="reviews">
  <div class="container">
    <div class="section-label">{c["rev_label"]}</div>
    <h2 class="section-title">{c["rev_h"]}</h2>
    <p class="section-intro">{c["rev_intro"]}</p>
    <div class="rev-grid">
{reviewblok(taal)}
    </div>
  </div>
</section>

<section class="book" id="book">
  <div class="container">
    <div class="section-label">{c["book_label"]}</div>
    <h2 class="section-title">{c["book_h"]}</h2>
    <p class="section-intro">{c["book_intro"]}</p>

    <div class="book-wrap">
      <div class="wa-lead">
        <a class="wa-cta" href="{wa_url(c["wa_txt"])}" target="_blank" rel="noopener">
          {WA_SVG.format(w=26)}
          {c["wa_cta"]}
        </a>
        <p class="wa-note">{c["wa_note"]}</p>
        <div class="wa-or"><span>{c["wa_of"]}</span></div>
      </div>

      <form action="https://formsubmit.co/{FORM_MAIL}" method="POST">
        <input type="hidden" name="_subject" value="{c["form_subject"]}">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="Language" value="{c["form_taal"]}">
        <input type="hidden" name="_next" value="{BASIS}{c["dank"]}">
        <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off">

        <div class="frow">
          <div class="field">
            <label for="name">{c["f_naam"]}</label>
            <input id="name" type="text" name="Name" required placeholder="{c["f_naam_ph"]}">
          </div>
          <div class="field">
            <label for="phone">{c["f_tel"]}</label>
            <input id="phone" type="tel" name="WhatsApp" required placeholder="{c["f_tel_ph"]}">
          </div>
        </div>

        <div class="frow">
          <div class="field">
            <label for="people">{c["f_aantal"]}</label>
            <select id="people" name="Riders">
              <option>1</option><option>2</option><option>3</option>
              <option>4</option><option>5</option><option>6+</option>
            </select>
          </div>
          <div class="field field-wide">
            <label for="when">{c["f_wanneer"]}</label>
            <input id="when" type="text" name="When" placeholder="{c["f_wanneer_ph"]}">
          </div>
        </div>

        <button type="submit" class="btn btn-lg">{c["f_send"]}</button>
        <p class="form-klein">{c["f_klein"]}</p>
      </form>

      <div class="book-alt">
        <div class="wa-alt">
          <span>{c["book_vraag"]}</span>
          <a class="wa-btn" href="{wa_url(c["wa_vraag"])}" target="_blank" rel="noopener">
            {WA_SVG.format(w=20)}
            WhatsApp {WA_WEERGAVE}
          </a>
        </div>
      </div>
    </div>
  </div>
</section>
''' + voettekst(c) + SCRIPTS.format(
        redirect=REDIRECT if taal == "en" else "", event="ViewContent")


# ══════════════════════════════════════════════════════════════════════
#  INFOPAGINA
# ══════════════════════════════════════════════════════════════════════
def bouw_info(taal):
    c = T[taal]
    i = INFO[taal]
    url = BASIS + c["info"]
    alt = (f'<link rel="alternate" hreflang="en" href="{BASIS}/info/">\n'
           f'<link rel="alternate" hreflang="es" href="{BASIS}/es/info/">\n'
           f'<link rel="alternate" hreflang="ca" href="{BASIS}/ca/info/">\n'
           f'<link rel="alternate" hreflang="x-default" href="{BASIS}/info/">')

    kaarten = "\n".join(f'''      <div class="know-card">
        <h3>{t}</h3>
        <ul>
{chr(10).join(f"          <li>{x}</li>" for x in punten)}
        </ul>
      </div>''' for t, punten in i["kaarten"])

    incl = "\n          ".join(f"<li>{x}</li>" for x in i["incl"])

    faq = "\n".join(f'''      <div class="faq-item">
        <button class="faq-q">{v} <span class="tog">+</span></button>
        <div class="faq-a"><div>{a}</div></div>
      </div>''' for v, a in i["faq"])

    return kop(c, i["titel"], i["meta"], url, alt) + f'''
<header>
  <div class="nav-wrap">
    <a href="{c["pad"]}" class="logo">SURRON <span>TOURS</span><small>Tarragona</small></a>
    <a href="{wa_url(c["wa_txt"])}" class="btn btn-sm hdr-wa" target="_blank" rel="noopener">
      {WA_SVG.format(w=17)} WhatsApp
    </a>
    {taalbalk(taal, "info/")}
  </div>
</header>

<section class="info-top">
  <div class="container">
    <a href="{c["pad"]}" class="terug">{i["terug"]}</a>
    <h1>{i["h1"]}</h1>
    <p class="section-intro" style="margin-left:0;text-align:left">{i["intro"]}</p>
  </div>
</section>

<section class="feel">
  <div class="container">
    <div class="split">
      <div class="split-img"><img src="/img/feel-sunset.jpg" alt="{i["feel_alt"]}" loading="lazy" width="1600" height="1000"></div>
      <div>
        <h2 style="font-size:28px">{i["feel_h"]}</h2>
        <p>{i["feel_p1"]}</p>
        <p>{i["feel_p2"]}</p>
        <p>{i["feel_p3"]}</p>
      </div>
    </div>

    <div class="split rev-split">
      <div class="split-img"><img src="/img/surron-light-bee.jpg" alt="{i["bike_alt"]}" loading="lazy"></div>
      <div>
        <h2 style="font-size:28px">{i["bike_h"]}</h2>
        <p>{i["bike_p"]}</p>
      </div>
    </div>
  </div>
</section>

<section class="know">
  <div class="container">
    <div class="know-grid">
{kaarten}
    </div>

    <div class="incl-wrap">
      <div class="incl-title">{i["incl_t"]}</div>
      <ul class="incl">
          {incl}
      </ul>
    </div>
  </div>
</section>

<section class="faq" id="faq">
  <div class="container">
    <h2 class="section-title">{i["faq_h"]}</h2>
    <div class="faq-list">
{faq}
    </div>
  </div>
</section>

<section class="book">
  <div class="container" style="text-align:center">
    <h2 class="section-title">{i["cta_h"]}</h2>
    <p class="section-intro">{i["cta_p"]}</p>
    <a class="wa-cta" style="max-width:420px;margin:0 auto" href="{wa_url(c["wa_vraag"])}" target="_blank" rel="noopener">
      {WA_SVG.format(w=26)}
      {c["wa_cta"]}
    </a>
    <p style="margin-top:26px"><a href="{c["pad"]}#book" class="btn btn-ghost">{c["cta_form"]}</a></p>
  </div>
</section>
''' + voettekst(c, op_info=True) + SCRIPTS.format(redirect="", event="ViewContent")


def schrijf(pad_delen, html):
    pad = os.path.join(HIER, *pad_delen)
    os.makedirs(os.path.dirname(pad), exist_ok=True)
    io.open(pad, "w", encoding="utf-8").write(html)
    print(f"  {'/'.join(pad_delen):26} {len(html) // 1024} kB")


if __name__ == "__main__":
    print("landingspagina's:")
    for taal in ("en", "es", "ca"):
        m = T[taal]["map"]
        schrijf(([m] if m else []) + ["index.html"], bouw_landing(taal))
    print("infopagina's:")
    for taal in ("en", "es", "ca"):
        m = T[taal]["map"]
        schrijf(([m] if m else []) + ["info", "index.html"], bouw_info(taal))

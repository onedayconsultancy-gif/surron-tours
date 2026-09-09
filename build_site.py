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
CSS = "/style.css?v=19"
PIXEL = "/pixel.js?v=2"
VID = "?v=2"             # ophogen bij een nieuwe film, anders blijft de oude 30 dagen in de cache

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
         "No licence, no experience, all gear included. From €175. Message us and we'll tell "
         "you which dates are free.",
    og_titel="The Best Hour of Your Holiday | Surron Tours Tarragona",
    og_meta="Ride an electric dirt bike across 200 private hectares near Tarragona. "
            "No licence needed. All gear included. From €175.",
    badge="The only Surron tours in Catalonia",
    h1_1="The Day You'll", h1_2="Actually Remember.",
    lead="Two hours on an electric dirt bike across 200 private hectares of vineyard and "
         "pine forest, with a guide the whole way. One hour from Barcelona. No licence. "
         "No experience. No road.",
    cta_wa="Ask which dates are free",
    cta_form="Or send the form",
    cta_noot="Usually answered within the hour.",
    trust=["From €175 p.p.", "No minimum group", "Ages 12+", "No licence needed"],
    feiten=[("€175", "per person, two hours"), ("€100", "per person, one hour"),
            ("200 ha", "private estate"), ("0", "licence needed")],

    video_alt="Eleven seconds on the estate at sunset — riders on the track, the vineyards, the valley.",
    video_nudge="Put the sound on.",
    video_aan="Sound on",
    video_uit="Sound off",
    beeld_h="What it looks like out there.",
    fotos=[
      ("fleet-three.jpg",
       "Three Surron Light Bee electric dirt bikes lined up on red earth, vines and pine forest behind",
       "One bike each"),
      ("feel-trail.jpg",
       "Two riders stopped on a trail through the scrub on the private estate near Tarragona",
       "On the trail"),
      ("vineyard-track.jpg",
       "Two electric dirt bikes on a red earth track running between the vines",
       "Through the vines"),
      ("track-clouds.jpg",
       "Two electric dirt bikes on an open red track with wooded hills behind",
       "Open track"),
      ("valley-bikes.jpg",
       "Two electric dirt bikes in dry grass with the valley and the pines behind",
       "The valley below"),
    ],

    afstand_h="Getting here.",
    afstand=[("Barcelona", "1 hour"), ("Tarragona", "30 min"),
             ("Reus", "40 min"), ("Salou", "40 min")],
    afstand_noot="Free parking on site. No car? Tell us where you are staying and we'll "
                 "arrange a pickup — it costs extra on top of the ride, and we'll tell you "
                 "what it would be before you commit to anything.",
    afstand_talen="Your guide speaks English, Español, Català and Nederlands.",

    niveau_h="And if you can already ride?",
    niveau="We pick the route to match the group, so the trails get harder if you want "
           "them to. Easy tracks between the vines for a first time; broken ground, climbs "
           "and tight rock for people who know what they are doing. Tell us what you have "
           "ridden before and we'll take you somewhere that isn't boring.",

    pitch_label="Why Bother",
    pitch_h="In Barcelona, looking for a day that isn't the beach again?",
    pitch=[
      "You have done the beach. You have done the tapas walk and the rooftop and the "
      "Sagrada Família queue. Karting, paintball, escape room — you already know how "
      "that afternoon ends, and in a month you will not be telling anyone about it.",
      "This is an hour out of the city, on a mountain with nobody else on it, on an "
      "electric dirt bike that you drive yourself. No licence. No experience. Five "
      "minutes in you are not following a guide at walking pace — you are riding.",
      "It is the bit of the trip people ask you to tell twice.",
    ],
    kort_label="In Thirty Seconds",
    kort_h="Here's the whole thing.",
    kort=[
        ("What it is",
         "One hour, one electric dirt bike each, across 200 private hectares of vineyard "
         "and pine forest. A guide rides with you the whole way, and you ride with your "
         "own group only — never with strangers."),
        ("What you need",
         "Nothing. No licence, no experience, no kit — helmet, body armour, gloves and the "
         "bike are all here waiting. From 12 years old."),
        ("What it costs",
         "€100 per person for one hour, €175 for two — the two-hour ride is the one both "
         "reviews below "
         "are talking about. Everything included. You pay on the day and can cancel free up "
         "to 24 hours before."),
    ],
    prakt_h="Before you ask.",
    prakt=[
      ("Where", "A private estate in the Tarragona countryside. About an hour from "
                "Barcelona, half an hour from Tarragona. You get the exact address and "
                "directions once your date is confirmed. Parking on site."),
      ("No car?", "We can come and pick you up. It costs extra and adds a bit of travel "
                  "time, so tell us where you are staying and we'll tell you what it "
                  "would be."),
      ("When", "Seven days a week, and we build the time around you — including at sunset, "
               "which is when it looks like the photos. Tell us your day and roughly what "
               "time. Fifteen minutes late is no problem, just message us."),
      ("How long", "One hour riding, or two. Allow about half an hour on top for the "
                   "briefing, kitting up and a few practice laps."),
      ("Age", "From 12. Under 15s ride with a parent or guardian there on the day."),
      ("Who you ride with", "Only your own group. We never put you together with people "
                            "you don't know — the slot is yours, whether you come on your "
                            "own or with five friends. For bigger groups we bring in extra "
                            "bikes, so tell us your numbers in advance. Anyone who would "
                            "rather not ride is welcome to come along and watch."),
      ("What to wear", "Closed shoes and long trousers. Helmet, body armour, knee and "
                       "elbow pads and gloves are ours and included."),
      ("Paying", "€50 holds your date; the rest in cash on the day. Free cancellation up "
                 "to 24 hours before, and you get the €50 back."),
      ("Languages", "English, Español, Català, Nederlands."),
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
    f_aantal="How many of you", f_aantal_hint="Your group rides on its own",
    f_wanneer="Roughly when",
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
         "carnet, sin experiencia, equipo incluido. Desde 175 €. Escríbenos y te decimos qué "
         "días quedan libres.",
    og_titel="Un plan que no se olvida | Surron Tours Tarragona",
    og_meta="Conduce una moto eléctrica por 200 hectáreas privadas cerca de Tarragona. "
            "Sin carnet. Equipo incluido. Desde 175 €.",
    badge="Las únicas rutas en Surron de Catalunya",
    h1_1="Un Plan Que", h1_2="No Se Olvida.",
    lead="Dos horas conduciendo tú mismo una moto eléctrica por 200 hectáreas privadas de "
         "viñedo y pinar, con guía todo el rato. A una hora de Barcelona. Sin carnet. "
         "Sin experiencia. Sin carretera.",
    cta_wa="Pregunta qué días quedan libres",
    cta_form="O rellena el formulario",
    cta_noot="Te contestamos en menos de una hora.",
    trust=["Desde 175 €/persona", "Sin mínimo de personas", "Desde los 12 años", "Sin carnet"],
    feiten=[("175 €", "por persona, dos horas"), ("100 €", "por persona, una hora"),
            ("200 ha", "finca privada"), ("0", "carnet necesario")],

    video_alt="Once segundos en la finca al atardecer — pilotos en la pista, los viñedos, el valle.",
    video_nudge="Pon el sonido.",
    video_aan="Activar sonido",
    video_uit="Silenciar",
    beeld_h="Cómo es por ahí fuera.",
    fotos=[
      ("fleet-three.jpg",
       "Tres motos eléctricas Surron Light Bee en fila sobre tierra roja, con viñedo y pinar detrás",
       "Una para cada uno"),
      ("feel-trail.jpg",
       "Dos personas paradas en una pista entre la maleza en la finca privada cerca de Tarragona",
       "En la pista"),
      ("vineyard-track.jpg",
       "Dos motos eléctricas en un camino de tierra roja entre las viñas",
       "Entre las viñas"),
      ("track-clouds.jpg",
       "Dos motos eléctricas en una pista roja abierta con las lomas boscosas detrás",
       "Pista abierta"),
      ("valley-bikes.jpg",
       "Dos motos eléctricas en la hierba seca con el valle y los pinos al fondo",
       "El valle"),
    ],

    afstand_h="Cómo llegar.",
    afstand=[("Barcelona", "1 hora"), ("Tarragona", "30 min"),
             ("Reus", "40 min"), ("Salou", "40 min")],
    afstand_noot="Aparcamiento gratis en la finca. ¿Sin coche? Dinos dónde estás y lo "
                 "organizamos — tiene un coste aparte de la ruta y te decimos cuánto sería "
                 "antes de que te comprometas a nada.",
    afstand_talen="Tu guía habla Español, Català, English y Nederlands.",

    kart_h="Y sí, cuesta más que un karting.",
    kart=[
      "Un karting son diez minutos compartiendo pista con desconocidos.",
      "Esto son dos horas, una moto para cada uno, un guía solo para vosotros y 200 "
      "hectáreas donde no hay absolutamente nadie más. Ni otro grupo, ni cola, ni turnos.",
      "No es lo mismo pero más caro. Es otra cosa.",
    ],

    niveau_h="¿Y si ya sabes conducir?",
    niveau="La ruta la elegimos según el grupo, así que el terreno se pone tan difícil como "
           "quieras. Pistas anchas entre viñas para el primer día; piedra, subidas fuertes y "
           "revueltas cerradas para quien sabe lo que hace. Dinos qué has llevado antes y te "
           "llevamos a un sitio que no se te haga corto.",

    pitch_label="Por qué esto",
    pitch_h="¿Otra vez el mismo plan de sábado?",
    pitch=[
      "Cenar fuera, kart, paintball, una terraza más. Ya sabes cómo acaba esa tarde, y "
      "dentro de un mes no te vas a acordar de ella.",
      "Esto es media hora de Tarragona, una hora de Barcelona: una montaña entera donde "
      "no hay nadie más y una moto eléctrica que conduces tú. Sin carnet. Sin "
      "experiencia. A los cinco minutos no vas detrás del guía a paso de tortuga — vas "
      "conduciendo.",
      "Es el plan que se cuenta dos veces.",
    ],
    kort_label="En treinta segundos",
    kort_h="Esto es todo.",
    kort=[
        ("Qué es",
         "Una hora, una moto eléctrica para cada uno, por 200 hectáreas privadas de viñedo "
         "y pinar. Un guía va contigo todo el rato, y ruedas solo con tu grupo — nunca con "
         "desconocidos."),
        ("Qué necesitas",
         "Nada. Ni carnet, ni experiencia, ni equipo — casco, peto, guantes y la moto ya "
         "están aquí esperándote. Desde los 12 años."),
        ("Cuánto cuesta",
         "100 € por persona una hora, 175 € dos horas — la de dos horas es de la que hablan "
         "las dos "
         "reseñas de abajo. Todo incluido. Se paga el mismo día y puedes cancelar gratis "
         "hasta 24 horas antes."),
    ],
    prakt_h="Antes de que preguntes.",
    prakt=[
      ("Dónde", "Una finca privada en el campo de Tarragona. A una hora de Barcelona y a "
                "media hora de Tarragona. La dirección exacta y cómo llegar te los mandamos "
                "al confirmar tu día. Hay sitio para aparcar."),
      ("¿Sin coche?", "Podemos ir a buscarte. Tiene un coste aparte y añade algo de viaje, "
                      "así que dinos dónde estás y te decimos cuánto sería."),
      ("Cuándo", "Siete días a la semana, y la hora la montamos contigo — también al "
                 "atardecer, que es cuando esto se ve como en las fotos. Dinos tu día y más "
                 "o menos a qué hora. Quince minutos tarde no pasa nada, solo avísanos."),
      ("Cuánto dura", "Una hora conduciendo, o dos. Cuenta con media hora más para el "
                      "briefing, equiparte y unas vueltas de práctica."),
      ("Edad", "Desde los 12. Los menores de 15 van con un padre, madre o tutor presente "
               "ese día."),
      ("Con quién ruedas", "Solo con tu propio grupo. Nunca te juntamos con gente que no "
                           "conoces — la hora es vuestra, vengas solo o con cinco amigos. "
                           "Para grupos grandes traemos motos de más, así que dinos cuántos "
                           "sois con antelación. Quien prefiera no conducir puede venir "
                           "igualmente a acompañar."),
      ("Qué ponerte", "Zapato cerrado y pantalón largo. Casco, peto, rodilleras, coderas y "
                      "guantes los ponemos nosotros y van incluidos."),
      ("Cómo se paga", "50 € para reservar tu día; el resto en efectivo el mismo día. "
                       "Cancelación gratis hasta 24 horas antes y te devolvemos los 50 €."),
      ("Idiomas", "Español, Català, English, Nederlands."),
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
    f_aantal="Cuántos sois", f_aantal_hint="Tu grupo rueda solo",
    f_wanneer="Más o menos cuándo",
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
    badge="A 30 minuts de Tarragona · A una hora de Barcelona",
    h1_1="Ho Tens Aquí.", h1_2="I No Ho Sabies.",
    lead="Una hora conduint tu mateix una moto elèctrica per 200 hectàrees privades de "
         "vinya i pinede, amb guia tota l'estona. Sense carnet. Sense experiència. 100 €.",
    cta_wa="Pregunta quins dies queden lliures",
    cta_form="O omple el formulari",
    cta_noot="Et contestem en menys d'una hora.",
    trust=["Des de 100 €/persona", "Sense mínim de persones", "A partir dels 12 anys", "Sense carnet"],
    feiten=[("100 €", "per persona, una hora"), ("175 €", "per persona, dues hores"),
            ("200 ha", "finca privada"), ("0", "carnet necessari")],

    video_alt="Onze segons a la finca al capvespre — pilots a la pista, les vinyes, la vall.",
    video_nudge="Posa-hi el so.",
    video_aan="Activa el so",
    video_uit="Silencia",
    beeld_h="Com és allà fora.",
    fotos=[
      ("fleet-three.jpg",
       "Tres motos elèctriques Surron Light Bee en filera sobre terra roja, amb vinya i pineda al darrere",
       "Una per a cadascú"),
      ("feel-trail.jpg",
       "Dues persones aturades en una pista entre la brolla a la finca privada a prop de Tarragona",
       "A la pista"),
      ("vineyard-track.jpg",
       "Dues motos elèctriques en un camí de terra roja entre les vinyes",
       "Entre les vinyes"),
      ("track-clouds.jpg",
       "Dues motos elèctriques en una pista roja oberta amb els turons boscosos al darrere",
       "Pista oberta"),
      ("valley-bikes.jpg",
       "Dues motos elèctriques a l'herba seca amb la vall i els pins al fons",
       "La vall"),
    ],

    afstand_h="Com arribar-hi.",
    afstand=[("Barcelona", "1 hora"), ("Tarragona", "30 min"),
             ("Reus", "40 min"), ("Salou", "40 min")],
    afstand_noot="Aparcament gratuït a la finca. Sense cotxe? Digues-nos on ets i ho "
                 "organitzem — té un cost a part de la ruta i t'expliquem quant seria abans "
                 "que et comprometis a res.",
    afstand_talen="El teu guia parla Català, Español, English i Nederlands.",

    niveau_h="I si ja saps conduir?",
    niveau="La ruta la triem segons el grup, així que el terreny es posa tan difícil com "
           "vulguis. Pistes amples entre vinyes per al primer dia; pedra, pujades fortes i "
           "revolts tancats per a qui sap el que fa. Digues-nos què has portat abans i et "
           "portem a un lloc que no se't faci curt.",

    winter_h="Quan vinguin de fora, i a l'hivern.",
    winter=[
      "Cunyats de Madrid? Amics que no coneixen la zona? Això és el pla, i el tens a mitja "
      "hora de casa.",
      "Setembre i octubre són dels millors mesos per rodar: ni la calor de l'agost ni el "
      "fang. I a l'hivern seguim obrint — si no plou, es roda.",
    ],

    pitch_label="Per què això",
    pitch_h="Ho tens a mitja hora i potser no ho sabies.",
    pitch=[
      "Sopar fora, karts, paintball, una terrassa més. Ja saps com acaba aquesta tarda, i "
      "d'aquí a un mes no te'n recordaràs.",
      "Això és mitja hora de Tarragona: una muntanya sencera on no hi ha ningú més i una "
      "moto elèctrica que condueixes tu. Sense carnet. Sense experiència. Als cinc minuts "
      "no vas darrere del guia a poc a poc — vas conduint.",
      "És el pla que s'explica dues vegades.",
    ],
    kort_label="En trenta segons",
    kort_h="Això és tot.",
    kort=[
        ("Què és",
         "Una hora, una moto elèctrica per a cadascú, per 200 hectàrees privades de vinya i "
         "pinede. Un guia va amb tu tota l'estona, i rodes només amb el teu grup — mai amb "
         "desconeguts."),
        ("Què necessites",
         "Res. Ni carnet, ni experiència, ni equip — casc, pitrera, guants i la moto ja són "
         "aquí esperant-te. A partir dels 12 anys."),
        ("Quant costa",
         "100 € per persona una hora, 175 € dues hores — la de dues hores és de la que parlen "
         "les dues "
         "ressenyes de sota. Tot inclòs. Es paga el mateix dia i pots anul·lar gratis fins "
         "a 24 hores abans."),
    ],
    prakt_h="Abans que ho preguntis.",
    prakt=[
      ("On és", "Una finca privada al camp de Tarragona. A una hora de Barcelona i a mitja "
                "hora de Tarragona. L'adreça exacta i com arribar-hi te les enviem en "
                "confirmar el teu dia. Hi ha lloc per aparcar."),
      ("Sense cotxe?", "Et podem anar a buscar. Té un cost a part i allarga una mica el "
                       "viatge, així que digues-nos on ets i t'expliquem quant seria."),
      ("Quan", "Set dies a la setmana, i l'hora la muntem amb tu — també al capvespre, que "
               "és quan això es veu com a les fotos. Digues-nos el teu dia i més o menys a "
               "quina hora. Quinze minuts tard no passa res, només avisa'ns."),
      ("Quant dura", "Una hora conduint, o dues. Compta mitja hora més per al briefing, "
                     "equipar-te i unes voltes de pràctica."),
      ("Edat", "A partir dels 12. Els menors de 15 van amb un pare, mare o tutor present "
               "aquell dia."),
      ("Amb qui rodes", "Només amb el teu grup. Mai no et posem amb gent que no coneixes "
                        "— l'hora és vostra, vinguis sol o amb cinc amics. Per a grups "
                        "grans portem motos de més, així que digues-nos quants sou amb "
                        "antelació. Qui prefereixi no conduir pot venir igualment a "
                        "acompanyar."),
      ("Què posar-te", "Calçat tancat i pantaló llarg. Casc, pitrera, genolleres, colzeres "
                       "i guants els posem nosaltres i van inclosos."),
      ("Com es paga", "50 € per reservar el teu dia; la resta en efectiu el mateix dia. "
                      "Anul·lació gratuïta fins a 24 hores abans i et tornem els 50 €."),
      ("Idiomes", "Català, Español, English, Nederlands."),
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
    f_aantal="Quants sou", f_aantal_hint="El teu grup roda sol",
    f_wanneer="Més o menys quan",
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
<meta property="og:image" content="{BASIS}/img/couple-vineyard.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="896">
<meta property="og:locale" content="{c["locale"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{c["og_titel"]}">
<meta name="twitter:description" content="{c["og_meta"]}">
<meta name="twitter:image" content="{BASIS}/img/couple-vineyard.jpg">

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


S = {
    "en": dict(aria_slide="review", aria_sterren="Five out of five stars",
               aria_naar="Go to review", aria_vorige="Previous review",
               aria_volgende="Next review", aria_foto="Go to photo"),
    "es": dict(aria_slide="reseña", aria_sterren="Cinco estrellas sobre cinco",
               aria_naar="Ir a la reseña", aria_vorige="Reseña anterior",
               aria_volgende="Reseña siguiente", aria_foto="Ir a la foto"),
    "ca": dict(aria_slide="ressenya", aria_sterren="Cinc estrelles sobre cinc",
               aria_naar="Ves a la ressenya", aria_vorige="Ressenya anterior",
               aria_volgende="Ressenya següent", aria_foto="Ves a la foto"),
}

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

{slider}<script src="{pixel}" data-event="{event}"></script>
</body>
</html>
"""


def reviewblok(taal):
    """Reviews als schuifbaar spoor. Op de telefoon zie je er één tegelijk
       en veeg je door; op een breed scherm staan ze gewoon naast elkaar.
       De bolletjes en pijlen zet het script pas aan als er echt iets te
       schuiven valt, anders zijn het knoppen die niets doen."""
    kaarten = []
    for i, r in enumerate(REVIEWS):
        bron = VERTAALD_UIT[taal].get(r["origineel"])
        noot = f'<div class="rev-src">{bron}</div>' if bron else ''
        kaarten.append(f"""        <figure class="rev" data-slide role="group" aria-roledescription="{S[taal]['aria_slide']}"
                aria-label="{i + 1} / {len(REVIEWS)}">
          <img src="{r["foto"]}" alt="{r["naam"]}" loading="lazy" width="900" height="900">
          <blockquote>
            <div class="rev-stars" aria-label="{S[taal]['aria_sterren']}">★★★★★</div>
            <p>{r[taal]}</p>
          </blockquote>
          <figcaption>{r["naam"]}{noot}</figcaption>
        </figure>""")
    bolletjes = "\n".join(
        f'        <button class="rev-dot" type="button" aria-label="{S[taal]["aria_naar"]} {i + 1}"></button>'
        for i in range(len(REVIEWS)))
    return f"""    <div class="rev-slider" data-slider>
      <button class="rev-nav slider-prev" type="button" aria-label="{S[taal]['aria_vorige']}" hidden>
        <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M15 5l-7 7 7 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
      <div class="rev-track slider-track" tabindex="0">
{chr(10).join(kaarten)}
      </div>
      <button class="rev-nav slider-next" type="button" aria-label="{S[taal]['aria_volgende']}" hidden>
        <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M9 5l7 7-7 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
      <div class="rev-dots slider-dots" hidden>
{bolletjes}
      </div>
    </div>"""


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
    pitch = "\n".join(f"      <p>{x}</p>" for x in c["pitch"])
    afstand = "\n".join(
        f'''        <div class="komen-rij"><b>{plek}</b><span>{tijd}</span></div>'''
        for plek, tijd in c["afstand"])

    kart = ("" if "kart_h" not in c else f'''
<section class="kart">
  <div class="container">
    <h2 class="section-title">{c["kart_h"]}</h2>
    <div class="pitch-tekst">
{chr(10).join(f"      <p>{x}</p>" for x in c["kart"])}
    </div>
  </div>
</section>
''')

    winter = ("" if "winter_h" not in c else f'''
<section class="winter">
  <div class="container">
    <h2 class="section-title">{c["winter_h"]}</h2>
    <div class="pitch-tekst">
{chr(10).join(f"      <p>{x}</p>" for x in c["winter"])}
    </div>
  </div>
</section>
''')

    fotostrip = "\n".join(
        f'''        <figure class="foto" data-slide>
          <img src="/img/{bestand}" alt="{alt}" loading="lazy">
          <figcaption>{bijschrift}</figcaption>
        </figure>''' for bestand, alt, bijschrift in c["fotos"])
    fotobolletjes = "\n".join(
        f'''        <button class="rev-dot" type="button" aria-label="{S[taal]["aria_foto"]} {i + 1}"></button>'''
        for i in range(len(c["fotos"])))

    prakt = "\n".join(f'''      <div class="prakt-rij">
        <b>{t}</b>
        <span>{x}</span>
      </div>''' for t, x in c["prakt"])

    ld = json.dumps({
        "@context": "https://schema.org", "@type": "TouristAttraction",
        "name": "Surron Tours Tarragona", "description": c["ld_beschrijving"],
        "url": url, "image": BASIS + "/img/couple-vineyard.jpg",
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
    <a href="{wa_url(c["wa_txt"])}" class="btn btn-sm hdr-wa" target="_blank" rel="noopener" aria-label="WhatsApp">
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
    <p class="cta-noot">{c["cta_noot"]}</p>
    <div class="hero-trust">{trust}</div>
  </div>
</section>

<section class="factbar" style="padding:0">
  <div class="factbar-grid">{feiten}</div>
</section>

<section class="afstand">
  <div class="container">
    <h2 class="section-title">{c["afstand_h"]}</h2>
    <div class="komen-lijst">
{afstand}
    </div>
    <p class="komen-noot">{c["afstand_noot"]}</p>
    <p class="komen-noot afstand-talen">{c["afstand_talen"]}</p>
  </div>
</section>

<section class="pitch">
  <div class="container">
    <div class="section-label">{c["pitch_label"]}</div>
    <h2 class="section-title">{c["pitch_h"]}</h2>
    <div class="pitch-tekst">
{pitch}
    </div>
  </div>
</section>

<section class="beeld">
  <div class="container">
    <h2 class="section-title beeld-titel">{c["beeld_h"]}</h2>

    <figure class="rit">
      <div class="rit-doos">
        <video poster="/video/poster.jpg{VID}" muted loop playsinline preload="none"
               width="720" height="1280" aria-label="{c["video_alt"]}" data-rit>
          <source src="/video/rit.mp4{VID}" type="video/mp4">
          <source src="/video/rit.webm{VID}" type="video/webm">
        </video>
        <button class="rit-geluid" type="button"
                data-aan="{c["video_aan"]}" data-uit="{c["video_uit"]}"
                aria-label="{c["video_aan"]}">
          <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true">
            <path d="M4 9v6h4l5 4V5L8 9H4z" fill="currentColor"/>
            <path class="rit-streep" d="M17 8l5 8M22 8l-5 8" stroke="currentColor" stroke-width="2" stroke-linecap="round" fill="none"/>
          </svg>
        </button>
      </div>
      <figcaption>{c["video_nudge"]}</figcaption>
    </figure>

    <div class="foto-slider rev-slider" data-slider>
      <div class="foto-track slider-track" tabindex="0">
{fotostrip}
      </div>
      <div class="foto-dots slider-dots" hidden>
{fotobolletjes}
      </div>
    </div>
  </div>
</section>

<section class="kort">
  <div class="container">
    <div class="section-label">{c["kort_label"]}</div>
    <h2 class="section-title">{c["kort_h"]}</h2>
    <div class="kort-grid">
{kort}
    </div>
  </div>
</section>

{kart}
<section class="niveau">
  <div class="container">
    <h2 class="section-title">{c["niveau_h"]}</h2>
    <div class="pitch-tekst"><p>{c["niveau"]}</p></div>
  </div>
</section>

<section class="prakt">
  <div class="container">
    <h2 class="section-title">{c["prakt_h"]}</h2>
    <div class="prakt-lijst">
{prakt}
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

{winter}
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
            <label for="people">{c["f_aantal"]} <span class="veld-hint">{c["f_aantal_hint"]}</span></label>
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
        redirect=REDIRECT if taal == "en" else "", event="ViewContent", pixel=PIXEL,
        slider='<script src="/reviews.js" defer></script>\n')


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
    komen = "\n".join(f'''        <div class="komen-rij"><b>{plek}</b><span>{tijd}</span></div>'''
                      for plek, tijd in i["komen"])

    faq = "\n".join(f'''      <div class="faq-item">
        <button class="faq-q">{v} <span class="tog">+</span></button>
        <div class="faq-a"><div>{a}</div></div>
      </div>''' for v, a in i["faq"])

    return kop(c, i["titel"], i["meta"], url, alt) + f'''
<header>
  <div class="nav-wrap">
    <a href="{c["pad"]}" class="logo">SURRON <span>TOURS</span><small>Tarragona</small></a>
    <a href="{wa_url(c["wa_txt"])}" class="btn btn-sm hdr-wa" target="_blank" rel="noopener" aria-label="WhatsApp">
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
      <div class="split-img"><img src="/img/fleet-three.jpg" alt="{i["bike_alt"]}" loading="lazy"></div>
      <div>
        <h2 style="font-size:28px">{i["bike_h"]}</h2>
        <p>{i["bike_p"]}</p>
      </div>
    </div>
  </div>
</section>

<section class="komen">
  <div class="container">
    <h2 class="section-title">{i["komen_h"]}</h2>
    <p class="section-intro">{i["komen_p"]}</p>
    <div class="komen-lijst">
{komen}
    </div>
    <p class="komen-noot">{i["komen_noot"]}</p>
    <div class="geen-auto">
      <b>{i["komen_geen_auto_h"]}</b>
      <p>{i["komen_geen_auto"]}</p>
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
''' + voettekst(c, op_info=True) + SCRIPTS.format(redirect="", event="ViewContent", slider="", pixel=PIXEL)


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

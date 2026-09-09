#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inhoud van de infopagina (/info/, /es/info/, /ca/info/).

Alles wat iemand pas wil weten NADAT hij geïnteresseerd is, staat hier.
De hoofdpagina heeft één taak — een bericht laten sturen — en mag dus
niets van dit alles bevatten.

Catalaans komt uit ca_info.json, gegenereerd uit de Spaanse tekst.
"""

INFO = {}

INFO["en"] = dict(
    titel="Everything You Need to Know | Surron Tours Tarragona",
    meta="Age limits, what to wear, what's included, how payment works and where we "
         "are. Every practical detail about riding a Surron electric dirt bike on our "
         "private estate near Tarragona.",
    terug="← Back to the main page",
    h1="Everything you need to know.",
    intro="The practical detail, so there are no surprises on the day. Anything not "
          "answered here — just message us.",

    feel_h="What it's actually like.",
    feel_p1="There is no engine noise. You hear your own tyres on the gravel, the wind, "
            "and the birds — and then you open the throttle and the bike simply goes. "
            "No gears. No clutch. No lever to get wrong. You twist, and it pulls.",
    feel_p2="Most people are riding properly within five minutes. Not creeping along "
            "behind a guide — actually riding, choosing their own line, laughing inside "
            "their helmet.",
    feel_p3="And there is nobody else out there. This is not a public trail or a shared "
            "bike park. It is a working organic estate — 200 hectares of vines, olives "
            "and pine — and while you are on it, it is yours. No traffic. No queue. No "
            "other group waiting for their turn.",
    feel_alt="Two riders on Surron electric dirt bikes at sunset on the private estate near Tarragona",

    bike_h="The bike: a 2025 Surron Light Bee.",
    bike_p="Current-model 2025 bikes, not worn-out rentals. Fully electric, near-silent "
           "and about 55 kg — roughly a third of a petrol enduro bike. No clutch, no gears: "
           "you twist the throttle and go. Every rider is on the same bike; we set the "
           "power mode to match you. <b>Eco</b> if you have never ridden, <b>Sport</b> if "
           "you know what you are doing, and your guide can switch you over mid-ride once "
           "you are comfortable.",
    bike_alt="Three Surron Light Bee electric dirt bikes lined up on the private estate near Tarragona, vines and pine forest behind",

    komen_h="Getting here.",
    komen_p="We are on a private estate in the Tarragona countryside, in Catalonia. "
            "Because it is private land we don't publish the address — you get the exact "
            "location, a map pin and driving directions as soon as your date is confirmed. "
            "There is parking on site.",
    komen=[("Barcelona", "about 1 hour by car"),
           ("Tarragona", "about 30 minutes"),
           ("Reus", "about 40 minutes"),
           ("Salou", "about 40 minutes")],
    komen_noot="Drive times are for a normal day. Leave a little extra in July and August, "
               "and plan to arrive 10 minutes before your slot so we can get you kitted up. "
               "Fifteen minutes late is not a problem — just send us a message.",
    komen_geen_auto_h="No car?",
    komen_geen_auto="We can come and pick you up. It costs extra on top of the ride and it "
                    "adds a bit of travel time, so message us with where you are staying "
                    "and we'll tell you what it would be before you book anything.",

    kaarten=[
        ("Who can ride", [
            "<b>From 12 years old</b> with a parent or guardian present. If they can "
            "confidently ride a mountain bike, they can handle Eco mode",
            "<b>From 15 years old</b> riders can come without a parent — we just need "
            "written permission from a parent or guardian",
            "<b>Every rider goes out with a professional guide</b>, whatever their age",
            "<b>No driving licence needed</b> — it's private land",
            "<b>No experience needed</b> — Eco mode is built for day one",
            "Rider height from roughly <b>1.45 m</b> so you can reach the ground comfortably",
            "Maximum rider weight <b>100 kg</b>",
            "Reasonable general fitness — you'll be standing on the pegs at times",
        ]),
        ("What to wear &amp; bring", [
            "<b>Closed shoes</b> — trainers are fine, boots are better. No sandals",
            "<b>Long trousers and long sleeves</b> — protects against dust and scrub",
            "Sunglasses or clear glasses if you wear them",
            "Water, and sun cream in summer",
            "Clothes you don't mind getting dusty — you will get dusty",
            "Your own helmet or armour if you prefer it (optional)",
        ]),
        ("Practical details", [
            "<b>Location:</b> private estate in the Tarragona countryside — exact address "
            "and directions sent when your booking is confirmed",
            "<b>Duration:</b> 1 hour riding (€100 per person) or 2 hours (€175 per person) "
            "— allow about half an "
            "hour on top for briefing and kitting up",
            "<b>Times:</b> seven days a week, and we build the time around you — mornings, "
            "afternoons or at sunset. Weekends book up first",
            "<b>Languages:</b> English, Español, Nederlands, Català",
            "<b>Payment:</b> €50 to hold your date, the rest in cash on the day",
            "<b>Cancellation:</b> free up to 24 hours before your slot",
            "<b>Every ride is private:</b> you ride with your own group only — we never "
            "put you together with people you don't know",
            "<b>Group size:</b> there is no minimum — riding on your own is fine and costs "
            "the same per person. For bigger groups we bring in extra bikes if you tell "
            "us your numbers in advance",
            "<b>Not riding:</b> anyone who would rather watch is welcome to come along",
        ]),
    ],

    incl_t="What's included in the price",
    incl=["A Surron Light Bee to yourself",
          "A guide with you the whole time",
          "Helmet, body armour, elbow and knee pads, gloves",
          "Safety briefing and practice laps before you set off",
          "The route and difficulty picked to match you",
          "Access to the full 200-hectare private estate",
          "Action photos of your ride"],

    faq_h="Questions we get.",
    faq=[
        ("Is there a minimum number of people?",
         "No. One rider on their own is fine, and it costs the same per person as it would "
         "in a group. The ride is private either way — you are never put together with "
         "people you don't know."),
        ("Do I need a driving licence?",
         "No. All the riding happens on private property, so no licence of any kind is "
         "required — car, motorbike or otherwise."),
        ("I've never ridden a motorbike. Can I still do this?",
         "Yes, and most of our riders haven't. There are no gears and no clutch to learn, "
         "the bike is light enough to handle easily, and you get a full briefing and "
         "practice laps in an open area before we go anywhere. Your guide stays with you "
         "the whole time."),
        ("What's the difference between Eco and Sport?",
         "Same 60V motor either way — only the power delivery changes. Eco softens the "
         "throttle and caps the power, which is what a first-timer wants. Sport releases "
         "everything and is reserved for experienced riders on the harder trails. Your "
         "guide sets the mode and can switch you up during the ride."),
        ("What's the minimum age?",
         "12, with a parent or guardian present on the day. From 15 they can come without "
         "a parent — we just need written permission beforehand. A professional guide "
         "rides with them either way, and younger riders start in Eco mode. If we see on "
         "the day that it isn't a good fit, we'll tell you straight."),
        ("What safety gear do you provide?",
         "Helmet, body armour for chest and back, elbow pads, knee pads and gloves. All "
         "included in the price. If you'd rather use your own helmet or armour, you're "
         "welcome to."),
        ("Will we be riding with other people?",
         "No. Every ride belongs to your booking alone. Whether you come on your own, as a "
         "couple or with a group of friends, the only people out there are you and your "
         "guide. We never put two bookings together, and you never share the estate with a "
         "group you don't know."),
        ("Can we come as a group?",
         "Yes. Small groups, families, stag and hen groups and company outings all work "
         "well. Because we can set a different power mode for each rider, mixed-ability "
         "groups genuinely can ride together. For bigger groups we bring in extra bikes — "
         "we just need to know your numbers in advance, so message us early with your dates "
         "and we'll sort the timing."),
        ("We have no car. Can we still come?",
         "Yes — we can come and pick you up. It costs extra on top of the ride and it adds "
         "some travel time, so message us with where you are staying and we'll tell you "
         "what it would be before you commit to anything."),
        ("What time can we ride?",
         "Whenever suits you. We run seven days a week and build the slot around your day — "
         "morning, afternoon or at sunset, which is when the estate looks the way it does "
         "in the photos. Tell us the day and roughly what time and we'll come back with "
         "what's open."),
        ("Can someone come along without riding?",
         "Yes. If one of you would rather watch than ride, that's completely fine — come "
         "along, take the photos, and see the estate."),
        ("What happens if it rains?",
         "Light rain is usually fine and honestly good fun. If the weather makes it unsafe "
         "we'll call you and move your slot — you never lose your money over weather."),
        ("How do I pay, and can I cancel?",
         "€50 holds your date — we arrange that when we confirm — and the rest is cash on "
         "the day. Free cancellation up to 24 hours before your slot, and the €50 comes "
         "straight back to you."),
        ("Where exactly are you?",
         "On a private estate in the countryside of Tarragona province, Catalonia. Because "
         "it's private property we send the exact address, map pin and driving directions "
         "as soon as your booking is confirmed. There's parking on site."),
        ("Can I really buy the wine and olive oil?",
         "Yes. The grapes and olives come off this estate and are made into organic wine "
         "and extra virgin olive oil by a local winemaker right next door, so you can "
         "taste and buy them after your ride. Availability changes with the season — ask "
         "your guide what's ready on the day."),
    ],

    cta_h="Still want to know something?",
    cta_p="Message us. We answer every one personally, usually within minutes.",
)

INFO["es"] = dict(
    titel="Todo lo que necesitas saber | Surron Tours Tarragona",
    meta="Edad mínima, qué ponerte, qué incluye, cómo se paga y dónde estamos. Todos los "
         "detalles prácticos de conducir una moto eléctrica Surron por nuestra finca "
         "privada cerca de Tarragona.",
    terug="← Volver a la página principal",
    h1="Todo lo que necesitas saber.",
    intro="Los detalles prácticos, para que el día de la ruta no haya sorpresas. Si algo "
          "no está aquí, escríbenos y te lo contamos.",

    feel_h="Cómo es de verdad.",
    feel_p1="No hay ruido de motor. Oyes tus propias ruedas sobre la grava, el viento y los "
            "pájaros — y entonces abres gas y la moto sale. Sin marchas. Sin embrague. Sin "
            "ninguna palanca que puedas equivocar. Giras el puño y tira.",
    feel_p2="La mayoría está conduciendo de verdad a los cinco minutos. No detrás del guía a "
            "paso de tortuga: conduciendo, eligiendo tu propia trazada, riéndote dentro del "
            "casco.",
    feel_p3="Y ahí fuera no hay nadie más. Esto no es un circuito público ni un bike park "
            "compartido. Es una finca ecológica en funcionamiento — 200 hectáreas de viña, "
            "olivo y pino — y mientras estás dentro, es tuya. Sin tráfico. Sin colas. Sin "
            "otro grupo esperando turno.",
    feel_alt="Dos personas en motos eléctricas Surron al atardecer en la finca privada cerca de Tarragona",

    bike_h="La moto: una Surron Light Bee de 2025.",
    bike_p="Motos del modelo 2025, no motos de alquiler gastadas. Cien por cien "
           "eléctricas, casi silenciosas y de unos 55 kg — aproximadamente un tercio de lo "
           "que pesa una enduro de gasolina. Sin embrague y sin marchas: giras el puño y "
           "sales. Todo el mundo va en la misma moto; lo único que cambiamos es el modo de "
           "potencia. <b>Eco</b> si no has montado nunca, <b>Sport</b> si sabes lo que "
           "haces, y el guía te lo puede cambiar a mitad de ruta cuando ya vayas cómodo.",
    bike_alt="Tres motos eléctricas Surron Light Bee en fila en la finca privada cerca de Tarragona, con viñedo y pinar detrás",

    komen_h="Cómo llegar.",
    komen_p="Estamos en una finca privada en el campo de Tarragona. Como es terreno "
            "privado no publicamos la dirección — te mandamos la ubicación exacta, el punto "
            "en el mapa y cómo llegar en cuanto confirmamos tu día. Hay sitio para aparcar.",
    komen=[("Barcelona", "una hora en coche aproximadamente"),
           ("Tarragona", "unos 30 minutos"),
           ("Reus", "unos 40 minutos"),
           ("Salou", "unos 40 minutos")],
    komen_noot="Son tiempos de un día normal. En julio y agosto deja un poco de margen, y "
               "cuenta con llegar 10 minutos antes de tu hora para equiparte con calma. "
               "Quince minutos tarde no pasa nada — solo mándanos un mensaje.",
    komen_geen_auto_h="¿Sin coche?",
    komen_geen_auto="Podemos ir a buscarte. Tiene un coste aparte de la ruta y añade algo "
                    "de viaje, así que escríbenos diciendo dónde estás y te decimos cuánto "
                    "sería antes de que reserves nada.",

    kaarten=[
        ("Quién puede conducir", [
            "<b>Desde los 12 años</b> con un padre, madre o tutor presente. Si se maneja "
            "con soltura en una bici de montaña, puede con el modo Eco",
            "<b>Desde los 15 años</b> pueden venir sin un adulto presente — solo "
            "necesitamos una autorización por escrito del padre, madre o tutor",
            "<b>Todo el mundo sale con un guía profesional</b>, tenga la edad que tenga",
            "<b>No hace falta carnet</b> — es terreno privado",
            "<b>No hace falta experiencia</b> — el modo Eco existe justo para el primer día",
            "Estatura a partir de <b>1,45 m</b> aproximadamente, para llegar bien al suelo",
            "Peso máximo del piloto <b>100 kg</b>",
            "Forma física normal — habrá ratos de ir de pie sobre las estriberas",
        ]),
        ("Qué ponerte y qué llevar", [
            "<b>Zapato cerrado</b> — vale una zapatilla, mejor una bota. Nada de sandalias",
            "<b>Pantalón largo y manga larga</b> — protege del polvo y de la maleza",
            "Gafas de sol o gafas transparentes si las usas",
            "Agua, y crema solar en verano",
            "Ropa que no te importe manchar de polvo — te vas a manchar",
            "Tu propio casco o peto si lo prefieres (opcional)",
        ]),
        ("Detalles prácticos", [
            "<b>Ubicación:</b> finca privada en el campo de Tarragona — te mandamos la "
            "dirección exacta y cómo llegar al confirmar la reserva",
            "<b>Duración:</b> 1 hora conduciendo (100 € por persona) o 2 horas (175 € por "
            "persona) — cuenta con "
            "media hora más para el briefing y equiparse",
            "<b>Horarios:</b> siete días a la semana, y la hora la montamos contigo — por "
            "la mañana, por la tarde o al atardecer. Los fines de semana se llenan antes",
            "<b>Idiomas:</b> Español, Català, English, Nederlands",
            "<b>Pago:</b> 50 € para reservar el día, el resto en efectivo el mismo día",
            "<b>Cancelación:</b> gratis hasta 24 horas antes de tu hora",
            "<b>Cada ruta es privada:</b> ruedas solo con tu grupo — nunca te juntamos con "
            "gente que no conoces",
            "<b>Tamaño del grupo:</b> no hay mínimo — puedes venir tú solo y cuesta lo "
            "mismo por persona. Para los grupos grandes traemos motos de más si nos "
            "dices cuántos sois con antelación",
            "<b>Sin conducir:</b> quien prefiera mirar puede venir igualmente a acompañar",
        ]),
    ],

    incl_t="Qué incluye el precio",
    incl=["Una Surron Light Bee para ti solo",
          "Un guía contigo todo el rato",
          "Casco, peto, coderas, rodilleras y guantes",
          "Briefing de seguridad y vueltas de práctica antes de salir",
          "La ruta y la dificultad elegidas según tu nivel",
          "Acceso a las 200 hectáreas privadas de la finca",
          "Fotos de acción de tu ruta"],

    faq_h="Lo que nos suelen preguntar.",
    faq=[
        ("¿Hay un mínimo de personas por grupo?",
         "No. Puedes venir tú solo y cuesta lo mismo por persona que si vinierais varios. "
         "La ruta es privada en cualquier caso — nunca te juntamos con gente que no "
         "conoces."),
        ("¿Hace falta carnet de conducir?",
         "No. Todo se hace en terreno privado, así que no se necesita ningún carnet — ni de "
         "coche ni de moto."),
        ("No he montado nunca en moto. ¿Puedo hacerlo igual?",
         "Sí, y es el caso de la mayoría. No hay marchas ni embrague que aprender, la moto "
         "es lo bastante ligera para manejarla sin esfuerzo, y antes de salir haces el "
         "briefing completo y unas vueltas de práctica en zona abierta. El guía se queda "
         "contigo todo el rato."),
        ("¿Qué diferencia hay entre Eco y Sport?",
         "Es el mismo motor de 60V en los dos — lo único que cambia es cómo entrega la "
         "potencia. Eco suaviza el acelerador y limita la potencia, que es justo lo que "
         "quiere alguien que no ha montado nunca. Sport lo suelta todo y se reserva a "
         "pilotos con experiencia en los caminos más exigentes. El guía elige el modo y te "
         "lo puede subir durante la ruta."),
        ("¿Cuál es la edad mínima?",
         "12 años, con un padre, madre o tutor presente ese día. A partir de los 15 pueden "
         "venir sin adulto — solo necesitamos una autorización por escrito de antemano. En "
         "ambos casos sale un guía profesional con ellos, y los más jóvenes empiezan en "
         "modo Eco. Si el día de la ruta vemos que no encaja, te lo diremos claramente."),
        ("¿Qué equipo de protección ponéis vosotros?",
         "Casco, peto para pecho y espalda, coderas, rodilleras y guantes. Todo incluido en "
         "el precio. Si prefieres usar tu propio casco o peto, adelante."),
        ("¿Vamos a rodar con otra gente?",
         "No. Cada ruta es solo para tu reserva. Vengas solo, en pareja o con un grupo de "
         "amigos, los únicos que estáis ahí fuera sois vosotros y el guía. Nunca juntamos "
         "dos reservas en una misma ruta, y nunca compartes la finca con un grupo que no "
         "conoces."),
        ("¿Podemos venir en grupo?",
         "Sí. Grupos pequeños, familias, despedidas y salidas de empresa funcionan muy "
         "bien. Como podemos poner un modo de potencia distinto a cada piloto, los grupos "
         "con niveles mezclados sí pueden rodar juntos de verdad. Para grupos grandes "
         "traemos motos de más — solo necesitamos saber cuántos sois con antelación, así "
         "que escríbenos pronto con vuestras fechas y cuadramos el horario."),
        ("No tenemos coche. ¿Podemos venir igual?",
         "Sí — podemos ir a buscaros. Tiene un coste aparte de la ruta y añade algo de "
         "viaje, así que escríbenos diciendo dónde estáis y os decimos cuánto sería antes "
         "de que os comprometáis a nada."),
        ("¿A qué hora se puede rodar?",
         "Cuando te vaya bien. Abrimos siete días a la semana y montamos la hora alrededor "
         "de tu día — por la mañana, por la tarde o al atardecer, que es cuando la finca se "
         "ve como en las fotos. Dinos el día y más o menos la hora y te decimos qué queda "
         "libre."),
        ("¿Puede venir alguien sin conducir?",
         "Sí. Si uno de vosotros prefiere mirar en vez de conducir, ningún problema — que "
         "venga, haga las fotos y vea la finca."),
        ("¿Qué pasa si llueve?",
         "Con lluvia floja se rueda perfectamente y hasta es divertido. Si el tiempo lo "
         "hace inseguro te llamamos y te cambiamos la hora — nunca pierdes el dinero por el "
         "tiempo."),
        ("¿Cómo se paga y puedo cancelar?",
         "50 € para reservar tu día — lo organizamos al confirmar — y el resto en efectivo "
         "el mismo día. Cancelación gratis hasta 24 horas antes de tu hora, y los 50 € te "
         "vuelven enteros."),
        ("¿Dónde estáis exactamente?",
         "En una finca privada en el campo de la provincia de Tarragona. Como es terreno "
         "privado, te mandamos la dirección exacta, la ubicación y cómo llegar en cuanto "
         "confirmamos la reserva. Hay sitio para aparcar."),
        ("¿De verdad puedo comprar el vino y el aceite?",
         "Sí. La uva y las olivas salen de esta finca y las convierte en vino ecológico y "
         "aceite de oliva virgen extra un elaborador local justo al lado, así que puedes "
         "probarlos y comprarlos después de la ruta. Según la temporada hay unas cosas u "
         "otras — pregunta al guía qué hay ese día."),
    ],

    cta_h="¿Te queda alguna duda?",
    cta_p="Escríbenos. Contestamos todos los mensajes personalmente, normalmente en minutos.",
)

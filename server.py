"""
Surron Tours — statische webserver met verstandige cache-instellingen.

Waarom dit bestand bestaat: de kale `python -m http.server` stuurt geen
Cache-Control mee. Browsers gaan dan zelf gokken hoe lang ze HTML mogen
bewaren, en dan zien terugkerende bezoekers een oude versie van de site
nadat er iets is aangepast. Dat is precies wat er bij het testen van de
Meta-pixel misging.

HTML wordt daarom nooit gecachet, afbeeldingen juist lang (die veranderen
niet meer, en ze zijn zwaar).
"""
import os
import json
import threading
import datetime
import http.server
import socketserver
import urllib.parse

CACHE_RULES = (
    (('.html', '/'),                                   'no-cache, must-revalidate'),
    (('.jpg', '.jpeg', '.png', '.webp', '.svg', '.ico'), 'public, max-age=2592000'),  # 30 dagen
    (('.css', '.js'),                                  'public, max-age=3600'),       # 1 uur
)


# Welke gebeurtenissen de teller aanneemt. Alles wat hier niet in staat
# wordt genegeerd, zodat niemand de log kan volgooien.
TELLER = ('balk', 'ja', 'nee', 'wa', 'wa-zonder', 'ig', 'ig-zonder')

# Waar de tellingen bewaard worden. Standaard in de container zelf; die
# wordt bij elke deploy opnieuw gebouwd en dan beginnen de tellers op nul.
# Wil je ze bewaren, koppel dan in Railway een Volume (bv. op /data) en
# zet de variabele TELLER_DIR=/data.
TELLER_DIR = os.environ.get('TELLER_DIR', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data'))
TELLER_BESTAND = os.path.join(TELLER_DIR, 'teller.json')

# /stats is alleen te zien met ?k=<STATS_TOKEN>. Zonder die variabele in
# Railway bestaat de pagina niet (404). Er staan geen persoonsgegevens in,
# alleen totalen per week.
STATS_TOKEN = os.environ.get('STATS_TOKEN', '')

_SLOT = threading.Lock()   # één schrijver tegelijk op teller.json


def _laad_teller():
    try:
        with open(TELLER_BESTAND, encoding='utf-8') as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def _bewaar_teller(d):
    try:
        os.makedirs(TELLER_DIR, exist_ok=True)
        tmp = TELLER_BESTAND + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as f:
            json.dump(d, f)
        os.replace(tmp, TELLER_BESTAND)
    except OSError as e:
        print(f'TEL kon niet opslaan: {e}', flush=True)


def _week(nu):
    j, w, _ = nu.isocalendar()
    return f'{j}-W{w:02d}'


def _stats_html():
    d = _laad_teller()
    weken = sorted(d.keys(), reverse=True)
    kol = TELLER
    rijen = []
    for wk in weken:
        r = d[wk]
        balk, ja = r.get('balk', 0), r.get('ja', 0)
        pct = f'{100 * ja / balk:.0f}%' if balk else '–'
        contact = r.get('wa', 0) + r.get('wa-zonder', 0) + r.get('ig', 0) + r.get('ig-zonder', 0)
        cellen = ''.join(f'<td>{r.get(k, 0)}</td>' for k in kol)
        rijen.append(f'<tr><th>{wk}</th>{cellen}<td>{pct}</td><td>{contact}</td></tr>')
    koppen = ''.join(f'<th>{k}</th>' for k in kol)
    tot = {k: sum(d[w].get(k, 0) for w in d) for k in kol}
    tb, tj = tot['balk'], tot['ja']
    tpct = f'{100 * tj / tb:.0f}%' if tb else '–'
    tcontact = tot['wa'] + tot['wa-zonder'] + tot['ig'] + tot['ig-zonder']
    totaal = ''.join(f'<td>{tot[k]}</td>' for k in kol)
    return f"""<!doctype html><html lang="nl"><meta charset="utf-8"><meta name="robots" content="noindex,nofollow">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Surron Tours · teller</title>
<style>body{{font:15px/1.5 system-ui,sans-serif;margin:32px;color:#222}}table{{border-collapse:collapse}}
th,td{{padding:6px 12px;border-bottom:1px solid #ddd;text-align:right}}th:first-child,td:first-child{{text-align:left}}
thead th{{background:#f4f4f4}}tfoot td,tfoot th{{font-weight:700;background:#fafafa}}p{{max-width:640px;color:#555}}</style>
<h1>Teller per week</h1>
<p>balk = cookiebalk getoond · ja/nee = akkoord/geweigerd · wa/ig = WhatsApp/Instagram geklikt mét toestemming ·
-zonder = geklikt zonder toestemming (ziet Meta niet) · % = ja ÷ balk · contact = alle wa+ig samen. Geen persoonsgegevens.</p>
<table><thead><tr><th>week</th>{koppen}<th>% ja</th><th>contact</th></tr></thead>
<tbody>{''.join(rijen) or '<tr><td colspan="10">nog niets geteld</td></tr>'}</tbody>
<tfoot><tr><th>totaal</th>{totaal}<td>{tpct}</td><td>{tcontact}</td></tr></tfoot></table>
<p style="margin-top:24px;font-size:13px">Bestand: {TELLER_BESTAND}</p></html>"""


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # sendBeacon stuurt altijd POST, nooit GET. Zonder dit antwoordt
        # de standaardhandler met 501 en tel je niets.
        if self.path.split('?')[0] == '/t':
            self._tel()
            return
        self.send_error(501, "Unsupported method")

    def do_GET(self):
        """Cookieloze teller op /t?e=...

        Waarom dit bestaat: de Meta-pixel laadt pas na toestemming, dus
        iedereen die de balk negeert en meteen op WhatsApp tikt is
        onzichtbaar. Precies die mensen wil je tellen. Er wordt niets op
        het apparaat gezet of gelezen, er gaat geen identificatie mee, en
        het IP-adres wordt niet weggeschreven — alleen een teller per
        soort gebeurtenis. Uitlezen doe je in de Railway-logs.
        """
        pad = self.path.split('?')[0]
        if pad == '/t':
            self._tel()
            return
        if pad == '/stats':
            self._stats()
            return
        super().do_GET()

    def _stats(self):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        k = (q.get('k') or [''])[0]
        if not STATS_TOKEN or k != STATS_TOKEN:
            self.send_error(404)
            return
        body = _stats_html().encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Cache-Control', 'no-store')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _tel(self):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        e = (q.get('e') or [''])[0]
        if e in TELLER:
            nu = datetime.datetime.now(datetime.timezone.utc)
            print(f'TEL {nu:%Y-%m-%d %H:%M} {e}', flush=True)
            with _SLOT:
                d = _laad_teller()
                wk = d.setdefault(_week(nu), {})
                wk[e] = wk.get(e, 0) + 1
                _bewaar_teller(d)
        self.send_response(204)
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()

    def end_headers(self):
        path = self.path.split('?')[0].split('#')[0].lower()
        if path == '' or path.endswith('/'):
            path += 'index.html'
        for suffixes, value in CACHE_RULES:
            if path.endswith(suffixes):
                self.send_header('Cache-Control', value)
                break
        else:
            self.send_header('Cache-Control', 'no-cache')
        self.send_header('X-Content-Type-Options', 'nosniff')
        super().end_headers()

    def log_message(self, fmt, *args):
        pass  # geen ruis in de Railway-logs


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    # Threaded: een trage download (video, foto) blokkeert dan niet de
    # teller-beacons of een andere bezoeker. Eerder gaf dat af en toe 503.
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    socketserver.ThreadingTCPServer.daemon_threads = True
    with socketserver.ThreadingTCPServer(('', port), Handler) as httpd:
        print(f'serving on :{port}', flush=True)
        httpd.serve_forever()

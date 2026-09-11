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
TELLER = ('balk', 'ja', 'nee', 'wa', 'wa-zonder')


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
        if self.path.split('?')[0] == '/t':
            self._tel()
            return
        super().do_GET()

    def _tel(self):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        e = (q.get('e') or [''])[0]
        if e in TELLER:
            print(f'TEL {datetime.datetime.now(datetime.timezone.utc):%Y-%m-%d %H:%M} {e}',
                  flush=True)
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
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(('', port), Handler) as httpd:
        print(f'serving on :{port}', flush=True)
        httpd.serve_forever()

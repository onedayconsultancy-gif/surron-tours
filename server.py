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
import http.server
import socketserver

CACHE_RULES = (
    (('.html', '/'),                                   'no-cache, must-revalidate'),
    (('.jpg', '.jpeg', '.png', '.webp', '.svg', '.ico'), 'public, max-age=2592000'),  # 30 dagen
    (('.css', '.js'),                                  'public, max-age=3600'),       # 1 uur
)


class Handler(http.server.SimpleHTTPRequestHandler):
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

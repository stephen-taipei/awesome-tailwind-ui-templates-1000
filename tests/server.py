"""Local-only fixture server that also simulates a GitHub Pages project prefix."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
PREFIX = '/awesome-tailwind-ui-templates-1000/'
class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs): super().__init__(*args, directory=str(ROOT), **kwargs)
    def do_GET(self):
        if self.path.startswith(PREFIX): self.path = '/' + self.path[len(PREFIX):]
        super().do_GET()
    def log_message(self, format, *args): pass
if __name__ == '__main__': ThreadingHTTPServer(('127.0.0.1', 4173), Handler).serve_forever()

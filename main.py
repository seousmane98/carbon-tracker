from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class CarbonHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                'message': 'Bienvenue au Dashboard Carbone !',
                'version': '1.0'
            }
            self.wfile.write(json.dumps(response).encode())

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), CarbonHandler)
    print('Server started on http://localhost:8000')
    server.serve_forever()
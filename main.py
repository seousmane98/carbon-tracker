from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import urllib.parse

# Facteurs d'émission de CO2 (kg CO2 par unité)
EMISSION_FACTORS = {
    'car': 0.21,  # kg CO2 par km
    'bus': 0.089,  # kg CO2 par km
    'train': 0.041,  # kg CO2 par km
    'flight': 0.255,  # kg CO2 par km
    'electricity': 0.6,  # kg CO2 par kWh
    'meat': 27.0  # kg CO2 par kg
}

def calculate_carbon(activity_type, value):
    """Calcule l'empreinte carbone"""
    if activity_type not in EMISSION_FACTORS:
        return None
    
    factor = EMISSION_FACTORS[activity_type]
    carbon_kg = value * factor
    
    return {
        'activity': activity_type,
        'value': value,
        'carbon_kg': round(carbon_kg, 2),
        'unit': 'kg CO2'
    }

class CarbonHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Gère les requêtes GET"""
        # Ajouter les en-têtes CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        if self.path == '/':
            response = {
                'message': 'Carbon Tracker API v2.0',
                'endpoints': {
                    '/api/status': 'Server status',
                    '/api/carbon?activity=car&value=100': 'Calculate carbon'
                }
            }
            self.wfile.write(json.dumps(response).encode())
        
        elif self.path == '/api/status':
            response = {'status': 'operational', 'version': '2.0'}
            self.wfile.write(json.dumps(response).encode())
        
        elif self.path.startswith('/api/carbon'):
            query = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(query)
            
            if 'activity' not in params or 'value' not in params:
                self.send_response(400)
                response = {'error': 'Use ?activity=car&value=100'}
                self.wfile.write(json.dumps(response).encode())
                return
            
            activity = params['activity'][0]
            try:
                value = float(params['value'][0])
            except ValueError:
                self.send_response(400)
                response = {'error': 'Value must be a number'}
                self.wfile.write(json.dumps(response).encode())
                return
            
            result = calculate_carbon(activity, value)
            
            if result is None:
                self.send_response(404)
                response = {'error': f'Activity "{activity}" not found', 'available': list(EMISSION_FACTORS.keys())}
                self.wfile.write(json.dumps(response).encode())
            else:
                self.send_response(200)
                self.wfile.write(json.dumps(result).encode())
        
        else:
            self.send_response(404)
            response = {'error': 'Not found'}
            self.wfile.write(json.dumps(response).encode())
    
    def do_OPTIONS(self):
        """Gère les requêtes OPTIONS pour CORS"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), CarbonHandler)
    print('🌍 Carbon Tracker API v2.0 running on http://localhost:8000')
    server.serve_forever()
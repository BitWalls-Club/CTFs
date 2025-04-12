from http.server import BaseHTTPRequestHandler, HTTPServer
import base64
from urllib.parse import urlparse, unquote
from dotenv import load_dotenv
import os

load_dotenv('.vault.env')
USERNAME = os.getenv('USERNAME', 'admin')
PASSWORD = os.getenv('PASSWORD', 'admin')
PORT = int(os.getenv('PORT', 8000))
VAULT_FILE = "creds.txt"

class VaultHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = unquote(parsed_path.path.lstrip('/'))

        if path:  # Assume this is login:password
            if ':' not in path:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'Invalid format. Use login:password in URL path.')
                return

            # Save login:password without auth
            with open(VAULT_FILE, 'a') as f:
                f.write(path + '\n')

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Password saved.\n')
        else:
            # Require auth to read vault
            auth_header = self.headers.get('Authorization-Internal')
            if auth_header is None or not self.is_authenticated(auth_header):
                self.send_response(401)
                self.send_header('WWW-Authenticate', 'Basic realm="Vault"')
                self.end_headers()
                self.wfile.write(b'Unauthorized: Provide Authorization-Internal header to retrieve vault.')
                return

            try:
                with open(VAULT_FILE, 'r') as f:
                    data = f.read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(data.encode('utf-8'))
            except FileNotFoundError:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'Vault is empty.\n')

    def is_authenticated(self, header):
        try:
            auth_type, encoded_credentials = header.split(' ')
            if auth_type != 'Basic':
                return False
            decoded = base64.b64decode(encoded_credentials).decode('utf-8')
            username, password = decoded.split(':', 1)
            return username == USERNAME and password == PASSWORD
        except Exception:
            return False

def run(server_class=HTTPServer, handler_class=VaultHandler, port=PORT):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Vault server running on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()

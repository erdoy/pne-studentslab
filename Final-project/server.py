import http.server
import socketserver
from pprint import pprint

import termcolor
import http.client
import json
from pathlib import Path

PORT = 8080

SERVER = 'rest.ensembl.org'
PARAMS = "?content-type=application/json"


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        termcolor.cprint(self.requestline, 'green')

        # -- Parse the path
        # -- NOTE: self.path already contains the requested resource
        list_resource = self.path.split('?')
        resource = list_resource[0]

        print("Resource: ", resource)
        print("List Resource: ", list_resource)

        if resource == "/":
            contents = Path('html/index.html').read_text()
            content_type = 'text/html'
            error_code = 200
        elif resource == "/list":

            ENDPOINT = '/info/species'
            msg = list_resource[1].strip("msg=")

            conn = http.client.HTTPConnection(SERVER)

            try:
                conn.request("GET", ENDPOINT + PARAMS)
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()

            r1 = conn.getresponse()
            print(f"Response received!: {r1.status} {r1.reason}\n")
            response = json.loads(r1.read().decode("utf-8"))

            pprint([i["display_name"] for i in response["species"][:2]])
            pprint(response["species"][:2])

            lim_species = len(response["species"])
            if msg.isdigit():
                lim = int(msg)

                species = ""

                for i in response["species"][:lim]:
                    species += f"<li>{i['display_name']}</li>"

                contents = Path('html/list.html').read_text().format(lim_species, lim, species)
                content_type = 'text/html'
                error_code = 200
            else:
                contents = Path('html/error.html').read_text()
                content_type = 'text/html'
                error_code = 404


        else:
            contents = Path('html/error.html').read_text()
            content_type = 'text/html'
            error_code = 404

        # Generating the response message
        self.send_response(error_code)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

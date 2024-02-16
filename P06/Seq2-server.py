import http.server
import socketserver
import termcolor
from pathlib import Path

# Define the Server's port
PORT = 8080

socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all its methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        termcolor.cprint(self.requestline, 'green', force_color=True)

        # from urllib.parse import parse_qs, urlparse
        # url_path = urlparse(self.path)
        # path = url_path.path  # we get it from here
        # arguments = parse_qs(url_path.query)
        #
        # import jinja2 as j
        # def read_html_file(filename):
        #     contents = Path("html/" + filename).read_text()
        #     contents = j.Template(contents)
        #     return contents

        # contents = read_html_file("form-e2.html").render(
        #     context={"todisplay": "icgygc"})  # provide a dictionary to build the form

        contents = Path("html/index.html").read_text()

        if self.requestline.startswith("GET /ping?"):
            contents = Path("html/ping.html").read_text()
        elif self.requestline.startswith("GET /"):
            print(self.requestline)


        # if self.requestline.startswith("GET /echo?msg="):
        #     msg = self.requestline.strip("GET /echo?msg=").strip(" HTTP/1.1")
        #     if "&chk=on" in self.requestline:
        #         msg = self.requestline.strip("GET /echo?msg=").strip("&chk=on HTTP/1.1").upper()
        #     contents = Path('html/form-e1.html').read_text().format(msg)
        #     termcolor.cprint(msg, 'red', force_color=True)

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        self.end_headers()

        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

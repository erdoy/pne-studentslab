import http.server
import socketserver
from pprint import pprint
from Seq1 import *
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

        print("List Resource: ", list_resource)

        if resource == "/" or resource == "/index" or resource == "/index.html":
            contents = Path('html/index.html').read_text()
            content_type = 'text/html'
            error_code = 200
        elif resource == "/listSpecies":

            ENDPOINT = '/info/species'

            if len(list_resource) >= 2:
                msg = list_resource[1].strip("limit=")
            else:
                msg = ""

            conn = http.client.HTTPConnection(SERVER)

            try:
                conn.request("GET", ENDPOINT + PARAMS)
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()

            r1 = conn.getresponse()
            print(f"Response received!: {r1.status} {r1.reason}\n")
            response = json.loads(r1.read().decode("utf-8"))

            # pprint(response["species"])

            lim_species = len(response["species"])
            print("Msg: " + msg)

            if msg == "":
                msg = str(lim_species)

            if msg.isdigit():
                lim = int(msg)
                if lim > lim_species:
                    lim = lim_species

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

        elif resource == "/karyotype":

            ENDPOINT = '/info/assembly/'
            msg = list_resource[1].replace("specie=", "")

            conn = http.client.HTTPConnection(SERVER)

            try:
                conn.request("GET", ENDPOINT + msg + PARAMS)
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()

            r1 = conn.getresponse()
            print(f"Response received!: {r1.status} {r1.reason}\n")
            response = json.loads(r1.read().decode("utf-8"))

            pprint(response["karyotype"])

            chromosomes = ""

            for i in response["karyotype"]:
                chromosomes += f"<li>{i}</li>"

            contents = Path('html/karyotype.html').read_text().format(chromosomes)
            content_type = 'text/html'
            error_code = 200

        elif resource == "/chromosomeLength":

            ENDPOINT = '/info/assembly/'
            msgs = [i.replace("specie=", "").replace("chromosome=", "") for i in list_resource[1].split("&")]
            print(msgs)

            conn = http.client.HTTPConnection(SERVER)

            try:
                conn.request("GET", ENDPOINT + msgs[0] + PARAMS)
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()

            r1 = conn.getresponse()
            print(f"Response received!: {r1.status} {r1.reason}\n")
            response = json.loads(r1.read().decode("utf-8"))

            pprint(response)

            length = None

            for i in response["top_level_region"]:
                if i["name"].lower() == msgs[1].lower():
                    length = i["length"]

            contents = Path('html/chromosomeLength.html').read_text().format(length)
            content_type = 'text/html'
            error_code = 200

        elif resource == "/geneSeq":

            ENDPOINT = '/sequence/id/'
            gene = list_resource[1].replace("gene=", "")
            gene = gene.upper()
            print(gene)

            id = get_id("human", gene)
            print(id)

            conn = http.client.HTTPConnection(SERVER)

            try:
                conn.request("GET", ENDPOINT + id + PARAMS)
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()

            r1 = conn.getresponse()
            print(f"Response received!: {r1.status} {r1.reason}\n")
            response = json.loads(r1.read().decode("utf-8"))

            contents = Path('html/geneSeq.html').read_text().format(gene, response["seq"])
            content_type = 'text/html'
            error_code = 200

        elif resource == "/geneInfo":

            ENDPOINT = "/lookup/symbol/"
            gene = list_resource[1].replace("gene=", "")
            gene = gene.upper()
            print(gene)

            conn = http.client.HTTPConnection(SERVER)

            try:
                conn.request("GET", ENDPOINT + "human/" + gene + PARAMS)
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()

            r1 = conn.getresponse()
            print(f"Response received!: {r1.status} {r1.reason}\n")
            response = json.loads(r1.read().decode("utf-8"))

            pprint(response)

            contents = Path('html/geneInfo.html').read_text().format(gene,
                                                                     response["start"],
                                                                     response["end"],
                                                                     response["end"] - response["start"],
                                                                     response["id"],
                                                                     response["assembly_name"])
            content_type = 'text/html'
            error_code = 200

        elif resource == "/geneCalc":

            ENDPOINT = "/sequence/id/"
            gene = list_resource[1].replace("gene=", "")
            gene = gene.upper()
            print(gene)

            id = get_id("human", gene)
            print(id)

            conn = http.client.HTTPConnection(SERVER)

            try:
                conn.request("GET", ENDPOINT + id + PARAMS)
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()

            r1 = conn.getresponse()
            print(f"Response received!: {r1.status} {r1.reason}\n")
            response = json.loads(r1.read().decode("utf-8"))

            s = Seq(response["seq"])
            pprint(str(s))

            response = ""
            count = s.count()
            for i in count:
                response += f"<li>{i}: {count[i]} ({round(count[i] / sum(count.values()) * 100, 1)}%)"

            contents = Path('html/geneCalc.html').read_text().format(gene,
                                                                     s.len(),
                                                                     response)
            content_type = 'text/html'
            error_code = 200

        elif resource == "/geneList":

            ENDPOINT = "/sequence/region/human/"
            # ENDPOINT = "/info/assembly/homo_sapiens/X"
            # ENDPOINT = "info/genomes/assembly/GCA_902167145.1"
            # ENDPOINT = "/lookup/symbol/homo_sapiens"
            msgs = [i.replace("start=", "").replace("chromo=", "").replace("end=", "") for i in
                    list_resource[1].split("&")]

            conn = http.client.HTTPConnection(SERVER)

            try:
                region = f"{msgs[0]}:{msgs[1]}..{msgs[2]}"
                print(ENDPOINT + region + "?content-type=text/plain")
                conn.request("GET", ENDPOINT + region + "?content-type=text/plain")
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()

            r1 = conn.getresponse()
            print(f"Response received!: {r1.status} {r1.reason}\n")
            response = json.loads(r1.read().decode("utf-8"))
            pprint(response)

            # ids = []
            # for i in response["karyotype_band"]:
            #     if i["end"] > int(msgs[2]):
            #         break
            #     if i["start"] > int(msgs[1]):
            #         ids.append(i["id"])
            #
            # pprint(ids)

            # s = Seq(response["seq"])
            # pprint(str(s))

            # response = ""
            # count = s.count()
            # for i in count:
            #     response += f"<li>{i}: {count[i]} ({round(count[i] / sum(count.values()) * 100, 1)}%)"
            #
            contents = Path('html/geneList.html').read_text().format(msgs[0],
                                                                     "0")
            content_type = 'text/html'
            error_code = 200

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


def get_id(species, gene):
    ENDPOINT = '/lookup/symbol/'
    conn = http.client.HTTPConnection(SERVER)

    try:
        conn.request("GET", ENDPOINT + species + "/" + gene.upper() + PARAMS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()
    response = json.loads(r1.read().decode("utf-8"))

    return response["id"]


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

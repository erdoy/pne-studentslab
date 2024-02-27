from Seq1 import Seq
import http.client
import json
from termcolor import cprint

genes = {"FRAT1": "ENSG00000165879",
         "ADA": "ENSG00000196839",
         "FXN": "ENSG00000165060",
         "RNU6_269P": "ENSG00000212379",
         "MIR633": "ENSG00000207552",
         "TTTY4C": "ENSG00000228296",
         "RBMY2YP": "ENSG00000227633",
         "FGFR3": "ENSG00000068078",
         "KDR": "ENSG00000128052",
         "ANK2": "ENSG00000145362"}

gene = input("\nWrite the gene name: ").upper().strip()
ID = genes[gene]

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/' + ID
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Connecting to server: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
response = json.loads(r1.read().decode("utf-8"))

cprint("Gene", color="green", end="")
print(": " + gene)
cprint("Description", color="green", end="")
print(": " + response["desc"])

s = Seq(response["seq"])
cprint("Total length", color="green", end="")
print(": " + str(s.len()))

count = s.count()
for base in count:
    cprint(base, color="blue", end="")
    print(f": {count[base]} ({round(100 * count[base] / sum(count.values()), 1)}%)")

cprint("Most frequent Base", color="green", end="")
print(": " + max(count, key=count.get))

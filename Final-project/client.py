import http.client
import json
from termcolor import cprint

SERVER = 'localhost'
PORT = 8080

print()
print(f"Connecting to server: {SERVER}")

conn = http.client.HTTPConnection(SERVER, PORT)

commands = ["/listSpecies?limit=1&json=1","/geneSeq?gene=FRAT1&json=1","/geneInfo?gene=FRAT1&json=1","/geneCalc?gene=FRAT1&json=1","/geneList?chromo=9&start=22125500&end=22136000&json=1"
            ,"/karyotype?species=mouse&json=1","/karyotype?species=Shrew+mouse&json=1","/chromosomeLength?species=mouse&chromo=18&json=1"]

for i in commands:

    try:
        conn.request("GET", i)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    response = json.loads(r1.read().decode("utf-8"))
    cprint(i, "red", force_color=True)
    cprint(response, "green", force_color=True)
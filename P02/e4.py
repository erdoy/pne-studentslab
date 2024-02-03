from Seq1 import Seq
from Client0 import Client
from termcolor import cprint
import socket
import requests
import pprint
import base64


FOLDER = "https://github.com/erdoy/pne-studentslab/tree/47da4166e2599650628ed76ea741ed11c37c9f6a/sequences/U5.txt"
req = requests.get(FOLDER)
if req.status_code == requests.codes.ok:
    req = req.json()  # the response is a JSON
    # req is now a dict with keys: name, encoding, url, size ...
    # and content. But it is encoded with base64.
    print(req)
    for i in req["payload"]["blob"]["rawLines"]:
        print(i)

    # print(req["title"])
    # content = base64.b64decode(req['content'])
else:
    print('Content was not found.')


FILENAMES = ["U5", "FRAT1", "ADA"]

# c = Client("81.34.46.31", 8081)
# print(c)
# s = Seq()
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# for i in FILENAMES:
#     s.read_fasta(FOLDER + i + ".txt")
#
#     message = f"Sending the {i} Gene to the server..."
#     cprint("To Server: " + message, "blue", force_color=True)
#     c.talk(message)
#
#     print("From Server: " + sock.recv(8081).decode("utf-8"))
#     c.talk((str(s)))

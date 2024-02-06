from Seq1 import Seq
from Client0 import Client
from termcolor import cprint
import socket
import requests
import pprint
import base64

FOLDER = "https://github.com/erdoy/pne-studentslab/tree/47da4166e2599650628ed76ea741ed11c37c9f6a/sequences/"

FILENAMES = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]


def getfromgit(url: str):
    value = ""

    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        req = req.json()
        value = "".join(req["payload"]["blob"]["rawLines"])
    else:
        value = None

    return value


c = Client("0.0.0.0", 8081)
print(c)
s = Seq()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for i in FILENAMES:
    s.strbases = getfromgit(FOLDER + i + ".txt")

    message = f"Sending the {i} Gene to the server..."
    cprint("To Server: " + message, "blue", force_color=True)
    c.talk(message)

    print("From Server: " + sock.recv(2048).decode("utf-8"))
    c.talk(str(s))

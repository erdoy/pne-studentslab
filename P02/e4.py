from Seq1 import Seq
from Client0 import Client
from termcolor import cprint
import socket
import requests

FOLDER = "https://github.com/erdoy/pne-studentslab/tree/47da4166e2599650628ed76ea741ed11c37c9f6a/sequences/"

FILENAMES = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]


def getfromgit(url: str):
    value = ""

    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        req = req.json()
        value = "".join(req["payload"]["blob"]["rawLines"][1:])
    else:
        value = None

    return value


c = Client("212.128.255.68", 8081)
print(c)
s = Seq()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for i in FILENAMES:
    s.strbases = getfromgit(FOLDER + i + ".txt")

    message = f"Sending the {i} Gene to the server..."
    cprint("To Server: " + message, "blue", force_color=True)
    c.talk(message)
    c.talk(str(s))
    # print("From Server: " + sock.recv(2048).decode("utf-8"))
    # c.talk(str(s))

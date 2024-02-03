from Seq1 import Seq
from Client0 import Client
from termcolor import cprint
import socket
import requests

FOLDER = "https://github.com/erdoy/pne-studentslab/tree/47da4166e2599650628ed76ea741ed11c37c9f6a/sequences/"


def getgitseq(filename,
              directory="https://github.com/erdoy/pne-studentslab/tree/47da4166e2599650628ed76ea741ed11c37c9f6a/sequences/"):
    file = ""
    req = requests.get(directory + filename)

    if req.status_code == requests.codes.ok:
        req = req.json()
        file = "".join(req["payload"]["blob"]["rawLines"][1:])
    else:
        file = 'Content was not found.'

    return file


FILENAMES = ["U5", "FRAT1", "ADA"]

c = Client("0.0.0.0", 8081)
print(c)
s = Seq()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for i in FILENAMES:
    s.strbases = getgitseq(i + ".txt")
    print(s.valid)
    s.validate()
    print(s.valid)

    message = f"Sending the {i} Gene to the server..."
    cprint("To Server: " + message, "blue", force_color=True)
    c.talk(message)

    print("From Server: " + sock.recv(8081).decode("utf-8"))
    c.talk((str(s)))

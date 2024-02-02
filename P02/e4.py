from Seq1 import Seq
from Client0 import Client
from termcolor import cprint
import socket

FOLDER = "/home/alumnos/edgamen/Escritorio/PNE/sequences/"
FILENAMES = ["U5", "FRAT1", "ADA"]

c = Client("212.128.255.26", 8081)
print(c)
s = Seq()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for i in FILENAMES:
    s.read_fasta(FOLDER + i + ".txt")

    message = f"Sending the {i} Gene to the server..."
    cprint("To Server: " + message, "blue", force_color=True)
    c.talk(message)

    print("From Server: " + sock.recv(8081).decode("utf-8"))
    c.talk((str(s)))

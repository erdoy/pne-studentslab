from Seq1 import Seq
from Client0 import Client
from termcolor import cprint
from Git import getfromgit
import socket

FOLDER = "https://github.com/erdoy/pne-studentslab/tree/47da4166e2599650628ed76ea741ed11c37c9f6a/sequences/"

FILENAME = "FRAT1"

c = Client("212.128.255.68", 8081)
print(c)
s = Seq()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.strbases = getfromgit(FOLDER + FILENAME + ".txt")

message = f"Sending the {FILENAME} Gene to the server, in fragments of 10 bases..."
cprint("To Server: " + message, "blue", force_color=True)
c.talk(message)

for i in range(5):
    message = f"Fragment {i + 1}: {str(s)[i * 10 : i * 10 + 10]}"
    cprint("To Server: " + message, "blue", force_color=True)
    c.talk(message)

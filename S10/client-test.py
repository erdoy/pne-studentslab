import socket, termcolor
from Client0 import Client

IP = "212.128.255.68"
PORT = 8080

c = Client(IP, PORT)
print(c)

for i in range(5):
    msg = f"Message {i}"

    print("To server: ", end = "")
    termcolor.cprint(msg, "blue", force_color=True)

    print("From server: ", end="")
    termcolor.cprint(c.talk(msg), "green", force_color=True)

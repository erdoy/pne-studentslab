from Seq1 import Seq
from termcolor import cprint
import socket

IP = "127.0.0.1"
PORT = 8080

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))

ls.listen()
print("SEQ Server configured!")

while True:

    print("Waiting for clients...")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        ls.close()

        exit()

    else:

        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()



        if msg == "PING":
            response = "OK!\n"
            cs.send(response.encode())

            cprint("PING command!", "green", force_color=True)
            print(response)

        cs.close()

# -- Close the listening socket
ls.close()

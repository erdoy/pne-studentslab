from Seq1 import Seq
from termcolor import cprint
import socket

seq_list = ["A", "C", "G", "T", "AC"]

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

        elif msg.startswith("GET ") and msg[4:].isdigit():
            server_seq = Seq(seq_list[int(msg[4:])])
            response = str(server_seq) + "\n"
            cs.send(response.encode())

            cprint("GET", "green", force_color=True)
            print(response)

        elif msg.startswith("INFO "):
            cprint("INFO", "green", force_color=True)

            server_seq = Seq(msg[5:])
            response = str(server_seq)

            if server_seq.valid:
                response = (f"Sequence: {str(server_seq)}\n"
                            f"Total length: {server_seq.len()}\n")

                count = server_seq.count()
                for i in count:
                    response += f"{i}: {count[i]} ({round(count[i]/sum(count.values())*100,1)}%)\n"

                cs.send(response.encode())

            print(response)

        cs.close()

# -- Close the listening socket
ls.close()

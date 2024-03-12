from Seq1 import Seq
from termcolor import cprint
import socket

seq_list = ["ACTGGGTACCATGACTAAGTCCAATGCATGCA", "C", "G", "T", "AC"]
FILENAMES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
FOLDER = "../S04/sequences/"

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
            cprint("PING command!", "green")
            response = "OK!"

            cs.send(response.encode())
            print(response)

        elif msg.startswith("GET "):
            cprint("GET", "green")
            response = "Invalid order after 'GET '\n"

            if msg[4:].isdigit():
                response = "Invalid number\n"
                if int(msg[4:]) < len(seq_list):
                    server_seq = Seq(seq_list[int(msg[4:])])
                    response = str(server_seq) + "\n"

            cs.send(response.encode())
            print(response)

        elif msg.startswith("INFO "):
            cprint("INFO", "green")

            server_seq = Seq(msg[5:])
            response = str(server_seq) + "\n"

            if server_seq.valid:
                response = (f"Sequence: {str(server_seq)}\n"
                            f"Total length: {server_seq.len()}\n")

                count = server_seq.count()
                for i in count:
                    response += f"{i}: {count[i]} ({round(count[i]/sum(count.values())*100,1)}%)\n"

            cs.send(response.encode())
            print(response)

        elif msg.startswith("COMP "):
            cprint("COMP", "green")

            server_seq = Seq(msg[5:])
            response = str(server_seq) + "\n"

            if server_seq.valid:
                response = server_seq.complement() + "\n"

            cs.send(response.encode())
            print(response)

        elif msg.startswith("REV "):
            cprint("REV", "green")

            server_seq = Seq(msg[4:])
            response = str(server_seq) + "\n"

            if server_seq.valid:
                response = server_seq.reverse() + "\n"

            cs.send(response.encode())
            print(response)

        elif msg.startswith("GENE "):
            cprint("GENE", "green")

            response = f"No gene in directory named {msg[5:]}\n"

            if msg[5:] in FILENAMES:
                server_seq = Seq()
                server_seq.read_fasta(FOLDER + msg[5:] + ".txt")
                response = str(server_seq) + "\n"

            cs.send(response.encode())
            print(response)

        cs.close()

# -- Close the listening socket
ls.close()

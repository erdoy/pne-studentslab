from termcolor import cprint
import socket
import random


class NumberGuesser:

    def __init__(self, attempts=None, secret_number=None):
        if attempts is None:
            attempts = []
        if secret_number is None:
            secret_number = random.randint(1, 100)

        self.secret_number = secret_number
        self.attempts = attempts

    def guess(self, number):
        self.attempts.append(number)
        if number == self.secret_number:
            return f"You won after {len(self.attempts)} attempts!"
        elif number < self.secret_number:
            return "Higher!"
        else:
            return "Lower!"


IP = "127.0.0.1"
PORT = 8080

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))

ls.listen()
print("Game Server configured!")

ng = None

while True:

    print("Waiting for players...")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        ls.close()
        exit()

    else:
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()

        if msg.isdigit():
            msg = int(msg)
            if 1 <= msg <= 100:
                if ng is None:
                    ng = NumberGuesser()
                    print("Secret number:", ng.secret_number)
                response = ng.guess(msg)
                cs.send(response.encode())

        cs.close()

# -- Close the listening socket
ls.close()

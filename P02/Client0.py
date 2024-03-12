import socket
from termcolor import cprint


class Client:
    def __init__(self, ip, port: int):
        self.ip = ip
        self.port = port

    @staticmethod
    def ping():
        print("OK")

    def __str__(self):
        return f"Connection to SERVER at {self.ip}, PORT: {self.port}"

    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((self.ip, self.port))

        s.send(str.encode(msg))

        response = s.recv(2048).decode("utf-8")

        s.close()

        return response

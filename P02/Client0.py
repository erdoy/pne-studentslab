class Client:
    def __init__(self, IP, Port:int):
        self.ip = IP
        self.port = Port

    def ping(self):
        print("OK")


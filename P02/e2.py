from Client0 import Client

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.26"  # your IP address
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

# -- Test the __str__ method
print(c)

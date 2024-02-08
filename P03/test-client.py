from Client0 import Client

print("-----| Practice 3, Exercise 7 |------")

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print(c)

print("* Testing PING...")
c.ping()

print()

print("* Testing GET...")
for i in range(5):
    msg = f"GET {i}"
    print(msg + ": " + c.talk(msg).replace("\n", ""))

print()

print("* Testing INFO...")
print(c.talk(f"INFO {c.talk('GET 0')}"))

print()

print("* Testing COMP...")
print(c.talk(f"COMP {c.talk('GET 0')}"))

print()

print("* Testing REV...")
print(c.talk(f"REV {c.talk('GET 0')}"))

print()

print("* Testing GENE...")
FILENAMES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for i in FILENAMES:
    print(f"GENE {i}")
    print(c.talk(f"GENE {i}"))
    print()

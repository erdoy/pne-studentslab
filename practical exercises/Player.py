from Client0 import Client

c = Client("127.0.0.1", 8080)
print(c)
print("You must guess a number between 1 and 100")

while True:
    guess = input("Enter a number: ")
    response = c.talk(guess)
    print(response)

    if response.startswith("You won"):
        break

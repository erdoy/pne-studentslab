import socket

# SERVER IP, PORT
PORT = 8081
IP = "212.128.255.68"  # depends on the computer the server is running

while True:
    # -- Ask the user for the message
    message = input("Enter a message: ")
    # -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # -- Establish the connection to the Server
    s.connect((IP, PORT))
    # -- Send the user message
    s.send(str.encode("HELLO FROM THE CLIENT!!!"))
    # -- Close the socket
    s.close()

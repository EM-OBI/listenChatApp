#import socket and threading modules
import socket
import threading

# Define server address (ports and server)
PORT = 5050
SERVER = "192.168.0.135"
ADDR = (SERVER, PORT)

# Create header that is fixed size (64 bytes) and will record the size of incoming message
HEADER = 64

# Decode/encode format
FORMAT = "utf-8"

DISCONNECT_MESSAGE = "bye"

# Create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establish connection with server
client.connect(ADDR)

# Get username
username = input("Please enter username: ")

# Define send function
def send(msg):
    message = msg.encode(FORMAT)

    # Build header for message length
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))

    # send header + message
    client.send(send_length)
    client.send(message)

# Define receiver function
def receive():
    while True:
        try:
            msg = client.recv(2048).decode(FORMAT)

            # Convert client message to "Me"
            if msg.startswith(f"[{username}]"):
                msg = msg.replace(f"[{username}]", "[Me]", 1)
            
            print(msg)
        except:
            print("Disconnected from server")
            break

# Receiver thread
threading.Thread(target=receive, daemon=True).start()

# Send username once
send(username)

# Set up chat loop
while True:
    msg = input("> ")

    if msg.lower() == DISCONNECT_MESSAGE:
        send(msg)
        break
    send(msg)
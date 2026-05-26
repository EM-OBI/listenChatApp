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

# Define send function
def send(msg):
    

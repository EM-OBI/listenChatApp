# import socket and threading modules
import socket
import threading

# Define server address (ports and server)
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

# Define socket 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to address
server.bind(ADDR)

# Create header that is 64 bytes and will tell us the size of the incoming data
HEADER = 64

# Decode/encode format
FORMAT = "utf-8"

DISCONNECT_MESSAGE = "!DISCONNECTED"

# Create dictionary to handle all connected clients' names and connection
Clients = {}

# Define receive function
def receive_msg(conn):
    msg_length = conn.recv(HEADER).decode(FORMAT)

    if not msg_length:
        return None

    if msg_length:
        msg_length = int(msg_length.strip())

        return conn.recv(msg_length).decode(FORMAT)
    
    return None


# Define function to handle connected clients
def handle_clients(conn, addr):
    # Add new clients to add clients
    print(f"[NEW CONNECTION] {addr} connected")

    # First message should be username
    username = receive_msg(conn)

    # Define name value pair for client
    Clients[conn] = username

    join_msg = f"{username} has joined the chat"
    print(join_msg)
    broadcast(conn, "Server", join_msg)

    connected = True

    while connected: 
        try:
            msg = receive_msg(conn)

            if msg:
                # print(f"[{username}]{msg}")
                broadcast(conn, username, msg)

                if msg == DISCONNECT_MESSAGE:
                    connected = False
        except:
            break

    # Cleanup and close
    leave_msg = f"{username} has left the chat"
    print(leave_msg)
    broadcast(conn, "Server", leave_msg)

    if conn in Clients:
        del Clients[conn]
    
    conn.close()

# Create broadcast functionality
def broadcast(sender_conn, sender_name, msg):
    if sender_name == "Server":
        message = f"{msg}".encode(FORMAT)
    else: 
        message = f"[{sender_name}] {msg}".encode(FORMAT)

    dead_clients = []

    for client in Clients:
        if client != sender_conn:
            try:
                client.send(message)
            except:
                dead_clients.append(client)

    # remove dead clients safely
    for dc in dead_clients:
        if dc in Clients:
            del Clients[dc]
        try:
            dc.close()
        except:
            pass

# Start server and listen for new connections
def start():
    # Set maximum connections to 4
    server.listen(4)
    print (f"Server is listening on {SERVER}")
    try:
        while True:
        # Use blocking to avoid program from running until valid connection is accepted
            conn, addr = server.accept()

            # Put each new client into a new thread
            thread = threading.Thread(target = handle_clients, args=(conn, addr))
            
            thread.start()

            # Display the number of threads running i.e. all active connections
            print(f"ACTIVE CONNECTIONS {threading.active_count() - 1}")
    # Handle keyboard interrupt gracefully
    except KeyboardInterrupt:
        print("\n[SHUTTING DOWN SERVER]")
    finally:
        server.close()

        print("Server socket closed.")


# Start server
print(f"Server is starting...")
start()
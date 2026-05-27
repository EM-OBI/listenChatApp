#import socket and threading and tkinter modules
import socket
import threading
from tkinter import *

# Set up the GUI
root = Tk()
root.title("Listen")
root.geometry("500x600")
root.config(bg="lightgray")

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


# Get username
username = ""

# Chat display frame
chat_frame = Frame(root, bg="lightgray")
chat_frame.pack(fill=BOTH, expand=True)

# Define send message function
def add_message(msg, sender="other"):
    if sender == "me":
        bg_color = "blue"
        anchor_side = "e"
    
    elif sender == "system":
        bg_color = "green"
        anchor_side = "center"
    
    else:
        bg_color = "darkgray"
        anchor_side = "w"
    
    label = Label(
        chat_frame,
        text=msg,
        bg=bg_color,
        padx=10,
        pady=5,
        wraplength=300,
        justify=LEFT
    )

    label.pack(anchor=anchor_side, pady=5, padx=10)

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

                # Messages from server/system
                if "joined the chat" in msg or "left the chat" in msg:
                    root.after(0, lambda m=msg: add_message(m, "system"))

                # Own messages
                elif msg.startswith(f"[{username}]"):
                    cleaned = msg.replace(f"[{username}]", "[Me]", 1)
                    root.after(0, lambda m=cleaned: add_message(m, "me"))

                # Other users
                else:
                    root.after(0, lambda m=msg: add_message(m, "other"))

            except:
                root.after(0, lambda: add_message("Disconnected from server", "system"))
                break

# Connect to server
def connect():
    global username

    username = username_entry.get().strip()

    if username == "":
        return
    
    client.connect(ADDR)

    # Receiver thread
    threading.Thread(target=receive, daemon=True).start()

    # Send username once
    send(username)

    add_message(f"You joined the chat as {username}", "system")

    connect_button.config(state=DISABLED)

# Send the message
def send_message():
    msg = message_entry.get().strip()

    if msg == "":
        return
    
    send(msg)

    # Display own message immediately
    add_message(f"[Me] {msg}", "me")

    message_entry.delete(0, END)

    if msg.lower() == DISCONNECT_MESSAGE:
        client.close()
        root.destroy()


# GUI LAYOUT
top_frame = Frame(root, bg="lightgray")
top_frame.pack(pady=10)

username_label = Label(top_frame, text="Username:", bg="lightgray")
username_label.pack(side=LEFT)

username_entry = Entry(top_frame)
username_entry.pack(side=LEFT, padx=5)

connect_button = Button(top_frame, text="Connect", command=connect)
connect_button.pack(side=LEFT)

bottom_frame = Frame(root, bg="lightgray")
bottom_frame.pack(fill=X, pady=10)

message_entry = Entry(bottom_frame)
message_entry.pack(side=LEFT, fill=X, expand=True, padx=10)

send_button = Button(bottom_frame, text="Send", command=send_message)
send_button.pack(side=RIGHT, padx=10)

# Start main event loop
root.mainloop()
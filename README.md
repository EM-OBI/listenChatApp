# Overview

## Description. How to use and start
I designed and implemented a simple chat app that allows a maximum of four friends connected to the same local network to exchange messages with each other. 
To use this software, you need a separate terminal on the same computer or on a separate computer connected to the same wifi. Afterwards, you start the server by running server.py. Then you can run up to four different clients on the same computer or on separate computers connected to the same network as the server. Then on the client terminal(s) you run client.py. Then you can connect to the server by clicking the "connect" button and start chatting. To disconnect from the server you use the disconnect message "bye" or on the terminal you click "ctrl + c"

## Purpose
The purpose of this project was to improve my understanding of computer networking fundamentals using Python. My aims were to:

* Learn how client-server communication works over a local network
* Understand socket programming and message transmission using TCP
* Improve my ability to design and integrate graphical user interfaces in Python using Tkinter
* Learn how to combine backend networking logic with a front-end GUI system

### Video demonstration
{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication
### Client/Server
I used a client/server architecture mainly because it was easier to set up. This involves the communication between client(s) through a central server.
{Describe the architecture that you used (client/server or peer-to-peer)}

### Protocol
{Identify if you are using TCP or UDP and what port numbers are used.}
* Server port: 5050
* Communication is established using a persistent TCP socket connection

### Message format
{Identify the format of messages being sent between the client and server or the messages sent between two peers.}
Messages are transmitted using UTF-8 encoding.

Each message consists of:
* A fixed-size header (64 bytes) that tells the server the length of the actual incoming message
* The actual message content encoded in UTF-8

# Development Environment
The project was developed using:
* IDE: Visual Studio Code
* Testing environment: Split local machine terminals and multiple devices on the same Wi-Fi network
* Operating systems: macOS and Windows (cross-platform testing)

{Describe the programming language that you used and any libraries.}
The application was written in Python and makes use of the following standard libraries:

* socket – for TCP client-server communication
* threading – to handle multiple clients at the same time on the server side
* tkinter – to build the graphical user interface for the client application

# Useful Websites
{Make a list of websites that you found helpful in this project}
* [Medium] https://medium.com/@shivambhadani_/understanding-tcp-and-building-our-own-tcp-server-in-c-language-8de9d9de78ef
* [YouTube]https://youtube.com/playlist?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&si=otZ9aJOeqmfsfCUd
* [YouTube]https://www.youtube.com/watch?v=sUzM-vIC-s4

# Future Work
### Things to fix, improve in the future
* Making the chat accessible over the internet using a public IP or a server on the cloud
* Developing a GUI for the server to allow easier startup, monitoring, and shutdown
* Implementing a more graceful server shutdown mechanism without relying on KeyboardInterrupt
* Improving UI design by adding timestamps, and better styling)
* Adding authentication and user session management for better control of connected clients
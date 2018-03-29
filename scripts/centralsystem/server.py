#!/usr/bin/python
import socket


class Server:

    def __init__(self):
        # Create a TCP/IP socket
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Get local server IP
        host = socket.gethostbyname(socket.gethostname())
        port = 34567
        print('Local IP address: ', host)
        self.s.bind((host, port))
        # 5 sockets max
        self.s.listen(5)

    def connect_socket(self):
        # Wait for client to connect to server
        c, addr = self.s.accept()
        print('Connected ', addr)
        c.send(b'Ground control to major Tom')
        # Receive client message
        received = c.recv(4096)
        print(received)
        # Close connection with client
        c.close()
        print('Closed connection with ', addr)


serversocket = Server()

serversocket.connect_socket()

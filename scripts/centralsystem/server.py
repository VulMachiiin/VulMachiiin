#!/usr/bin/python
import socket
import json


class Server:

    # Initialises server
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

    # Parses regular String to JSON
    def to_json(self, message):
        parsed_json = json.loads(message)
        return parsed_json

    # Handles connection with client socket
    def connect_socket(self):
        # Wait for client to connect to server
        c, addr = self.s.accept()
        print('Connected ', addr)
        c.send(b'Server message')
        # Receive client message
        received = c.recv(4096)
        print(received)
        # Close connection with client
        c.close()
        print('Closed connection with ', addr)


serversocket = Server()
serversocket.connect_socket()



# Json Format and parsing testcode (not needed anymore due to Python not being able to send JSON objects over sockets)
'''testJson = '{"directions" : "FRLD", "cartridgeheight" : "3"}'
parsedJson = serversocket.to_json(testJson)
print(parsedJson['directions'])'''

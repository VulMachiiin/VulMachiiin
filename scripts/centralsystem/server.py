#!/usr/bin/python
import socket
import json
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


class Server:

    # Initialises server
    def __init__(self):
        key = get_random_bytes(16)
        print(key)
        # Create a TCP/IP socket
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Get local server IP
        host = socket.gethostbyname(socket.gethostname())
        port = 34567
        print('Local IP address: ', host)
        self.s.bind((host, port))
        # 5 sockets max
        self.s.listen(5)

    #Creates a random key ()
    def create_randomkey(self):
        key = get_random_bytes(16)
        print(key)

    # encrypts the message using AES128 EAX
    def do_encrypt(self, message):
        key = 'test123'
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext = cipher.encrypt(message)
        return ciphertext

    # Parses regular String to JSON
    def to_json(self, message):
        parsed_json = json.loads(message)
        return parsed_json

    # Handles connection with client socket
    def connect_socket(self):
        # Wait for client to connect to server
        c, addr = self.s.accept()
        print('Connected ', addr)
        testJson = '{"directions" : "FRLD", "cartridgeheight" : "3"}'
        c.send(do_encrypt(testJson))
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

#!/usr/bin/python
import socket
import json
from Crypto.Cipher import AES


class Server:

    # All String-type need to be converted to byte-type
    key = b'2r5u7x!A%D*G-KaP'
    IV = b'This is an IV456'

    # Initialises server
    def __init__(self):
        # Create a TCP/IP socket
        self.s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        # Get local server IP
        print(socket)
        host = ''
        port = 34567
        #print('Local IP address: ', socket.getaddrinfo(host, port)[0][4][0])
        self.s.bind((host, port))
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 5 sockets max
        self.s.listen(1)

    # encrypts the message using AES128 CFB
    def do_encrypt(self, message):
        cipher = AES.new(self.key, AES.MODE_CFB, self.IV)
        ciphertext = cipher.encrypt(message)
        return ciphertext

    # decrypts the message using AES128 CFB
    def do_decrypt(self, message):
        cipher = AES.new(self.key, AES.MODE_CFB, self.IV)
        decryptedmessage = cipher.decrypt(message)
        return decryptedmessage

    # Parses regular String to JSON
    def to_json(self, message):
        parsed_json = json.loads(message)
        return parsed_json

    # Handles connection with client socket
    def create_socket(self):
        # Wait for client to connect to server
        c, addr = self.s.accept()
        print('Connected ', addr)
        testJson = b'{"directions" : "FRLD", "cartridgeheight" : "3"}'
        test = serversocket.do_encrypt(testJson)
        c.send(test)
        # Receive client message
        #received = c.recv(4096)
        #print(received)
        # Close connection with client
        c.close()
        print('Closed connection with ', addr)

    def close_server(self):
        self.s.close()



serversocket = Server()
serversocket.create_socket()
serversocket.close_server()

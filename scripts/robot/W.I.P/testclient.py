import socket
from Crypto.Cipher import AES

class socketHandler:

    def __init__(self):
        print('Creating socket')
        self.s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, IP_address, port):
        self.s.connect((IP_address, port))
        ciphertext = self.s.recv(4096)
        decryptedmessage = self.do_decrypt(ciphertext)
        return decryptedmessage

    def do_decrypt(self, ciphertext):
        key = b'2r5u7x!A%D*G-KaP'
        IV = b'This is an IV456'
        cipher = AES.new(key, AES.MODE_CFB, IV)
        decryptedmessage = cipher.decrypt(ciphertext)
        decryptedmessage = decryptedmessage.decode("utf-8")
        return decryptedmessage

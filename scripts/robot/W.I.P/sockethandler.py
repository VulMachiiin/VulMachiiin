import socket
import maes
import ubinascii


class socketHandler:

    def __init__(self):
        print('Creating socket')
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, IP_address, port):
        self.s.connect((IP_address, port))
        ciphertext = self.s.recv(4096)
        decryptedmessage = self.do_decrypt(ciphertext)
        return decryptedmessage

    def array_tostring(self,array_data):
        _string = ""
        for _array in array_data:
            _string = _string + chr(_array)
        return _string

    def do_decrypt(self, ciphertext):
        key = b'2r5u7x!A%D*G-KaP'
        IV = b'This is an IV456'
        cipher = decryptor = maes.new(key, maes.MODE_CFB, IV=IV)
        decryptedmessage = decryptor.decrypt(ciphertext)
        print(self.array_tostring(decryptor.decrypt(ciphertext)))
        return "Koel"

import usocket as socket
import maes
import ubinascii


class Server_connector:

    def __init__(self):
        print('Creating socket')
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connects with the server via sockets
    def connect(self, IP_address, port):
        self.s.connect((IP_address, port))
        print('Succesfully connected to: ', IP_address)
        self.s.send('hoi')
        ciphertext = self.s.recv(4096)
        print('Encrypted message: ', ciphertext)
        decryptedmessage = self.do_decrypt(ciphertext)
        print('Decrypted message: ', decryptedmessage)
        return decryptedmessage

    # Converts char array to string
    def array_tostring(self, array_data):
        _string = ""
        for _array in array_data:
            _string = _string + chr(_array)
        return _string

    # Encrypts message
    def do_encrypt(self, _string):
        key = b'2r5u7x!A%D*G-KaP'
        IV = b'This is an IV456'
        cryptor = maes.new(key, maes.MODE_CBC, IV=IV)
        ciphertext = cryptor.encrypt(str.encode(_string))
        return ciphertext

    # Decrypts message
    def do_decrypt(self, ciphertext):
        key = b'2r5u7x!A%D*G-KaP'
        IV = b'This is an IV456'
        decryptor = maes.new(key, maes.MODE_CBC, IV=IV)
        return self.array_tostring(decryptor.decrypt(ciphertext))

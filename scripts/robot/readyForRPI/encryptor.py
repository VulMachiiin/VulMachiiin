import maes
import ubinascii

class Encryptor:
    # Converts char array to string
    key = b'2r5u7x!A%D*G-KaP'
    IV = b'This is an IV456'
    cryptor = maes.new(key, maes.MODE_CBC, IV=IV)


    def array_tostring(self, array_data):
        return ''.join(array_data)

    # Encrypts message
    def encrypt(self, _string):
        ciphertext = self.cryptor.encrypt(str.encode(_string))
        return ciphertext

    # Decrypts message
    def decrypt(self, ciphertext):
        return self.array_tostring(self.cryptor.decrypt(ciphertext))

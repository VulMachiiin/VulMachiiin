import socket
from Crypto.Cipher import AES

print('Creating socket')

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = '192.168.0.118'
port = 34567
s.connect((IP_address, port))

ciphertext = s.recv(4096)

key = b'2r5u7x!A%D*G-KaP'
IV = b'This is an IV456'
cipher = AES.new(key, AES.MODE_CFB, IV)
decryptedmessage = cipher.decrypt(ciphertext)

#Convert byte-type back to String-type
print(decryptedmessage.decode("utf-8") )

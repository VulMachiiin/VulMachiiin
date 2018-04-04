import socket

print('Creating socket')
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = '192.168.0.118'
port = 34567
s.connect((IP_address, port))
ciphertext = s.recv(4096)
key = 'test123'
cipher = AES.new(key, AES.MODE_EAX)
decryptedmessage = cipher.decrypt(ciphertext)
print(decryptedmessage)

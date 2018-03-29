import socket

print('Creating socket')
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = '192.168.0.118'
port = 34567
s.connect((IP_address, port))
s.send('one small step for man one giant leap for mankind')
reply = s.recv(4096)
print(reply)

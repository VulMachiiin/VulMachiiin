#!/usr/bin/python
import socket

s = socket.socket()
host = socket.gethostbyname(socket.gethostname())

print ('Local IP address: ', host)
port = 34567

s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print ('Connected ', addr)
    c.send('Thanks bruv')
    c.close()

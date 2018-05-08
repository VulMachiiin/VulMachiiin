import socket               # Import socket module

HOST = ''
PORT = 52342

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket created')

try:
    server.bind((HOST, PORT))
except socket.error as msg:
    print('bind failed. error code:' + str(msg[0]) + ' message:' + msg[1])

print('socket bind complete')

server.listen(10)
print('socket now listening')

while True:
    conn, addr = server.accept()
    print('Connected with' + addr[0] + ':' + str(addr[1]))

s.close()
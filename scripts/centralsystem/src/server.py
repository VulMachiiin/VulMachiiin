import socket               # Import socket module

from threads import RobotConnection, DatabaseHook
from pathfinding import PathFinding
from databaseconnector import DatabaseConnector

class Server():
    '''Opens the server for outside connections and keeps track of connected devices'''
    def __init__(self, port):
        self.server_processes = ServerProcesses(self)

        key = b'2r5u7x!A%D*G-KaP'
        iv = b'This is an IV456'
        self.cipher = AES.new(key, AES.MODE_CBC, iv)
        
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('socket created')

        try:
            self.server_socket.bind(('', port))
        except socket.error as msg:
            print('bind failed. error code:' + str(msg[0]) + ' message:' + msg[1])
        print('socket bind complete')
    
    def __del__(self):
        self.server_socket.close()

    def run(self):
        self.server_socket.listen()
        print('socket now listening')

        while True:
            conn, addr = self.server_socket.accept()
            print('Connected with' + addr[0] + ':' + str(addr[1]))
            conn_type = int(conn.rcv(64))
            #for now only robot connects
            if conn_type == 1:
                self.robot_connection = RobotConnection(conn, self.cipher, self)
                self.robot_connection.run()
            elif conn_type == 0:
                print('shelf tried to connect but no handling for it yet!')

    def add_shelve_connection(self, thread_id, conn_type, thread_reference):
        self.shelve_connections_dict[thread_id] = ((conn_type, thread_reference))

    def remove_shelve_connection(self, thread_id):
        del self.shelve_connections_dict[thread_id]


class ServerProcesses():

    def __init__(self, server):
        self.server = server
        self.robot_connection = None
        self.shelve_connections_dict = {}

        self.robot_at_shelve = False
        self.robot_ready = False
        self.trays_to_replace = []

        self.db_connector = DatabaseConnector()
        self.pathfinding = PathFinding()
        self.database_hook = DatabaseHook(self.db_connector, self)



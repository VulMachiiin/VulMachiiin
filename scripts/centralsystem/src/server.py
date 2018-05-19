import socket               # Import socket module

from threads import RobotConnection
from pathfinding import PathFinding
from databaseconnector import DatabaseConnector

class ServerConnector():
    '''Opens the server for outside connections and keeps track of connected devices'''
    def __init__(self, port):
        self.robot_connection = None
        self.shelve_connections_dict = {}

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('socket created')

        try:
            self.server.bind(('', port))
        except socket.error as msg:
            print('bind failed. error code:' + str(msg[0]) + ' message:' + msg[1])
        print('socket bind complete')
    
    def __del__(self):
        self.server.close()

    def run(self):
        self.server.listen()
        print('socket now listening')

        while True:
            conn, addr = self.server.accept()
            print('Connected with' + addr[0] + ':' + str(addr[1]))
            #for now only robot connects
            self.robot_connection = RobotConnection(conn)
            self.robot_connection.run()

    def add_shelve_connection(self, thread_id, conn_type, thread_reference):
        self.shelve_connections_dict[thread_id] = ((conn_type, thread_reference))

    def remove_shelve_connection(self, thread_id):
        del self.shelve_connections_dict[thread_id]

class ServerProcesses():
    '''Gets given to threads so they have a common object to manipulate the server on'''

    def __init__():
        self.server_connector = ServerConnector()
        self.db_connector = DatabaseConnector()
        self.pathfinding = PathFinding()
        
        self.robot_at_shelve = False
        self.robot_ready = False
    

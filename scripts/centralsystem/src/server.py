import socket               # Import socket module
import methods
import time

from threads import RobotConnection, DatabaseHook
from pathfinding import PathFinding
from databaseconnector import DatabaseConnector

class Server():
    '''Opens the server for outside connections and keeps track of connected devices'''
    def __init__(self, port):
        self.robot_connection = None
        self.shelve_connections_dict = {}
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
                print('shelf tried to connect but no handler for it yet!')

    def add_shelve_connection(self, shelf_id, conn_type, thread_reference):
        self.shelve_connections_dict[shelf_id] = thread_reference

    def remove_shelve_connection(self, shelf_id):
        del self.shelve_connections_dict[shelf_id]


class ServerProcesses():

    def __init__(self, server):
        self.server = server

        self.robot_at_shelve = False
        self.robot_ready = False
        self.trays_to_replace = []
        self.items_to_order = []

        self.db_connector = DatabaseConnector()
        self.pathfinding = PathFinding(self.db_connector)
        self.database_hook = DatabaseHook(self)
        self.database_hook.run()

    def print_lists(self):
        if self.items_to_order:
            message_str = 'Following items should be ordered:'
            methods.print_log(message_str)
            print(message_str)
            for item in self.items_to_order:
                message_str = 'order {}, {} items left'.format(item[1], item[2])
                methods.print_log(message_str, leading_space=4)
                methods.print_padded(message_str, leading_space=4)            

        if self.robot_ready and self.trays_to_replace:
            message_str = 'Fill robot with:'
            methods.print_log(message_str)
            print(message_str)
            for i in range(0, min(3, len(self.trays_to_replace))):
                name, amount_per_cartridge, product_id, shelve_id, x_coordinate, y_coordinate = self.trays_to_replace[i]
                message_str = 'fill place x = {}, y = {} with {} {}'.format(x_coordinate, y_coordinate, amount_per_cartridge, name)
                methods.print_log(message_str, leading_space=4)
                methods.print_padded(message_str, leading_space=4)

    def tray_list_updated(self):
        self.print_lists()
        #while input_str != 'ready':
        #    input_str = input('type ready to continue')
        #self.server.robot_connection.message_queue.append() fix pathfinding first Owo

            

server = Server(54321)
server.run()

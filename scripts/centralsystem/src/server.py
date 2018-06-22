import socket               # Import socket module
import methods
import time
import os

from threads import RobotConnection, DatabaseHook
from pathfinding import PathFinding
from databaseconnector import DatabaseConnector

class Server():
    '''Opens the server for outside connections and keeps track of connected devices'''
    def __init__(self, port):
        self.robot_connection = None
        self.shelve_connections_dict = {}
        self.server_processes = ServerProcesses(self)

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
                self.robot_connection = RobotConnection(conn, self)
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
        self.trays_to_replace_in_process = []
        self.items_to_order = []

        self.db_connector = DatabaseConnector()
        self.pathfinding = PathFinding(self.db_connector)
        self.database_hook = DatabaseHook(self)
        self.database_hook.run()

    def print_lists(self):
        #os.system('cls' if os.name == 'nt' else 'clear')
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
            for i in range(0, min(3, len(self.trays_to_replace))): # runs the loop a maximum of 3 times depending on how many shelve tray requests there are
                self.trays_to_replace_in_process.append(self.trays_to_replace[0]) #adds a list of shelves that will be handled right now

                name, amount_per_cartridge, product_id, shelve_id, x_coordinate, y_coordinate = self.trays_to_replace[0]
                message_str = 'fill place x = {}, y = {} with {} {}'.format(x_coordinate, y_coordinate, amount_per_cartridge, name)
                methods.print_log(message_str, leading_space=4)
                methods.print_padded(message_str, leading_space=4)

                del self.trays_to_replace[0] #deletes the first item

    def tray_list_updated(self):
        self.print_lists()
        if self.trays_to_replace == [] or not self.robot_ready:
            return
        input_str = ""
        while input_str != 'ready':
            input_str = input('type ready to continue')
        self.robot_ready = False

        location_list = []
        for item in self.trays_to_replace_in_process:
            if item[3] not in location_list:
                location_list.append(item[3])
        print('trays to replace:', self.trays_to_replace, 'trays now:', self.trays_to_replace_in_process)
        shortest_perm, dir_list = self.pathfinding.robot_directions(location_list) #get the path needed for the robot and also the order in which the shelves will get visited. This is needed for the unload message that needs to give the location

        trays_to_replace_in_process_copy = list(self.trays_to_replace_in_process) #copies list so that we can overwrite the current list with the items in the right order
        self.trays_to_replace_in_process = []
        for number in shortest_perm: #go over the numbers in the shortest permutation list
            for item in trays_to_replace_in_process_copy: # go over each shelve
                if number == item[3]:
                    self.trays_to_replace_in_process.append(item)

        self.server.robot_connection.message_queue.append({'type': 'route', 'route': dir_list})
        while not robot_ready:
            if robot_at_shelve: #if robot is at a shelve, do unload sequence
                #send unload/load to shelve if implemented
                cartridge_location_list = []
                for i in range(0, len(self.trays_to_replace_in_process)):
                    if self.trays_to_replace_in_process[0] == self.trays_to_replace_in_process[i]:
                        cartridge_location_list.append((self.trays_to_replace_in_process[4], self.trays_to_replace_in_process[5]))
                        del self.trays_to_replace_in_process[i]
                self.server.robot_connection.message_queue.append({'type': 'unload', 'cartridge_location': cartridge_location_list})
                self.server.robot_connection.message_queue.append({'type': 'load', 'cartridge_location': cartridge_location_list})
                robot_at_shelve = False

            
if __name__ == '__main__':
    server = Server(54321)
    server.run()

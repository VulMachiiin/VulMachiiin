import json
import threading
import time

class RobotConnection(threading.Thread):
'''Thread that runs the connection with the robot and does actions according to the messages'''
    def __init__(self, connection, cipher, server):
        threading.Thread.__init__(self)
        self.connection = connection
        self.cipher = cipher        
        self.server = server 

    def run(self):
        #robot related stuff
        json_message = {'type':'ready', 'value':True}
        self.sent(json_message)

        while True:
            json_message = self.receive()
            if json_message['type'] == 'ready':
                if json_message['value'] == True:
                    self.        
            elif json_message['type'] == 'arrived_at_target':

            elif json_message['type'] == 'unload':

            elif json_message['type'] == 'load':

    
    def receive(self):
        message = self.connection.rcv(4096)
        message = self.cipher.decrypt(message)
        
        log = open('robotconnectionlog.txt', 'a')
        log.write('{} - robot - {}'.format(time.asctime(), message.replace('\n', ' '))) #might remove the replace if using minimalistic json convertion
        log.close()

        return json.load(message)

    def sent(self, message):
        json.dumps(message, separators=(',',':'))
        
        log = open('robotconnectionlog.txt', 'a')
        log.write('{} - server - {}'.format(time.asctime(), message.replace('\n', ' ')))
        log.close()
        
        self.cipher.encrypt(message)
        self.connection.sendall(message)

class DatabaseHook(threading.Thread):

    def __init__(self, db_connection, server_processes):
        self.db_connection = db_connection
        self.server_processes = server_processes

    def run(self):
        while True:
            self.db_connection.get_query('SELECT product_id, shelve_id, x_coordinate, y_coordinate FROM productsinshelve WHERE amount_in_cartridge < 0')
            

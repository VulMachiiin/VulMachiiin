import json
import threading

from time import asctime

class RobotConnection(threading.Thread):
    def __init__(self, connection):
        threading.Thread.__init__(self)

        self.connection = connection
                
    def run(self):
        #robot related stuff

    def receive(self):
        message = self.connection.rcv(4096)
        #TODO add json convertion and AES decryption
        log = open('robotconnectionlog.txt', 'a')
        log.write('{} - robot - {}'.format(time.asctime(), message.replace('\n', ' '))) #might remove the replace if using minimalistic json convertion
        log.close()
        return message

    def sent(self, message):
        #TODO encrypt with AES
        log = open('robotconnectionlog.txt', 'a')
        log.write('{} - server - {}'.format(time.asctime(), message.replace('\n', ' ')))#might remove the replace if using minimalistic json convertion
        log.close()
        self.connection.sentall(message)


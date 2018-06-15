import usocket as socket
import threading
import json
import Encryptor
import IO_controller
class Server_Connector(threading.Thread):


    encryptor = Encryptor()
    iocontroller = IO_controller()

    def __init__(self):
        print('Creating socket')
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #TODO ip en port global
        #ciphertext = self.s.recv(4096)
        #decryptedmessage = self.do_decrypt(ciphertext))
        # Save me from the darks\

    def run(self, IP_address, port):
        self.s.connect((IP_address, port))
        print('Succesfully connected to: ', IP_address)
        # Send a 1 to the server to let it know that you're a robot
        self.send('1')
        message = self.s.receive(1024)
        json_message = {'type':'ready', 'value':True}
        self.send(json_message)
        while True:
            message = self.receive()
            if(message['type'] == 'route'):
                directions = message['routes']
                for directionlist in directions:
                    for direction in directionlist:
                        while(self.iocontroller.detect_node() == "line"):
                            pass
                        if(self.iocontroller.detect_node() == "node"):
                            # TODO draai naar dirction
                            self.iocontroller.control_motors(directions)

    def send(self, message):
        jsonmessage = json.dumps(message)
        encryptedmessage = self.encryptor.encrypt(jsonmessage)
        self.s.send(encryptedmessage)

    def receive(self):
        receivedmessage = self.s.recv(1024)
        receivedmessage = self.encryptor.decrypt(receivedmessage)
        return json.loads(receivedmessage)

from machine import Pin
from ultrasonic import Ultrasonic
from wemosSocket import clientSocket
from json_parser import Json_parser

# for testing purposes only
#clientsocket = clientSocket()
#clientsocket.connect('192.168.43.234', 34567)
json_parser = Json_parser()
parsed = json_parser('{"directions" : "FRLD", "cartridgeheight" : "3"}')

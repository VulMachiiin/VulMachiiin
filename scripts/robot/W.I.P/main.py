from machine import Pin
from server_connector import Server_connector
#from json_parser import Json_parser

# for testing purposes only
#json_parser = Json_parser()
#parsed = json_parser('{"directions" : "FRLD", "cartridgeheight" : "3"}')
server_connector = Server_connector()
server_connector.connect('192.168.0.118', 34567)

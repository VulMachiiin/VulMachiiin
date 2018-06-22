from machine import Pin
from server_connector import Server_connector
from IO_controller import IO_controller

server_connector = Server_connector()
server_connector.connect('192.168.0.118', 34567)
parsed = server_connector.parse_to_JSON('{"directions" : "FRLD", "cartridgeheight" : "3"}')

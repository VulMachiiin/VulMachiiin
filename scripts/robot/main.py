from machine import Pin
from server_connector import Server_connector
from IO_controller import IO_controller

server_connector = Server_connector('ip', 'port')
server_connector.start()

# TODO thread.start, niet run

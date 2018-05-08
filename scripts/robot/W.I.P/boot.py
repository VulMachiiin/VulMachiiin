import webrepl
from sockethandler import socketHandler
from network import WLAN
webrepl.start()
wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()
for net in nets:
    if net.ssid == 'vulmach':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, 'vulmachiiin'), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        break

clientsocket = socketHandler()
print(clientsocket.connect('192.168.0.118', 34567))

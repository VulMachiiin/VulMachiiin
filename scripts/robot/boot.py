# This file is executed on every boot (including wake-boot from deepsleep)
import gc
import webrepl
import network
import time
gc.collect()

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('vulmachin', 'test1998')
        # Try to connect for 2 seconds, after that continue program
        time.sleep(2)
    print('network config:', sta_if.ifconfig())

do_connect()

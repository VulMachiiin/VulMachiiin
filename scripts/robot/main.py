from machine import Pin
import time
laser = Pin(2, Pin.OUT)

while True:
    laser(0)
    time.sleep(1)
    laser(1)
    time.sleep(1)

from machine import Pin
from machine import Pin, time_pulse_us
from time import sleep_us
from ultrasonic import Ultrasonic
import time
laser = Pin(0, Pin.OUT)
ultrasonic = Ultrasonic()

while True:
    if(ultrasonic.measure() < 10):
        laser(0)
    else:
        laser(1)

from machine import Pin
from ultrasonic import Ultrasonic
from json_parser import Json_parser

laser = Pin(0, Pin.OUT)
ultrasonic = Ultrasonic()

# for testing purposes only
json_parser = Json_parser()
parsed = json_parser('{"directions" : "FRLD", "cartridgeheight" : "3"}')
print(parsed['directions'])

while True:
    if(ultrasonic.measure() < 10):
        laser(0)
    else:
        laser(1)

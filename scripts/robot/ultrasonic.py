from machine import Pin, time_pulse_us
import time


class Ultrasonic:
    trig = Pin(15, Pin.OUT)
    echo = Pin(13, Pin.IN)
    def __init__(self):
        print("Class initialised")

    def measure(self):
        self.trig.off()
        time.sleep_us(2)
        self.trig.on()
        time.sleep_us(10)
        self.trig.off()
        while self.echo.value() == 0:
            pass
        t1 = time.ticks_us()
        while self.echo.value() == 1:
            pass
        t2 = time.ticks_us()
        cm = (t2 - t1) / 58.0
        print(cm)
        time.sleep(0.5)
        return cm;

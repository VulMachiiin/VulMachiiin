from wiringpi import *
import Motor
import time

#Connect Ultrasonic to 5V, line detection to 3,3V!
class IO_controller():

    # Ultrasonic sensors pins
    motor1 = Motor(1,1,1)
    motor2 = Motor(1,1,1)
    motor3 = Motor(1,1,1)
    motor4 = Motor(1,1,1)

    def __init__(self, trigPin, echoPin):
        print("IO controller initialised")
        pinMode(trigPin, 1)
        pinMode(echoPin, 1)
        self.trigPin = trigPin
        self.echoPin = echoPin

    # Measure distance using ultrasonic sensor
    def measure_distance(self):
        # set Trigger to HIGH
        digitalWrite(self.trigPin, 1)
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        digitalWrite(self.trigPin, 0)
        StartTime = time.time()
        StopTime = time.time()
        # save StartTime
        while digitalRead(self.echoPin) == 0:
            StartTime = time.time()
        # save time of arrival
        while digitalRead(self.echoPin) == 1:
            StopTime = time.time()
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
        print("distance: " + distance + " cm")
        return distance

    # Detect lines and nodes
    def detect_node(self):
        value = 0
        print(value)
        if(value == 1000):
            return "line"
        elif(value == 2000):
            return "node"

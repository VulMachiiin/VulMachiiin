import RPi.GPIO as GPIO            # import RPi.GPIO module
import Motor
import time
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD

#Connect Ultrasonic to 5V, line detection to 3,3V!
class IO_controller():

    # Ultrasonic sensors pins
    motor1 = Motor(1,1,1)
    motor2 = Motor(1,1,1)
    motor3 = Motor(1,1,1)
    motor4 = Motor(1,1,1)

    def __init__(self, trigPin, echoPin):
        print("IO controller initialised")
        GPIO.setup(trigPin, GPIO.OUT)
        GPIO.setup(echoPin, GPIO.OUT)
        self.trigPin = trigPin
        self.echoPin = echoPin

    # Measure distance using ultrasonic sensor
    def measure_distance(self):
        # set Trigger to HIGH
        GPIO.output(self.trigPin, True)
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.trigPin, False)
        StartTime = time.time()
        StopTime = time.time()
        # save StartTime
        while GPIO.input(self.echoPin) == 0:
            StartTime = time.time()
        # save time of arrival
        while GPIO.input(self.echoPin) == 1:
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
        value = self.adc.read()
        print(value)
        if(value == 1000):
            return "line"
        elif(value == 2000):
            return "node"
        # If value is between somethings its a line

io  = IO_controller(18,24)
while(True):
    io.measure_distance()
    # Control the motors to make the robot turn/move forwards

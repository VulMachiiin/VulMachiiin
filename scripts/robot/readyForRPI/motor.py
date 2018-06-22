import RPi.GPIO as GPIO            # import RPi.GPIO module
from time import sleep             # lets us have a delay
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD

# Motor class
class Motor:

    # Initialises motor class
    def __init__(self, PWMpin, togglepinA, togglepinB):
        GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD
        GPIO.setup(24, GPIO.OUT)           # set GPIO24 as an output
        self.togglepinA = togglepinA
        self.togglepinB = togglepinB
        GPIO.setup(togglepinA, GPIO.OUT)
        GPIO.setup(togglepinB, GPIO.OUT)
        self.PWMpin = GPIO.setup(PWMpin, GPIO.OUT)
        self.PWMpin.start(0)
        #self.PWMpin = PWM(Pin(PWMpin))

    # Changes frequency (2000 recommended for DC motor)
    def setFrequency(self, frequency):
        self.PWMpin.ChangeFrequency(frequency)

    # Sets duty cycle
    def setDuty(self, dutycycle):
        self.PWMpin.ChangeDutyCycle(dutycycle)

    # Makes the motor turn one way
    def forward(self):
        GPIO.output(self.togglepinA, 1)
        GPIO.output(self.togglepinB, 0)

    # Makes the motor turn the opposite way
    def reverse(self):
        GPIO.output(self.togglepinA, 0)
        GPIO.output(self.togglepinB, 1)

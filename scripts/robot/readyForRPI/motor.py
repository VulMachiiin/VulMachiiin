from wiringpi import *

# Motor class
class Motor:

    # Initialises motor class
    def __init__(self, PWMpin, togglepinA, togglepinB):
        pinMode(togglepinA, togglepinB)           # set GPIO24 as an output
        self.togglepinA = togglepinA
        self.togglepinB = togglepinB
        self.PWMpin = PWMpin
        pinMode(togglepinA, 1)
        pinMode(togglepinB, 1)
        pinMode(PWMpin, 1)
        softPwmCreate(PWMpin, 0, 255)
    # Sets duty cycle
    def setDuty(self, dutycycle):
        softPwmWrite(self.PWMpin, dutycycle);

    # Makes the motor turn one way
    def forward(self):
        digitalWrite(togglepinA, 1)
        digitalWrite(togglepinB, 0)

    # Makes the motor turn the opposite way
    def reverse(self):
        digitalWrite(togglepinA, 0)
        digitalWrite(togglepinB, 1)

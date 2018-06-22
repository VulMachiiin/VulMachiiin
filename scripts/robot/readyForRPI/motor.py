from time import sleep             # lets us have a delay
import wiringpi

# Motor class
class Motor:

    # Initialises motor class
    def __init__(self, PWMpin, togglepinA, togglepinB):
        wiringpi.pinMode(24, 1)           # set GPIO24 as an output
        self.togglepinA = togglepinA
        self.togglepinB = togglepinB
        wiringpi.pinMode(togglepinA, 1)
        wiringpi.pinMode(togglepinB, 1)
        self.PWMpin = wiringpi.pinMode(PWMpin, 1)
        wiring.softPwmCreate(PWMpin, 0, )
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

from machine import PWM, Pin

# Motor class
class Motor:

    # Initialises motor class
    def __init__(self, PWMpin, togglepinA, togglepinB):
        self.togglepinA = Pin(togglepinA, PIN.OUT)
        self.togglepinB = Pin(togglepinB, PIN.OUT)
        self.PWMpin = PWM(Pin(PWMpin))

    # Changes frequency (2000 recommended for DC motor)
    def setFrequency(frequency):
        self.PWMpin.freq(frequency)

    # Sets duty cycle
    def setDuty(dutycycle):
        self.PWMpin.duty(dutycycle)

    # Makes the motor turn one way
    def forward():
        self.togglepinA.value(1)
        self.togglepinB.value(0)

    # Makes the motor turn the opposite way
    def reverse():
        self.togglepinA.value(0)
        self.togglepinB.value(1)

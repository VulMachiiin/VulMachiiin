from machine import PWM, Pin

class Motors:
	def __init__(self):
		self.enA = Pin(14, Pin.OUT) #enable
		self.pwmA = PWM(self.enA)
		self.pwmA.freq(1000)

		self.enB = Pin(25, Pin.OUT) #enable
		self.pwmB = PWM(self.enB)
		self.pwmB.freq(1000)

		self.in1 = Pin(27,Pin.OUT) 
		self.in2 = Pin(26,Pin.OUT) 
		
		self.in3 = Pin(33,Pin.OUT) 
		self.in4 = Pin(32,Pin.OUT) 
		
		print("starting")

		self.pwmA.duty(1023) #range 0-1023
		self.pwmB.duty(1023)

	def vooruit(self):
		#dc1
		self.in1.value(0) 
		self.in2.value(1)

		#dc2
		self.in3.value(1) 
		self.in4.value(0)

	def achteruit(self):
		#dc1
		self.in1.value(1) 
		self.in2.value(0)

		#dc2
		self.in3.value(0) 
		self.in4.value(1)	

	def rechts(self):
		#dc1
		self.in1.value(1) 
		self.in2.value(0)

		#dc2
		self.in3.value(1) 
		self.in4.value(0)	

	def links(self):
		#dc1
		self.in1.value(0) 
		self.in2.value(1)

		#dc2
		self.in3.value(0) 
		self.in4.value(1)	


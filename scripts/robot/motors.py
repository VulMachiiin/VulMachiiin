from machine import PWM, Pin

class Motors
	def __init__(self):
		enA = Pin(14, Pin.OUT) #enable
		pwmA = PWM(enA)
		pwmA.freq(1000)

		enB = Pin(25, Pin.OUT) #enable
		pwmB = PWM(enB)
		pwmB.freq(1000)

		in1 = Pin(27,Pin.OUT) 
		in2 = Pin(26,Pin.OUT) 
		
		in3 = pin(33,Pin.OUT) 
		in4 = pin(32,Pin.OUT) 
		
		print("starting")

		pwmA.duty(1023) #range 0-1023
		pwmB.duty(1023)
		in1.value(0) 
		in2.value(1)

	def vooruit(self):
		#dc1
		in1.value(0) 
		in2.value(1)

		#dc2
		in3.value(1) 
		in4.value(0)

	def achteruit(self):
		#dc1
		in1.value(1) 
		in2.value(0)

		#dc2
		in3.value(0) 
		in4.value(1)	

	def rechts(self):
		#dc1
		in1.value(1) 
		in2.value(0)

		#dc2
		in3.value(1) 
		in4.value(0)	

	def links(self):
		#dc1
		in1.value(0) 
		in2.value(1)

		#dc2
		in3.value(0) 
		in4.value(1)	

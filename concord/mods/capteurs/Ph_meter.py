import time
import grovepi
from threading import Thread

# Connect the Grove PH Sensor to analog port A0
# SIG,NC,VCC,GND
#http://www.phidgets.com/docs/1130_User_Guide
sensor = 0
# Reference voltage of ADC is 5v
adc_ref = 5

class Ph_Capteur(Thread):

	def __init__(self,queue):
		Thread.__init__(self)
		self.Queue = queue

	def run(self):
		while True:
			try:
				# Read sensor value
				sensor_value = grovepi.analogRead(sensor)
				# Calculate PH
				ph2 = 7 - (2.5 - sensor_value/200)/(0.257179 + 0.000941468 * 25)
				ph3 = 0.0178 * sensor_value - 1.889
				self.Queue.put(ph2)

			except IOError:
				print ("Error")
				
			time.sleep(2)

if __name__ == "__main__":
	while True:
		try:
			# Read sensor value
			sensor_value = grovepi.analogRead(sensor)
			# Calculate PH
			#ph = 7 - 1000 * (float)(sensor_value) * adc_ref / 59.16 / 1023
			ph2 = 7 - (2.5 - sensor_value/200)/(0.257179 + 0.000941468 * 25)
			ph3 = 0.0178 * sensor_value - 1.889
			print("sensor_value =", sensor_value, "test =",ph2, "test2 =",ph3)

		except IOError:
			print ("Error")
			
		time.sleep(2)


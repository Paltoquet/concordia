import time
import grovepi
from mods.utils.message import Message
from capteur import Capteur


class Ph_capteur(Capteur):

	def __init__(self,_output_,_time,_pin):
		Capteur.__init__(self,_output_,_time,_pin)

	def run(self):
		while True:
			try:
				# Read sensor value
				sensor_value = grovepi.analogRead(self.sensor)
				# Calculate PH
				ph2 = 7 - (2.5 - sensor_value/200)/(0.257179 + 0.000941468 * 25)
				ph3 = 0.0178 * sensor_value - 1.889
				msg = Message("ph_capteur",str(ph2))
				print(msg)
				self.send(Message("ph_capteur"))
			except IOError:
				print ("Error")
			time.sleep(self.time)
			
if __name__ == "__main__":
	try:
		# Read sensor value
		sensor_value = grovepi.analogRead(2)
		# Calculate PH
		#ph = 7 - 1000 * (float)(sensor_value) * adc_ref / 59.16 / 1023
		ph2 = 7 - (2.5 - sensor_value/200)/(0.257179 + 0.000941468 * 25)
		ph3 = 0.0178 * sensor_value - 1.889
		print("sensor_value =", sensor_value, "test =",ph2, "test2 =",ph3)

	except IOError:
		print ("Error")
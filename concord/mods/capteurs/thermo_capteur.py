import os
import time
from mods.utils.message import Message
from capteur import Capteur

#load the drivers
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')




def read():
	path="/sys/bus/w1/devices/28-000005f1bd6d/w1_slave"

	tfile = open(path)
	# Read all of the text in the file.
	text = tfile.read()
	# Close the file now that the text has been read.
	tfile.close()
	# Split the text with new lines (\n) and select the second line.
	secondline = text.split("\n")[1]
	# Split the line into words, referring to the spaces, and select the 10th word (counting from 0).
	temperaturedata = secondline.split(" ")[9]
	# The first two characters are "t=", so get rid of those and convert the temperature from a string to a number.
	temperature = float(temperaturedata[2:])
	# Put the decimal point in the right place and display it.
	temperature = temperature / 1000
	print temperature
	return temperature

class Thermo_capteur(Capteur):

	def __init__(self,_output,_time,_pin):
		Capteur.__init__(self,_output,_time,_pin)

	def run(self):
		while True:
			try:
				value = read()
				msg = Message("thermo_capteur",str(value))
				self.send(msg)
			except IOError:
				print ("Error")
				
			time.sleep(self.period)

			
if __name__ == "__main__":
	read()
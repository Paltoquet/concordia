import time
import grovepi
from threading import Thread
from mods.utils.message import Message


class Capteur(Thread):


	#output is where we will push or new values
	#input is where we receive information/orders
	#time the default period beetween 2 measures
	def __init__(self,_output_queue,_time,_pin):
		Thread.__init__(self)
		self.output = _output_queue
		self.period = _time
		self.sensor = _pin
		

	def run(self):
		pass
		
	def send(self,msg):
		self.output.put(msg)
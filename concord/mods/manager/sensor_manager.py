import time
import Queue
import grovepi
from threading import Thread
from mods.capteurs.thermo_capteur import Thermo_capteur
from mods.capteurs.ph_capteur import Ph_capteur
from mods.utils.message import Message


class Sensor_manager(Thread):
	def __init__(self,_db):
		Thread.__init__(self)
		self.input = Queue.Queue()
		self.sensors = {}
		self.db = _db
		thermo = Thermo_capteur(self.input,2,-1)
		ph = Ph_capteur(self.input,2,3)
		self.sensors["thermo"] = thermo
	
	def run(self):
		for sensor in self.sensors.itervalues():
			sensor.start()
		while True:
			msg = self.input.get()
			self.db.record.insert({"sensor":msg.sensor,"value":msg.value,"date":msg.date})
		
	
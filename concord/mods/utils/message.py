import time


class Message():

	def __init__(self,_capteur,_value):
		self.sensor = _capteur
		self.value = _value
		self.date = time.strftime("%x") + " " + time.strftime("%X")
		
	def __str__(self):
		return "capteur:{}, value:{}".format(self.sensor,self.value)
		
	def getObj(self):
		result = {}
		result["capteur"] = self.sensor
		result["vaue"] = self.value
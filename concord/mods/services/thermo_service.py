import logging, grovepi, time, threading
from twisted.internet import reactor
from pyupnp.event import EventProperty
from pyupnp.device import Device, DeviceIcon
from pyupnp.logr import Logr
from pyupnp.services import register_action, Service, ServiceActionArgument, ServiceStateVariable
from pyupnp.ssdp import SSDP
from pyupnp.upnp import UPnP
import os

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
    return temperature

class Thermo_Service(Service):
    version = (1, 0)
    serviceType = "urn:schemas-upnp-org:service:TemperatureService:1"
    serviceId = "urn:upnp-org:serviceId:ConcordiaTemperatureService"

    actions = {
        'GetTemperature': [
            ServiceActionArgument('Temp','out','TempValue')
        ],
    }
    
    stateVariables = [
        # Variables
        ServiceStateVariable('TempValue','string',sendEvents=True),
        ServiceStateVariable('ListeningTemp','boolean',sendEvents=True)

    ]
        
    state=EventProperty('ListeningTemp', 0)
    temp=EventProperty('TempValue', "0")

    @register_action('GetTemperature')
    def getTemp(self):
        return {
            'Temp' : str(self.temp)
        }
        
    def listen_to_temp_sensor(self, s):
        print "Listening for temp sensor values"
        while True:
            try:
                self.temp = read()
                print('{}] Temp value  =  {}'.format(time.strftime("%H:%M:%S"), self.temp))
                time.sleep(3)
            except IOError as e:
                print "I/O error({0}): {1}".format(e.errno, e.strerror)
                time.sleep(0.5)
        return
        
        
    def startListening(self):
        self.state = True
        self.thread = threading.Thread(target=Thermo_Service.listen_to_temp_sensor, args = (self,0))
        self.thread.daemon = True
        self.thread.start();
        return {
            'ListeningTemp':True
        }

            
if __name__ == "__main__":
    thermo = Thermo_Service()
    thermo.startListening()
    input()
    read()
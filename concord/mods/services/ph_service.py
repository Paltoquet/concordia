import logging, grovepi, time, threading
from twisted.internet import reactor
from pyupnp.event import EventProperty
from pyupnp.device import Device, DeviceIcon
from pyupnp.logr import Logr
from pyupnp.services import register_action, Service, ServiceActionArgument, ServiceStateVariable
from pyupnp.ssdp import SSDP
from pyupnp.upnp import UPnP

sensor = 0
def read_ph():
    sensor_value = grovepi.analogRead(sensor)
    # Calculate PH
    ph2 = 7 - (2.5 - sensor_value/200)/(0.257179 + 0.000941468 * 25)
    #ph3 = 0.0178 * sensor_value - 1.889
    return ph2

class Ph_Service(Service):
    version = (1, 0)
    serviceType = "urn:schemas-upnp-org:service:PhService:1"
    serviceId = "urn:upnp-org:serviceId:ConcordiaPhService"

    actions = {
        'GetPh': [
            ServiceActionArgument('Ph','out','PhValue')
        ]
    }
    
    stateVariables = [
        # Variables
        ServiceStateVariable('PhValue','string',sendEvents=True),
        ServiceStateVariable('ListeningPh','boolean',sendEvents=True)

    ]
        
    state = EventProperty('ListeningPh', 0)
    ph = EventProperty('PhValue', '0')

    @register_action('GetPh')
    def getState(self):
        self.ph = int(self.ph)
        return {
            'Ph' : str(self.ph)
        }
        
    def listen_to_ph_sensor(self, s):
        print "Listening for ph sensor values"
        while True:
            try:
                self.ph = read_ph()
                print('Ph value = ' + self.ph)
                time.sleep(3)
            except IOError as e:
                print "I/O error({0}): {1}".format(e.errno, e.strerror)
                time.sleep(0.5)
        return
        
        
    def startListening(self):
        self.state=True
        self.ph = 0
        self.thread = threading.Thread(target=Ph_Service.listen_to_ph_sensor, args = (self,0))
        self.thread.daemon = True
        self.thread.start();
        return {
            'ListeningPh':True
        }

            
if __name__ == "__main__":
    print(read_ph())
import logging, grovepi, time, threading
from twisted.internet import reactor
from pyupnp.event import EventProperty
from pyupnp.device import Device, DeviceIcon
from pyupnp.logr import Logr
from pyupnp.services import register_action, Service, ServiceActionArgument, ServiceStateVariable
from pyupnp.ssdp import SSDP
from pyupnp.upnp import UPnP

sensor = 2
def read_light():
    sensor_value = grovepi.analogRead(sensor)
    return sensor_value

class Light_Service(Service):
    version = (1, 0)
    serviceType = "urn:schemas-upnp-org:service:LightService:1"
    serviceId = "urn:upnp-org:serviceId:ConcordiaLightService"

    actions = {
        'GetLight': [
            ServiceActionArgument('Light','out','LightValue')
        ]
    }
    
    stateVariables = [
        # Variables
        ServiceStateVariable('LightValue','string',sendEvents=True),
        ServiceStateVariable('ListeningLight','boolean',sendEvents=True)

    ]
        
    state = EventProperty('ListeningLight', 0)
    ph = EventProperty('LightValue', '0')

    @register_action('GetLight')
    def getState(self):
        self.light = int(self.light)
        return {
            'Light' : str(self.light)
        }
        
    def listen_to_light_sensor(self, s):
        print "Listening for light sensor values"
        while True:
            try:
                self.light = read_light()
                print('{}] Light value =  {}'.format(time.strftime("%H:%M:%S"), self.light))
                time.sleep(3)
            except IOError as e:
                print "I/O error({0}): {1}".format(e.errno, e.strerror)
                time.sleep(0.5)
        return
        
        
    def startListening(self):
        self.state=True
        self.light = 0
        self.thread = threading.Thread(target=Light_Service.listen_to_light_sensor, args = (self,0))
        self.thread.daemon = True
        self.thread.start();
        return {
            'ListeningLight':True
        }

            
if __name__ == "__main__":
    print(read_light())
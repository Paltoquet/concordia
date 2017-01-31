import logging, grovepi, time, threading
from twisted.internet import reactor
from pyupnp.event import EventProperty
from pyupnp.device import Device, DeviceIcon
from pyupnp.logr import Logr
from pyupnp.services import register_action, Service, ServiceActionArgument, ServiceStateVariable
from pyupnp.ssdp import SSDP
from pyupnp.upnp import UPnP

grove_vcc = 5
adc_ref = 5
full_angle = 300

sensor = 1


def read_potar():
    sensor_value = grovepi.analogRead(sensor)
    voltage = round((float)(sensor_value) * adc_ref / 1023, 2)
    degrees = round((voltage * full_angle) / grove_vcc, 2)
    return degrees

class Potar_Service(Service):
    version = (1, 0)
    serviceType = "urn:schemas-upnp-org:service:PotarService:1"
    serviceId = "urn:upnp-org:serviceId:ConcordiaPotarService"

    actions = {
        'GetPotar': [
            ServiceActionArgument('Potar', 'out', 'PotarValue')
        ]
    }

    stateVariables = [
        # Variables
        ServiceStateVariable('PotarValue', 'string', sendEvents=True),
        ServiceStateVariable('ListeningPotar', 'boolean', sendEvents=True)
    ]

    state = EventProperty('ListeningPotar', 0)
    potar = EventProperty('PotarValue', '0')

    @register_action('GetPotar')
    def getState(self):
        return {
            'Potar' : str(self.potar)
        }

    def listen_to_potar_sensor(self, s):
        print "Listening for potar sensor values"
        while True:
            try:
                self.potar = read_potar()
                print('Potar value = ' + self.potar)
                time.sleep(3)
            except IOError as e:
                print "I/O error({0}): {1}".format(e.errno, e.strerror)
                time.sleep(0.5)
        return

    def startListening(self):
        self.state=True
        self.thread = threading.Thread(target=Potar_Service.listen_to_potar_sensor, args = (self,0))
        self.thread.daemon = True
        self.thread.start();
        return {
            'ListeningPotar':True
        }

if __name__ == "__main__":
    print(read_potar())
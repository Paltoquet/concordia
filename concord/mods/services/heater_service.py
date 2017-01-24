import logging, grovepi, time, threading
from twisted.internet import reactor
from pyupnp.event import EventProperty
from pyupnp.device import Device, DeviceIcon
from pyupnp.logr import Logr
from pyupnp.services import register_action, Service, ServiceActionArgument, ServiceStateVariable
from pyupnp.ssdp import SSDP
from pyupnp.upnp import UPnP

relay = 4

class Heater_Service(Service):
    version = (1, 0)
    serviceType = "urn:schemas-upnp-org:service:HeaterService:1"
    serviceId = "urn:upnp-org:serviceId:heaterService"

    actions = {
        'Turn_On_Heater': [
            ServiceActionArgument('heater_is_on','out','Heater_on')
        ]
        ,
        'Turn_Off_Heater': [
            ServiceActionArgument('heater_is_on','out','Heater_on')
        ]
    }

    stateVariables = [
        # Variables
        ServiceStateVariable('Heater_on','boolean',sendEvents=True),
    ]

    Heater_on = EventProperty('Heater_on')

    # Relay pin
    grovepi.pinMode(relay, 'OUTPUT')

    @register_action('Turn_On_Heater')
    def Turn_On_Heater(self):
        grovepi.digitalWrite(relay, 1)
        self.Heater_on = 1
        return {
            'heater_is_on' : True
        }

    @register_action('Turn_Off_Heater')
    def Turn_Off_Heater(self):
        grovepi.digitalWrite(relay, 0)
        self.Heater_on = 0
        return {
            "heater_is_on" : False
        }

if __name__ == "__main__":
    grovepi.pinMode(relay, 'OUTPUT')
    grovepi.digitalWrite(relay, 1)
    time.sleep(2)
    grovepi.digitalWrite(relay, 0)

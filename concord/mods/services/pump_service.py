import logging, grovepi, time, threading
from twisted.internet import reactor
from pyupnp.event import EventProperty
from pyupnp.device import Device, DeviceIcon
from pyupnp.logr import Logr
from pyupnp.services import register_action, Service, ServiceActionArgument, ServiceStateVariable
from pyupnp.ssdp import SSDP
from pyupnp.upnp import UPnP

PUMP_RELAY = 7
PUMP_TIME_MAX = 1

class Pump_Service(Service):
    version = (1, 0)
    serviceType = "urn:schemas-upnp-org:service:PumpService:1"
    serviceId = "urn:upnp-org:serviceId:ConcordiaPumpService"

    actions = {
        'Turn_On_Pump': [
            ServiceActionArgument('pump_is_on', 'out', 'Pump_on')
        ]
        ,
        'Turn_Off_Pump': [
            ServiceActionArgument('pump_is_on', 'out', 'Pump_on')
        ]
    }

    stateVariables = [
        # Variables
        ServiceStateVariable('Pump_on', 'boolean', sendEvents=True),
    ]

    Pump_on = EventProperty('Pump_on')

    # Relay pin
    grovepi.pinMode(PUMP_RELAY, 'OUTPUT')

    @register_action('Turn_On_Pump')
    def Turn_On_Pump(self):
        grovepi.digitalWrite(PUMP_RELAY, 1)
        self.Pump_on = 1
        """
        time.sleep(PUMP_TIME_MAX)
        grovepi.digitalWrite(PUMP_RELAY, 0)
        self.Pump_on = 0
        """

    @register_action('Turn_Off_Pump')
    def Turn_Off_Pump(self):
        print("a\na\na\na\na")
        grovepi.digitalWrite(PUMP_RELAY, 0)
        self.Pump_on = 0

if __name__ == "__main__":
    grovepi.pinMode(PUMP_RELAY, 'OUTPUT')
    grovepi.digitalWrite(PUMP_RELAY, 1)
    time.sleep(PUMP_TIME_MAX)
    grovepi.digitalWrite(PUMP_RELAY, 0)

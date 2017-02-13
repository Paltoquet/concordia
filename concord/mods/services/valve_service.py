import logging, grovepi, time, threading
from twisted.internet import reactor
from pyupnp.event import EventProperty
from pyupnp.device import Device, DeviceIcon
from pyupnp.logr import Logr
from pyupnp.services import register_action, Service, ServiceActionArgument, ServiceStateVariable
from pyupnp.ssdp import SSDP
from pyupnp.upnp import UPnP

VALVE_RELAY = 5
VALVE_TIME_MAX = 1

class Valve_Service(Service):
    version = (1, 0)
    serviceType = "urn:schemas-upnp-org:service:ValveService:1"
    serviceId = "urn:upnp-org:serviceId:ConcordiaValveService"

    actions = {
        'Turn_On_Valve': [
            ServiceActionArgument('valve_is_on', 'out', 'Valve_on')
        ]
        ,
        'Turn_Off_Valve': [
            ServiceActionArgument('valve_is_on', 'out', 'Valve_on')
        ]
    }

    stateVariables = [
        # Variables
        ServiceStateVariable('Valve_on', 'boolean', sendEvents=True),
    ]

    Valve_on = EventProperty('Valve_on')

    # Relay pin
    grovepi.pinMode(VALVE_RELAY, 'OUTPUT')

    @register_action('Turn_On_Valve')
    def Turn_On_Valve(self):
        grovepi.digitalWrite(VALVE_RELAY, 1)
        self.Valve_on = 1
        time.sleep(VALVE_TIME_MAX)
        grovepi.digitalWrite(VALVE_RELAY, 0)
        self.Valve_on = 0

    @register_action('Turn_Off_Valve')
    def Turn_Off_Valve(self):
        grovepi.digitalWrite(VALVE_RELAY, 0)
        self.Valve_on = 0

if __name__ == "__main__":
    grovepi.pinMode(VALVE_RELAY, 'OUTPUT')
    grovepi.digitalWrite(VALVE_RELAY, 1)
    time.sleep(VALVE_TIME_MAX)
    grovepi.digitalWrite(VALVE_RELAY, 0)

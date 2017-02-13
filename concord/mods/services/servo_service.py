import logging, grovepi, time, threading
from twisted.internet import reactor
from pyupnp.event import EventProperty
from pyupnp.device import Device, DeviceIcon
from pyupnp.logr import Logr
from pyupnp.services import register_action, Service, ServiceActionArgument, ServiceStateVariable
from pyupnp.ssdp import SSDP
from pyupnp.upnp import UPnP
import os



def write(value):
    path="/dev/servoblaster"
    tfile = open(path, "a")
    tfile.write(value)
    tfile.close()

class Servo_Service(Service):
    version = (1, 0)
    serviceType = "urn:schemas-upnp-org:service:ServoService:1"
    serviceId = "urn:upnp-org:serviceId:ConcordiaServoService"

    actions = {
        'Turn_On_Servo': [
            ServiceActionArgument('servo_is_on', 'out', 'Servo_on')
        ]
        ,
        'Turn_Off_Servo': [
            ServiceActionArgument('servo_is_on', 'out', 'Servo_on')
        ]
    }
    
    stateVariables = [
        # Variables
        ServiceStateVariable('Servo_on', 'boolean', sendEvents=True),
    ]
        
    Servo_on = EventProperty('Servo_on')

    @register_action('Turn_On_Servo')
    def Turn_On_Servo(self):
        write("\n2=-10\n")
        self.Servo_on = 1
        
    @register_action('Turn_Off_Servo')
    def Turn_Off_Servo(self):
        write("\n2=200\n")
        # tfile = open(PATH, "a")
        # tfile.write("\n2=200")
        # tfile.close()
        self.Servo_on = 0

if __name__ == "__main__":
    tfile = open(PATH, "a")
    tfile.write("\n2=-10")
    time.sleep(1)
    time.sleep(1)
    #tfile.write("\n2=200")
    #time.sleep(1)
    #time.sleep(1)
    tfile.close()
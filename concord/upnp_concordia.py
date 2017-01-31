from twisted.internet import reactor
from pyupnp.event import EventProperty
from pyupnp.device import Device, DeviceIcon
from pyupnp.logr import Logr
from pyupnp.services import register_action, Service, ServiceActionArgument, ServiceStateVariable
from pyupnp.ssdp import SSDP
from pyupnp.upnp import UPnP
from mods.services.thermo_service import Thermo_Service
from mods.services.ph_service import Ph_Service
from mods.services.pump_service import Pump_Service
from mods.services.heater_service import Heater_Service
from mods.services.potar_service import Potar_Service

import logging, time, grovepi

class Concordia(Device):
    deviceType = 'urn:schemas-upnp-org:device:Concordia:1'
    friendlyName = "The Diving Concord"
    
    def __init__(self):
        Device.__init__(self)
        self.uuid = '2fac1234-31f8-11b4-a222-08002b34c002'
        self.icons = [DeviceIcon('image/jpeg', 300, 300, 24, 'https://a1-images.myspacecdn.com/images03/34/78bfe9e1349146dca67e9b7eab9e76f4/300x300.jpg')]
        
        # Declare services
        self.thermo_service = Thermo_Service()
        self.ph_service = Ph_Service()
        self.pump_service = Pump_Service()
        self.heater_service = Heater_Service()
        self.potar_service = Potar_Service()

        # Register services
        self.services = [
            self.thermo_service,
            self.ph_service,
            self.pump_service,
            self.heater_service,
            self.potar_service
        ]

        # Start services listening to sensors
        self.thermo_service.startListening()
        self.ph_service.startListening()
        self.potar_service.startListening()

if __name__ == '__main__':
    Logr.configure(logging.DEBUG)

    device = Concordia()

    upnp = UPnP(device)
    ssdp = SSDP(device)

    upnp.listen()
    ssdp.listen()
    reactor.run()

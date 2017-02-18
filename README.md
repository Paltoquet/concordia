# concordia

Serveur tournant sur la raspberry, nous mettons à dispotions une liste de webservice respectant le protocole `UPnP`

###Capteurs: 
- Temperature °C
- Ph 
- Potar [0-300]
- Light lux

###Actionneurs:
  * Pump: pour actionner/éteindre la pompe 
  * ServoMoteur: Pour augmenter/réduire l'intensité de la lumière ou l'éteindre sans vous préocupez de son état actuel
  * Heater: pour allumer/éteindre le chauffage
  * Valve: Pour ouvrir/fermer l'électrovalve

##Installation et mise en place

- clonez notre répertoire
- clonez le répertoire [https://github.com/fuzeman/PyUPnP] servant de librarie pour utiliser UPnP
- ajouter le au projet, à la racine
- run `python upnp_concordia.py`

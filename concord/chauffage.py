import time
import grovepi

relay = 2

Grovepi.pinmode(relay,"OUTPUT")


if __name__ == "__main__":
	Grovepi.digitalWrite(relay,0)
	time.seep(2)
	Grovepi.digitalWrite(relay,1)
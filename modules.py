from machine import Pin
from time import sleep
import dht
buzz=Pin(2,Pin.OUT)
#flame
def getFlameVal():
    return not Pin(5,Pin.IN).value()

def getTempHumid():
    temp = dht.DHT11(Pin(4))
    temp.measure()
    return [temp.temperature(),temp.humidity()]

def getPirVal():
    return Pin(18,Pin.IN).value()

class Relay():
    def __init__(self, ps0,ps1,ps2,ps3):
        self.ps0=ps0
        self.ps1=ps1
        self.ps2=ps2
        self.ps3=ps3
        self.status=[not ps0.value(),not ps1.value(),not ps2.value(),not ps3.value()]
    def update(self,switches:list):
        self.ps0.value(not switches[0])
        self.ps1.value(not switches[1])
        self.ps2.value(not switches[2])
        self.ps3.value(not switches[3])
        self.status=[not self.ps0.value(),not self.ps1.value(),not self.ps2.value(),not self.ps3.value()]

relay = Relay(Pin(32,Pin.OUT),Pin(33,Pin.OUT),Pin(25,Pin.OUT),Pin(26,Pin.OUT))
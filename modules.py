from machine import Pin
from time import sleep
import dht,ujson
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
        jsn=open('config.json')
        jsn.seek(0)
        config=ujson.loads(jsn.read())
        jsn.close()
        self.ps0=ps0
        self.ps1=ps1
        self.ps2=ps2
        self.ps3=ps3
        self.status=[not ps0.value(),not ps1.value(),not ps2.value(),not ps3.value()]
        config['s0'] = False if config['s0'] == 'False' else True
        config['s1'] = False if config['s1'] == 'False' else True
        config['s2'] = False if config['s2'] == 'False' else True
        config['s3'] = False if config['s3'] == 'False' else True
        self.update([config['s0'], config['s1'], config['s2'],config['s3']])
    def update(self,switches:list):
        self.ps0.value(not switches[0])
        self.ps1.value(not switches[1])
        self.ps2.value(not switches[2])
        self.ps3.value(not switches[3])
        self.status=[not self.ps0.value(),not self.ps1.value(),not self.ps2.value(),not self.ps3.value()]
        s=f'"s0":"{str(bool(switches[0]))}","s1":"{str(bool(switches[1]))}","s2":"{str(bool(switches[2]))}","s3":"{str(bool(switches[3]))}"'
        s="{"+s+"}"
        jsn=open('config.json','w')
        jsn.seek(0)
        jsn.write(s)
        jsn.close()


relay = Relay(Pin(32,Pin.OUT),Pin(33,Pin.OUT),Pin(25,Pin.OUT),Pin(26,Pin.OUT))
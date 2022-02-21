from machine import Pin, SoftI2C
import ssd1306
from time import sleep
import dht
import machine
import network


class Flame:
    def __init__(self, pin):
        self.val=pin.value()
    def getval(self):
        return self.val


#wifi connect

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
	print('connecting to network...')
	wlan.connect('Amaan', '9013393120')
	while not wlan.isconnected():
		pass
	print('network config:', wlan.ifconfig())



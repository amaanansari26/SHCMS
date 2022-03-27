from machine import Pin

import os,ssd1306,dht,machine,network,socket,math,ujson,time

deviceId=846
filelist=os.listdir()
if 'config.json' not in filelist:
    jsn=open('config.json','w')
    jsn.write('{"s0":false,"s1":false,"s2":false,"s3":false')
    jsn.close()


if 'wific.json' not in filelist:
    wific=open('wific.json','w')
    wific.write('{"SSID":"Amaan","PASS":"9013393120"}')
    wific.close()


#wifi connect
wific=open('wific.json')
wific.seek(0)
wific=ujson.loads(wific.read())
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
	print('connecting to network...')
	wlan.connect(wific['SSID'],wific['PASS'])
	while not wlan.isconnected():
		pass
	print('network config:', wlan.ifconfig())

import modules as m
# m.relay.update([0,0,0,0])  



import webrepl
webrepl.start()
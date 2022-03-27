import machine, time, os, network, socket, math, dht, ujson, urequests, _thread
import modules as m
lockmode=False
def get():
    try:
        fdata=urequests.get('https://shcmsmgm.herokuapp.com/device/846')
        if fdata.text:
            config=ujson.loads(fdata.text)
            m.relay.update([int(config['s0']),int(config['s1']),int(config['s2']),int(config['s3'])])
            lockmode=bool(int(config['s4']))
        fdata.close()
        print('get success')
    except:
        print('get fail try in next loop')

def post(emergency=0):
    try:
        fireEmergency= True if emergency==1 or emergency ==3 else False
        theftEmergency= True if emergency==2 or emergency ==3 else False
        #temphumid=m.getTempHumid()
        temphumid=[25,50]
        out={"temp":temphumid[0],"humid":temphumid[1], "fireEmergency": fireEmergency, "theftEmergency":theftEmergency}
        print(out)
        res = urequests.post('https://shcmsmgm.herokuapp.com/device/846', headers = {'content-type': 'application/json'}, data = ujson.dumps(out)).close()
        print('post success')
    except:
        print('post failed try in next loop')
def emergency():
    print('Emergency check')

    flame=int(m.getFlameVal())
    pir= 2 if m.getPirVal==1 else 0
    print("flame: ")
    print(flame)
    print("pir: ")
    print(pir)
    if lockmode:
        print('lockdown trigger')
        print('lockdown return value:'+(flame+pir))
        return flame+pir
    print('return value:')
    print(flame)
    return flame
def postEmergency(emergencyVal):
    if emergencyVal==2:
        m.relay.update[0,0,0,0]
    print('Emergency value')
    print(emergencyVal)
    post(emergencyVal)

def getReset():
    try:
        fdata=urequests.get('https://shcmsmgm.herokuapp.com/device/846')
        print('inside get reseet')
        if fdata.text:
            config=ujson.loads(fdata.text)
            print(config)
            reset=config['s5']
        fdata.close()
        if reset:
            rst=urequests.get('https://shcmsmgm.herokuapp.com/device/846/reset')
            rst.close()
        return reset
    except:
        print('get fail try in next loop')

def start():
    emergencyVal=emergency()
    if not emergencyVal:
        post()
        get()
    else:
        while True:
            print('Emegency mode')
            m.buzz.on()
            postEmergency(emergencyVal)
            if getReset():
                m.buzz.off()
                break

        

        
        
while True:
    start()
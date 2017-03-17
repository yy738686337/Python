import threading
import time
import random
import datetime
import json
import requests

WIFI_PROBE = 1000
WIFI_PROBE_ID = set()
WIFI_AP_SSID = ('hello1', 'hello2', 'hello3')
MAC_TABLE = ['mac' + str(i) for i in range(5000)]
wifi_info = {}


def createData(wifi_info):
    wifi_info['data'] = {
        'mac': random.choice(MAC_TABLE),
        'rssi': random.uniform(-100, 0),
        'range': random.randrange(0, 30),
        'ts': random.choice(WIFI_AP_SSID),
        'tc': random.choice((True, False)),
        'ds': random.choice((True, False)),
        'tmc':'fffffffff',
        'essid':'ssssssss',
        'time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    jsonEncode = json.dumps(wifi_info)
    requests.post('http://127.0.0.1:5000/post', data={'a':jsonEncode})
    # print ""
    # sql = """
    #       INSERT INTO data(probe_id,probe_mac,rate,wssid,wmac,time,lat,lon,addr,phone_mac,phone_rssi,phone_range,phone_cssid, ts,ds,essid)
    #         VALUES('{}','{}',)
    #       """.format()



def createWifiInfo(wifi_info, id):
    wifi_info['id'] = id
    wifi_info['rate'] = 1
    wifi_info['mmac'] = 'ffffff'
    wifi_info['wssid'] = 'ffffff'
    wifi_info['addr'] = '......'
    wifi_info['lat'] = '30.748093'
    wifi_info['lon'] = '103.973083'


def wifiProbe(id):
    if id not in WIFI_PROBE_ID:
        WIFI_PROBE_ID.add(id)
        createWifiInfo(wifi_info, id)
        createData(wifi_info)
    else:
        createData(wifi_info)


def main():
    while True:
        for i in range(WIFI_PROBE):
            t = threading.Thread(target=wifiProbe, args=(i,))
            t.setDaemon(False)
            t.start()
        t.join()
        time.sleep(1)

probe_info = {
}

if __name__ == '__main__':
    main()
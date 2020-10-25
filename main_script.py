from datetime import datetime
from wifi import Cell
import random, time, json
while True:
    c = list(Cell.all('wlo1'))[0]
    params = open('params.json', 'r')
    if params.read() == '':
        params = open('params.json', 'w')
        params.write(json.dumps({'SSID': c.ssid, 'Mac': c.address, 'RSSI': c.signal}))
        params.close()
        log = open('log.txt', 'a')
        log.write('SSID: {0}, Mac: {1}, RSSI: {2} at {3} \n'.format(c.ssid, c.address, c.signal, datetime.now().time()))
        log.close()
    else:
        params = open('params.json', 'r')
        params_dict = json.loads(params.read())
        if (params_dict['SSID'] != c.ssid) | (params_dict['Mac'] != c.address) | (params_dict['RSSI'] != c.signal):
            log = open('log.txt', 'a')
            log.write('SSID: {0}, Mac: {1}, RSSI: {2} at {3} \n'.format(c.ssid, c.address, c.signal, datetime.now().time()))
            params.close()
            log.close()
            params = open('params.json', 'w')
            params.write(json.dumps({'SSID': c.ssid, 'Mac': c.address, 'RSSI': c.signal}))
            params.close()
            print('SSID: {0}, Mac: {1}, RSSI: {2} at {3} \n'.format(c.ssid, c.address, c.signal, datetime.now().time()))
            time.sleep(10)

from datetime import datetime
from wifi import Cell
import random, time, json, os, sys, subprocess
from detect2 import main
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        label_b = tk.Label(self, text="Возможно ваше соединение небезопасно. \nЗапустить углубленную проверку точки доступа на легитимность?", font='20')
        label_a = tk.Label(self, text="")
        yes = tk.Button(self, text ="Да", font='20', command=click_yes)
        label_d = tk.Label(self, text="", fg="blue")
        no = tk.Button(self, text ="Нет", font='20', command=self.destroy)
        label_f = tk.Label(self, text="",  fg="orange")
        opts = { 'padx': 10, 'pady': 10, 'fill': tk.BOTH }
        label_b.pack(side=tk.TOP)
        label_a.pack(side=tk.TOP, ipadx = "60", ipady="100")
        yes.pack(side=tk.LEFT, **opts, ipadx = "90", ipady="20")
        label_d.pack(side=tk.LEFT)
        no.pack(side=tk.RIGHT, **opts, ipadx = "90", ipady="300")
        label_f.pack(side=tk.TOP, padx='300', pady="300")



def click_yes():
    subprocess.call(['sudo airmon-ng start ' + WIname], shell=True)
    print(main(WIname+"mon", False))



WIname = input('Введите название своего сетевого интерфейса (узнать можно с помощью iwconfig):')
while True:
    c = list(Cell.all(WIname))[0]
    params = open('params.json', 'r')
    if params.read() == '':
        params = open('params.json', 'w')
        params.write(json.dumps({'SSID': c.ssid, 'Mac': c.address, 'RSSI': c.channel}))
        params.close()
        log = open('log.txt', 'a')
        log.write('SSID: {0}, Mac: {1}, RSSI: {2} at {3} \n'.format(c.ssid, c.address, c.channel, datetime.now().time()))
        log.close()
    else:
        params = open('params.json', 'r')
        params_dict = json.loads(params.read())
        if (params_dict['SSID'] != c.ssid) | (params_dict['Mac'] != c.address) | (params_dict['RSSI'] != c.channel):
            log = open('log.txt', 'a')
            log.write('SSID: {0}, Mac: {1}, RSSI: {2} at {3} \n'.format(c.ssid, c.address, c.channel, datetime.now().time()))
            params.close()
            log.close()
            params = open('params.json', 'w')
            params.write(json.dumps({'SSID': c.ssid, 'Mac': c.address, 'RSSI': c.channel}))
            params.close()
            print('SSID: {0}, Mac: {1}, RSSI: {2} at {3} \n'.format(c.ssid, c.address, c.channel, datetime.now().time()))

            app = App()
            app.geometry('640x360')
            app.mainloop()

            time.sleep(10)

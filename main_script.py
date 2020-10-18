from wifi import Cell, Scheme

c = list(Cell.all('wlo1'))[0]
print("SSID: {}".format(c.ssid))
print("Mac: {}".format(c.address))
print("RSSI: {}".format(c.signal))
# https://www.youtube.com/watch?v=dQw4w9WgXcQ

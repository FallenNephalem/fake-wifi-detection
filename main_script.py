from wifi import Cell, Scheme
print(Cell.all('wlo1'))

c = list(Cell.all('wlo1'))[0]
print("SSID: {}".format(c.ssid))
print("Mac: {}".format(c.address))
print("signal: {}".format(c.signal))
print("quality: {}".format(c.quality))
# https://www.youtube.com/watch?v=b_os0Gxs4e8
# https://issue.life/questions/53246654
# https://xakep.ru/2018/11/09/wifi-hack/

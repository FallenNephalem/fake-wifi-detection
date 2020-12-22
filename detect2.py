

from scapy.all import *
from multiprocessing import Process
from termcolor import colored
import time, random,sys

logo = """"                                                                                     
    Если вы видите эту надпись то программа начала работу (^-^)
                                                                                    
"""
packets_list = []
target_wifi_mac = []
target_device_mac = []
def detect_attack():
    #print(len(packets_list))
    if (len(packets_list) >= 250):
        i = 0
        deauth = 0
        disassoc = 0
        for i in range(len(packets_list)):
            if("deauth" in packets_list[i]):
                deauth = deauth + 1
            if("disassoc" in packets_list[i]):
                disassoc = disassoc + 1
        if(deauth > disassoc * 2):
            print(colored("[+] ", "green", attrs=['bold']) + str(datetime.now().strftime("%a, %d, %b %Y %H:%M:%S %Z")) + colored(" Airgeddon ", "green", attrs=['bold']) + "Target Wi-Fi: " + target_wifi_mac[0] + " Target Device: " + target_device_mac[0])
            packets_list[:] = []
            target_wifi_mac[:] = []
            target_device_mac[:] = []
    elif(len(packets_list) >= 2):
        i = 0
        deauth = 0
        disassoc = 0
        for i in range(len(packets_list)):
            if("deauth" in packets_list[i]):
                deauth = deauth + 1
            if("disassoc" in packets_list[i]):
                disassoc = disassoc + 1
        if(deauth == disassoc):
            print(colored("[+] ", "yellow", attrs=['bold']) + str(datetime.now().strftime("%a, %d, %b %Y %H:%M:%S %Z")) + colored(" MDK3 ", "yellow", attrs=['bold']) + " Target Wi-Fi: " + target_wifi_mac[0] + " Target Device: " + target_device_mac[0])
        elif(deauth < disassoc):
            print(colored("[+] ", "yellow", attrs=['bold']) + str(datetime.now().strftime("%a, %d, %b %Y %H:%M:%S %Z")) + colored(" Unknown ", "yellow", attrs=['bold']) + " Target Wi-Fi: " + target_wifi_mac[0] + " Target Device: " + target_device_mac[0])
            packets_list[:] = []
            target_wifi_mac[:] = []
            target_device_mac[:] = []

def sniff_packets(pkt):
    detect_attack()
    if pkt.haslayer(Dot11):
        if pkt.type == 0 and pkt.subtype == 0x00c:
            target_wifi_mac.append(pkt.addr2.upper())
            target_device_mac.append(pkt.addr1.upper())
            packets_list.append("deauth")
        if pkt.type == 0 and pkt.subtype == 0x00a:
            target_wifi_mac.append(pkt.addr2.upper())
            target_device_mac.append(pkt.addr1.upper())
            packets_list.append("disassoc")

def change_channel(iface):
    while True:
        channel = random.randrange(1,12)
        os.system("iw dev %s set channel %d" % (iface, channel))
        time.sleep(0.3)
def main(iface):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    p1 = Process(target=change_channel, args=(iface,))
    p1.start()
    sniff(iface = iface, prn=sniff_packets)
        

if __name__ == "__main__":
    if len(sys.argv)==2:
        main(sys.argv[1])
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("[X] Error", "red"))
        print(colored("[X] Input command: python detect_deauth.py <MONITOR MODE INTERFACE>", "white"))
        print(colored("[X] Example: python detect_deauth.py wlan0mon", "white"))



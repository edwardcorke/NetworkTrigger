import getmac
import time

def mapNetwork():
    for x in range(255):
        search = "192.168.0." + str(x)
        print(search + ": " + str(getmac.get_mac_address(ip=search)))

def detectDevice(ipAddress, macAddress):
    while True:
        mac = getmac.get_mac_address(ip=ipAddress)
        if mac == macAddress:
            msg = "Device (" + ipAddress + ") has joined the network"
            print(msg)
            return
        else:
            time.sleep(1)

detectDevice("192.168.0.30", "36:00:2d:da:49:ae")

import uos
import network
import sys

print("Python version: {version}\nVersion Info: {info}"
      .format(version=sys.version, info=sys.version_info))

print("-----------------------")

print("sysname: {sysname}\nnodename: {nodename}\nrelease: {release}\nversion: {version}\nmachine: {machine}"
      .format(sysname=uos.uname().sysname, nodename=uos.uname().nodename, release=uos.uname().release,
              version=uos.uname().version, machine=uos.uname().machine))

print("-----------------------")

print("WIFI Networks\n")

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

for ap in wifi.scan():
    print(ap)
    
print("-----------------------")

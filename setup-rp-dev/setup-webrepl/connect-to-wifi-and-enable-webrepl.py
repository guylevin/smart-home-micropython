import network
from time import sleep

host_name = ''
ssid = ''
wifi_pass = ''
webrepl_pass = ''

routercon = network.WLAN(network.STA_IF)

routercon.active(False)

# Check status and turn on if needed
if routercon.active() == False:
    routercon.active(True)

routercon.config(dhcp_hostname=host_name)
print(routercon.config('dhcp_hostname'))

# Connect wifi
routercon.connect(ssid, wifi_pass)

while routercon.isconnected() == False:
  pass

print('Connection successful')
print(routercon.ifconfig())

import webrepl
webrepl.start(password=webrepl_pass)

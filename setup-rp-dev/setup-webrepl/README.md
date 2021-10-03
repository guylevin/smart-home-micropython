# Set up webrepl for development over wifi

## 1. Open Thonny
Open Thonny By Clicking on `Applications Menu -> Programming -> Thonny Python IDE`

## 2. Install websockets
* Click on `Tools -> Manage Plugins`
* Search for `websockets` 
* Install
* Restart Thonny

![image](https://user-images.githubusercontent.com/4077233/135772915-ee69d84d-ef60-47cd-b688-785b4aab1027.png)

* Copy the content of 
Run [Connect to wifi and enable webrepl](connect-to-wifi-and-enable-webrepl.py) 
and run

This script should print the IP addresss of the device, keep it for the next step

  
## Connect to WebREPL

* Click on `Run->Select Interpreter`  
* Select `MicroPython (ESP32)` 
* Select `WebREPL`
* Set URL, port and password
* OK

![image](https://user-images.githubusercontent.com/4077233/135772906-e14866cb-db57-474d-b81e-dd9b234962f1.png)

Now you can develop from Wifi

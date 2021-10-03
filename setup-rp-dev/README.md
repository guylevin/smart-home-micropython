# Setup Raspberry Pi and ESP32 for MicroPython Development

## 1. Enable the serial port

* Go to the `Applications Menu -> Preferences -> Raspberry Pi Configuration -> Interfaces -> Enable the Serial Port`   

![image](https://user-images.githubusercontent.com/4077233/135768655-914697f8-98cb-416e-89df-de14aee2aed1.png)  
  
* Restart the device  

  
## 2. Install MicroPython Firmware
(This is an example for esp32, for other devices select the right configuration)

Download the firmware
* Go to https://micropython.org/download/  
* Select `Generic ESP32 module` under `Espressif ESP-based boards`

* The page says   
![image](https://user-images.githubusercontent.com/4077233/135769042-c66bd798-ff25-465c-aa19-0d00c0cdcc2f.png)  
So select and download the latest v4

## 3. Get Thonny Ready
* Open Thonny By Clicking on `Applications Menu -> Programming -> Thonny Python IDE`
* Click on `Switch to regular mode` and restart Thonny  

### 3.1. Install esptools
* Click on `Tools -> Manage Plugins`
* Search for `esptool` 
* Install
* Restart Thonny

![image](https://user-images.githubusercontent.com/4077233/135770331-e19aec3b-2d64-4da8-9637-bd274b777ef5.png)


### 3.2. Install Firmware
* Click on `Run->Select Interpreter`  
* Select `MicroPython (ESP32)`  
* Click on `Install and update firmware`  

![image](https://user-images.githubusercontent.com/4077233/135769708-e5a89a29-952f-4f8b-9295-40d581bdf725.png)

* Connect the device with a USB cabale to the raspbery pi
* Select the correct port
* Select the firmware file
* Click Install

![image](https://user-images.githubusercontent.com/4077233/135770254-62e60503-4009-4cde-8111-ac6cb0f69d44.png)

## Test the connection

* Click on `Run->Select Interpreter`  
* Select `MicroPython (ESP32)` 
* Select port
* OK

![image](https://user-images.githubusercontent.com/4077233/135771562-790c27ce-dfec-42a2-b113-54f8616252b7.png)

* Copy and paste this test python code and run  
[Print Device Info](print-device-info.py)



For setting up development using wifi see [Setup webREPL](setup-webrepl/)




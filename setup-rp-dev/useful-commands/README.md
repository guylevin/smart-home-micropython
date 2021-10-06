
# Useful Commands For ESP Development

## esptool

Install  
`pip3 install esptool`  

Get port and other information about the device  
`esptool.py read_mac`

Erase Device  
`esptool.py -p <port name> erase_flash`

Install Firmware  
`esptool.py --port /dev/ttyUSB0 --baud 1000000 write_flash --flash_size=4MB -fm dio 0  ./Downloads/esp8266-20210902-v1.17.bin`  
  
    
## ampy

Install  
`pip install adafruit-ampy`

List files  
`ampy -p <port> ls`

Upload files  
`ampy -p <port> put <local file or folder> <remote path (optional)>`

Recieve Files  
`ampy -p <port> get <remote file or folder> <Local path>`

Create a directory  
`ampy -p <port> mkdir <remote directory path>`

Remove file  
`ampy -p <port> rm <remote file path>`

Remove a directory  
`ampy -p <port> rmdir <remote directory path>`

Run a file  
`ampy -p <port> run <local file path>`

Reset the device  
`ampy -p <port> reset`


## Thonny

Open files menu  
`View -> Files`

Copy a file to the device  
`Right click on a file -> Upload to /`  

![image](https://user-images.githubusercontent.com/4077233/135897162-921c8d12-fef7-442d-a49e-0ea5b4328fef.png)


Remove a file from the device  
`Right click on a file -> Delete`  

![image](https://user-images.githubusercontent.com/4077233/135897013-7a42e5fa-4f6a-4d99-aaf0-81b6df203ba3.png)


# xrpwifidrive

## setup
1. using [xrpcode](https://xrpcode.wpi.edu/), connect to device, update firmware (if prompted) and write all files to device (file > new file)
2. update `secrets.json` with `robot_id` (it cannot collide with another)
	* optionally update `config.py` to change wifi information
3. select `code.py` and run it
4. now you should be able to disconnect from usb and it should keep running after power cycle (board "reset" button)
5. connect to network ssid with password (see `config.py`)
	* you might need to disable cellular or prevent disconnecting from the network
6. navigate to `http://192.168.4.1:80` on the device, there should be a joystick
7. use joystick for drive, slider for arm servo
	* if controls don't work, try reloading the page or pressing "reset" on the device
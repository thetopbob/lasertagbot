# LaserTagBot - Robots that can play Laser Tag!

This application enables robots with the right equipment to paticipate in a game of Laser Tag!

## Kit
### Main Kit
 - [Raspberry Pi](https://thepihut.com/collections/raspberry-pi/products/raspberry-pi-zero)
 - Wi-Fi connection (Built into the Raspberry Pi Zero)
 - Power (requirements TBC)
 - Breadboard (for modelling)
### Weapons Subsystem
 - ADS1115 (Analogue converter to receive IR input)
 - IR receiver (x2)
 - IR LED (any IR LED will do)
 - PN2222 transistor
 - 100ohm resistor
 - [Micro Servo](https://thepihut.com/products/9g-micro-servo-1-6kg)
 - Servo driver possibly this one that has the [PCA9685](https://thepihut.com/products/adafruit-16-channel-12-bit-pwm-servo-driver-i2c-interface-pca9685)
 - 2.54mm pitch terminal for the above (to supply power)
### Control Subsytem
 - Requirements TBC
### Drive Subsystem
 - L293D H bridge motor driver
 - DC Motors (x2)

## Installation
We've made installing everything you need to get started with our browser controlled robot easy!

	git clone https://github.com/thetopbob/lasertagbot.git
	cd lasertagbot
	make install

## Usage
Running the project is easy. From your Raspberry Pi command line, run the following:

	python3 newwebbot.py

Once running, the software will display a web address for you to connect to. By default, and for security purposes, the software will only initially allow connections from the web browser running on the Raspberry Pi by visiting http://localhost:5000

If you know what you're doing, and would like to expose the interface to all devices running on your network, then run the software using the following:

	python3 newwebbot.py -i 0.0.0.0

This will allow you to control the robot from any device on the same network as your Raspberry Pi at http://raspberrypi.lan:5000

### Control
Once connected in your browser, by default, you can use the following keys on your keyboard to control the robot:

- Arrow keys for forwards, backwards, left turn and right turn
- 'f' to fire the IR LED
- 'c' key to capture and display an image from the camera if connected
- 'u' key to turn on/off an ultrasonic distance measurement every 2 seconds

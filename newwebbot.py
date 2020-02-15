#!/usr/bin/env python3

import os, logging, subprocess, time, argparse
from py_irsend import irsend # module required for sending IR signal
from bottle import route, request, response, redirect, hook, error, default_app, view, static_file, template, HTTPError
from gpiozero import CamJamKitRobot
import board
import busio

i2c = busio.I2C(board.SCL, board.SDA)

import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

@route('/left')
def action_left():
	robot.left()
	time.sleep(0.2)
	robot.stop()
	return "LEFT TURN"

@route('/right')
def action_right():
	robot.right()
	time.sleep(0.2)
	robot.stop()
	return "RIGHT TURN"

@route('/forward')
@route('/forwards')
def action_forward():
	robot.forward()
	time.sleep(0.2)
	robot.stop()
	return "FORWARDS"

@route('/back')
@route('/backward')
def action_back():
	robot.backward()
	time.sleep(0.2)
	robot.stop()
	return "BACKWARDS"

@route('/irinput')
def irinput():
	ads = ADS.ADS1115(i2c)
	chan1 = AnalogIn(ads, ADS.P0)
	if chan1.value < 20000:
		return "!!!! I'M HIT !!!! {:5d}".format(chan1.value)
	else:
		return "No hit {:5d}".format(chan1.value)


@route('/fireLED')
def fireLED():
	irsend.send_once('Samsung_BN59-00516A_TV', ['KEY_POWER'])
	return "WEAPON FIRED!"

@route('/')
def index():
	return static_file('index.html', root='public')

@route('/style.css')
def index():
	return static_file('style.css', root='public')

if __name__ == '__main__':

	parser = argparse.ArgumentParser()

	# Server settings
	parser.add_argument("-i", "--host", default=os.getenv('IP', '127.0.0.1'), help="IP Address")
	parser.add_argument("-p", "--port", default=os.getenv('PORT', 5000), help="Port")

	# Verbose mode
	parser.add_argument("--verbose", "-v", help="increase output verbosity", action="store_true")
	args = parser.parse_args()

	if args.verbose:
		logging.basicConfig(level=logging.DEBUG)
	else:
		logging.basicConfig(level=logging.INFO)
	log = logging.getLogger(__name__)

	try:
		robot = CamJamKitRobot()
		robot.stop()
	except Exception as e:
		log.error(e)
		exit()

	try:
		app = default_app()
		app.run(host=args.host, port=args.port, server='tornado')
	except:
		log.error("Unable to start server on {}:{}".format(args.host, args.port))

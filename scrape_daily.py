#!/usr/bin/env python3
"""
This program scrapes Forecast.io's weather API to get the current 7-day forecast.
The current forecast is saved, as a .json file, to $PWD/dataset/daily$CURTIME.json.
"""

import sys, os
import time
import json
from forecastiopy import *

import code #DEBUG

API_KEY = open("FORECASTIO_API_KEY.txt").read().strip()
DATA_PATH = "./dataset" # TODO: take from os.environ or from sys.argv

montreal = [45.5, -73.566667]
def main(location=montreal):

	#code.InteractiveConsole(locals=locals()).interact()
	if not os.path.isdir(DATA_PATH):
		os.mkdir(DATA_PATH) # XXX this doesn't handle if the path exists but is a file quite right

	fio = ForecastIO.ForecastIO(API_KEY, latitude=location[0], longitude=location[1])
	d = FIODaily.FIODaily(fio)
	with open(os.path.join(DATA_PATH, "daily%d.json" % (time.time()*1000,)), "w") as save:
		json.dump(d.data, save, indent=1, sort_keys=True)


if __name__=='__main__':
	main()

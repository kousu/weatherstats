
from forecastiopy import *

YOUR_API_KEY = open("FORECASTIO_API_KEY.txt").read().strip()

montreal = [45.5, -73.566667]
location=montreal

fio = ForecastIO.ForecastIO(YOUR_API_KEY, latitude=location[0], longitude=location[1])
current = FIOCurrently.FIOCurrently(fio)
print('Temperature:', current.temperature)
print('Precipitation Probability:', current.precipProbability)

Weather error bars
==================

A data-science collaboration between @kousu and @cannonshard to attempt to independently investigate the accuracy of weather forecasting around the world.

Plan
====

As for what data to scrape, we want the following information every day:

* Temp/forecast predictions for the day (For Montreal & Toronto respectively. We will be doing two seperate analyses just for validity's sake. We can generalize across other climates/cities later)
* Temp/forecast predictions 1 day in advance (Montreal & Toronto)
* Temp/forecast predictions 2 days in advance
* ''...3 days in advance
* ''...4 days in advance
* ''...5 days in advance
* ''...6 days in advance
* ''...7 days in advance

We will obtain historical data later on, right now we need to scrap info daily.

We should use consistent weather stations- preferably ones closer to the downtown core (or closer to our addresses, respectively)

Interestingly, Forecast.io (and others?) encode precipitation as a probabilistic value
Maybe that means we can evaluate the efficacy of these predictions.

Code
====

To run this code you need a Forecast.io API key. Sign up at developers.forecast.io (or something like that).
Put the API key in `FORECASTIO_API_KEY.txt` by itself; this file is explicitly hidden from the repo by `.gitignore`

https://github.com/bitpixdigital/forecastiopy3
this isn't on pip, so to install:
* ```$ git clone --depth 1 https://github.com/bitpixdigital/forecastiopy3.git
$ cd forecastiopy3
$ python3 setup.py install --user
$ # to test it worked:
$ python3
>>> import forecastiopy
```


This was the other one:
https://github.com/ZeevG/python-forecast.io


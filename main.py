__author__ = "Christophe AUBERT"
__copyright__ = "Copyright 2016"
__credits__ = ["Christophe AUBERT"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Christophe AUBERT"
__status__ = "development"

import pyb
from MoistureSensor import MoistureSensor

print("Start program test moisture sensor")

sensor = MoistureSensor()

while True:
    print("humidity : " + str(sensor.measure()))
    print("humidity : " + str(sensor.rawMeasure()))
    pyb.delay(1000)


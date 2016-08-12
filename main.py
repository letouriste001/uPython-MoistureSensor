import pyb
from MoistureSensor import MoistureSensor

print("Start program test moisture sensor")

sensor = MoistureSensor()

while True:
    print("humidity : " + str(sensor.measure()))
    pyb.delay(1000)


uPython-MoistureSensor
=============

This module provides a device driver for MoistureSensor on microPython board.

Moisture Sensor For Arduino Automatic Watering System

Description:

This is a summary of the moisture sensor can be used to detect soil moisture, when the soil water, the analog value of the sensor output will decrease, and vice versa will increase. Using this sensor make an automatic watering system, when you are not at home or over a long period of time watering, it can sense whether your plants already thirsty. Prevent plants withered know that this is caused by lack of water. With Arduino controller to make your plants more comfortable, garden smarter.
 
Sensor surface made of metal processing, it can extend its life. Insert it into the soil, then read it using the AD converter. In its help, the plant will remind you: I want to drink, please give me a little water to drink me.

Technical Specification:

TODO modifier les specification pour le 3.3V

Supply voltage: 3.3V or 5V
Working current: less than 20mA
Output voltage: 0-2.3V [2.3V voltage values are completely immersed in the water], 5V power supply, the greater the humidity, the greater the output voltage.
Sensor Type: Analog Output
Interface definition: 1 signal, 2  power positive, 3 GND
Life: approximately 1 year (surface gold processing, enhanced electrical conductivity and corrosion resistance)
Module size: 20 X 60mm

Hack the arduino sensor for pyboard
Use 3.3v

You can check more about the microPython project here: http://micropython.org/

```
Sensor pin | board pin
-----------+----------
    VDD    |    3.3v
    DTA    |    X11
    GND    |    GND
```

Installation
------------
There are two files:
* MoistureSensor.py - the module implementing communication with the sensor

The simplest installation way is to follow these steps (Linux):

1. Connect your microPython board to your PC using a USB cable
2. Mount the device pointing to the board (/dev/sdb1 in my case)
  ```
  mkdir ~/tmp
  sudo mount /dev/sdb1 ~/tmp
  ```
3. copy MoistureSensor.py and main.py files to the board
  ```
  sudo cp MoistureSensor.py main.py ~/tmp
  ```
4. Unmount the device
  ```
  sudo umount ~/tmp
  ```
5. Restart your microPython board


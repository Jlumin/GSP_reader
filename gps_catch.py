# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:58:30 2020

@author: Luming
"""


import serial
import time
import string
import pynmea2
gps_nmea=["$GPGAA","$GPGSV","$GPGLL","$GPRMC","$GPVTG"]
with open('../test.txt','wb') as f:
    while True:
        port="/dev/ttyAMA0"
        ser=serial.Serial(port, baudrate=9600, timeout=1)
        dataout = pynmea2.NMEAStreamReader()
        newdata=ser.readline()
        f.write(newdata)
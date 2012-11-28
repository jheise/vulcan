#!/usr/bin/env python

################################################
# Module:   servo.py
# Created:  2 April 2008
# Author:   Brian D. Wendt
#   http://principialabs.com/
# Version:  0.2
# License:  GPLv3
#   http://www.fsf.org/licensing/
'''
Provides a serial connection abstraction layer
for use with Arduino "MultipleServos" sketch.
'''
################################################

import serial
from time import sleep
trigger = chr(9)
laser = chr(8)
start = chr(255)
on = chr(1)
off = chr(0) 

usbport = '/dev/ttyACM0'
#usbport = '/dev/ttyACM1'
#usbport = '/dev/tty.usbmodemfd4121'
#usbport = '/dev/tty.usbmodemfd14131'
ser = serial.Serial(usbport, 9600, timeout=1)
firingInterval = .25
#print ser

def readline():
    print ser.readline()

def startfire():
    #ser.write(start)
    #ser.write(trigger)
    #ser.write(on)
    #ser.write("%s,%s,%s\n"% (start,trigger,on))
    ser.write('255,9,1\n')

def stopfire():
    #ser.write(start)
    #ser.write(trigger)
    #ser.write(off)
    ser.write('255,9,0\n')


def fire(count=1):
    stopfire()
    startfire()
    print "sleeping for %s" % (firingInterval * count)
    sleep(firingInterval * count)
    stopfire()


def startlaser():
    #ser.write(start)
    #ser.write(laser)
    #ser.write(on)
    ser.write('255,8,1\n')

def stoplaser():
    #ser.write(start)
    #ser.write(laser)
    #ser.write(off)
    ser.write('255,8,0\n')

#!/usr/bin/env python
import struct
import vulcan

BUTTON_EVENT = 1
AXIS_EVENT = 2

laser = False

class Event:
    def __init__(self,timestamp,value,etype,number):
        self.timestamp = timestamp
        self.value = value
        self.type = etype
        self.number = number

    def printEvent(self):
        print( "Event Received: " )
        print( "\tTime Stamp %s" % self.timestamp)
        print( "\tValue %s" % self.value)
        print( "\tType %s" % self.type)
        print( "\tnumber %s" % self.number)
    
def handleEvent(event):
    global laser
    if event.type  == BUTTON_EVENT:
        if event.value == 1:
            #print( "Button %s pressed" % event.number)
            if event.number == 0:
                vulcan.startfire()
                print( "Commencing fire.")
            if event.number == 1:
                if laser:
                    vulcan.stoplaser()
                    laser = False
                    print("Deactivating laser.")
                else:
                    vulcan.startlaser()
                    laser = True
                    print("Activating laser.")
        if event.value == 0:
            #print( "Button %s released" % event.number)
            if event.number == 0:
                vulcan.stopfire()
                print( "Ceasing fire.")

    #if event.type == AXIS_EVENT:
        #print("axis %s %s" % (event.number,event.value))

vulcan.readline()
vulcan.stopfire()
vulcan.stoplaser()

joystruct = struct.Struct("<IHBB")
running = True
joystick = open('/dev/input/js0')
while running:
    message = joystick.read(8);
    event  = Event(*joystruct.unpack(message))
    handleEvent(event)

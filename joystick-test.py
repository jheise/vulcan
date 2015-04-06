#!/usr/bin/env python

import joystick

def consume_joystick():
    event = None
    print "waiting for events"
    while True:
        event = (yield)
        print event

stick = joystick.Joystick()
stick_consume = consume_joystick()
stick_consume.send(None)
for x  in stick.messages:
    stick_consume.send(x)

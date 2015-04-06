import struct

BUTTON_EVENT = 1
AXIS_EVENT = 2

BUTTON_ON = 1
BUTTON_OFF = 0

TRIGGER = 0
LASER_BUTTON = 1
THIRD_BUTTON = 2

JOYSTRUCT = struct.Struct("<IHBB")

class Event(object):
    """
    Object to represent a joystick event
    """

    def __init__(self, timestamp, value, etype, number):
        super(Event, self).__init__()
        self.timestamp = timestamp
        self.value = value
        self.type = etype
        self.number = number

    def __str__(self):
        return "EventType {0}, Value {1}, Number{2}, Timestamp {3}".format( self.type, self.value, self.number, self.timestamp)


class ButtonEvent(Event):
    """
    Class for handling Button events
    """
    def __init__(self, timestamp, value, etype, number):
        super(ButtonEvent, self).__init__(timestamp, value, etype, number)

    def __str__(self):
        return "ButtonEventType {0}, Value {1}, Number{2}, Timestamp {3}".format( self.type, self.value, self.number, self.timestamp)

class TriggerEvent(ButtonEvent):
    def __init__(self, timestamp, value, etype, number):
        super(TriggerEvent, self).__init__(timestamp, value, etype, number)

    def __str__(self):
        return "TriggerEventType {0}, Value {1}, Number{2}, Timestamp {3}".format( self.type, self.value, self.number, self.timestamp)

class TriggerDownEvent(TriggerEvent):
    def __init__(self, timestamp, value, etype, number):
        super(TriggerDownEvent, self).__init__(timestamp, value, etype, number)

    def __str__(self):
        return "TriggerDownEventType {0}, Value {1}, Number{2}, Timestamp {3}".format( self.type, self.value, self.number, self.timestamp)

class TriggerUpEvent(TriggerEvent):
    def __init__(self, timestamp, value, etype, number):
        super(TriggerUpEvent, self).__init__(timestamp, value, etype, number)

    def __str__(self):
        return "TriggerUpEventType {0}, Value {1}, Number{2}, Timestamp {3}".format( self.type, self.value, self.number, self.timestamp)

class LaserButtonEvent(ButtonEvent):
    def __init__(self, timestamp, value, etype, number):
        super(LaserButtonEvent, self).__init__(timestamp, value, etype, number)

    def __str__(self):
        return "LaserEventType {0}, Value {1}, Number{2}, Timestamp {3}".format( self.type, self.value, self.number, self.timestamp)

class LaserButtonOffEvent(LaserButtonEvent):
    def __init__(self, timestamp, value, etype, number):
        super(LaserButtonOffEvent, self).__init__(timestamp, value, etype, number)

    def __str__(self):
        return "LaserDownOffType {0}, Value {1}, Number{2}, Timestamp {3}".format( self.type, self.value, self.number, self.timestamp)

class LaserButtonOnEvent(LaserButtonEvent):
    def __init__(self, timestamp, value, etype, number):
        super(LaserButtonOnEvent, self).__init__(timestamp, value, etype, number)

    def __str__(self):
        return "LaserOnEventType {0}, Value {1}, Number{2}, Timestamp {3}".format( self.type, self.value, self.number, self.timestamp)

class AxisEvent(Event):
    """
    class to handle movement events
    """
    pass



class Joystick(object):
    """
    Object to represent a joystick
    """

    def __init__(self, path="/dev/input/js0"):
        self.joy_handle = open(path)

    @property
    def messages(self):
        while True:
            message = self.joy_handle.read(8)
            event = None
            timestamp, value, etype, number = JOYSTRUCT.unpack(message)
            if etype == BUTTON_EVENT:
                if number == TRIGGER:
                    if value == BUTTON_OFF:
                        event = TriggerUpEvent(timestamp, value, etype, number)
                    if value == BUTTON_ON:
                        event = TriggerDownEvent(timestamp, value, etype, number)
                if number == LASER_BUTTON:
                    if value == BUTTON_OFF:
                        event = LaserButtonOffEvent(timestamp, value, etype, number)
                    elif value == BUTTON_ON:
                        event = LaserButtonOnEvent(timestamp, value, etype, number)
            else:
                event = AxisEvent(timestamp, value, etype, number)

            yield event

import serial
from time import sleep
TRIGGER = chr(9)
LASER = chr(8)
START = chr(255)
ON = chr(1)
OFF = chr(0)

class Vulcan(object):
    """
    Class to wrap around ardunio controlling a modified Nerf Vulcan
    """

    #usbport = '/dev/ttyACM0'
    #usbport = '/dev/ttyACM1'
    #usbport = '/dev/tty.usbmodemfd4121'
    #usbport = '/dev/tty.usbmodemfd14131'
    def __init__(self, usbport="/dev/ttyACM0", interval=.25):
        super(Vulcan, self).__init__()
        self.usbport = usbport
        self.serial_con = serial.Serial(usbport, 9600, timeout=1)
        self.interval = interval
        self.laser = False

        # do a readline on the serial connection
        self.serial_con.readline()


    def __str__(self):
        return "Vulcan: {0}, Firing interval {1}".format(self.usbport,
                                                         self.interval)

    def __repr__(self):
        return "Vulcan(usbport={0},interval={1})".format(self.usbport,
                                                         self.interval)
    def readline(self):
        return self.serial_con.readline()

    def start_fire(self):
        self.serial_con.write('255,9,1\n')

    def stop_fire(self):
        self.serial_con.write('255,9,0\n')


    def fire(self, count=1):
        self.stop_fire()
        self.start_fire()
        sleep(self.interval* count)
        self.stop_fire()


    def start_laser(self):
        self.serial_con.write('255,8,1\n')
        self.laser = True

    def stop_laser(self):
        self.serial_con.write('255,8,0\n')
        self.laser = False

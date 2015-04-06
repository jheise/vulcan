import logging
import sys
import joystick

class EventProcessor(object):
    """
    take events from a given joystick and process them on the vulcan
    """

    def __init__(self, joystick, vulcan):
        super(EventProcessor, self).__init__()
        self.joystick = joystick
        self.vulcan = vulcan
        #formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        #console = logging.StreamHandler(sys.stdout)
        #console.setFormatter(formatter)
        #self.log.addHandler(console)
        logging.basicConfig( handlers=[logging.StreamHandler(sys.stdout)],
                                       level=logging.INFO)
        self.log = logging.getLogger("VulcanControl")
        self.log.info("Vulcan Online")

    def run(self):
        self.log.info("Listening for joystick events...")
        for message in self.joystick.messages:
            #if message.is_button_event():
            if isinstance(message, joystick.ButtonEvent):
                if isinstance(message, joystick.LaserButtonEvent):
                    if self.vulcan.laser:
                        self.vulcan.stop_laser()
                        self.log.info("Stopping laser.")
                    else:
                        self.log.info("Starting laser.")
                        self.vulcan.start_laser()

                if isinstance(message, joystick.TriggerEvent):
                    if isinstance(message, joystick.TriggerDownEvent):
                        self.log.info("Commencing fire...")
                        self.vulcan.start_fire()
                    elif isinstance(message, joystick.TriggerUpEvent):
                        self.log.info("Ceasing fire...")
                        self.vulcan.stop_fire()

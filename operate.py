#!/usr/bin/env python

import joystick
import vulcan
import eventprocessor
import logging
import argparse
import sys

def main(processor):
    processor.run()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Control program for Nerf Vulcan")
    parser.add_argument("--vulcan", default="/dev/ttyACM0", help="Path to vulcan ardiuno")
    parser.add_argument("--joystick", default="/dev/input/js0", help="Path to joystick")
    args = parser.parse_args()

    new_vulcan = vulcan.Vulcan(args.vulcan)
    new_joystick = joystick.Joystick(args.joystick)

    processor = eventprocessor.EventProcessor(new_joystick, new_vulcan)

    main(processor)

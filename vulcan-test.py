#!/usr/bin/env python
import vulcan
import time

def main():
    vc = vulcan.Vulcan()
    print "doing readline"
    vc.readline()
    print "Test Fire 1"
    vc.fire()

    print "Testing burst fire"
    for x in range(10):
        vc.fire()
        time.sleep(1)

    print "Testing laser"
    vc.start_laser()
    time.sleep(5)
    vc.stop_laser()


if __name__ == "__main__":
    main()

#!/usr/bin/python

import mouse_control
import wordament
import time
import sys

test = "queedoorkoobenac"

print test[0:4]
print test[4:8]
print test[8:12]
print test[12:16]

result = wordament.solve(test)

x = 2
for r in result:
    m = mouse_control.Mouse(75, (700,700))
    m.do_pattern(r[2])
    print r[0]
    print "::"
    print test[0:4]
    print test[4:8]
    print test[8:12]
    print test[12:16]
    print "--------"
    time.sleep(0.3)
    x = x-1
    if x == 0:
        sys.exit(0)


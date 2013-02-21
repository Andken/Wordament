#!/usr/bin/python

from delta import *

print "test start"

status1, x, y, z = delta_calcForward(.001,.001,.001)
status2, t1, t2, t3 = delta_calcInverse(x,y,z)

print status1, x, y, z
print status2, t1, t2, t3



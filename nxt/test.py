#!/usr/bin/python

from DeltaRobot import *

print "test start"

#x, y, z = delta_calcForward(0.0,0.0,-5.0)
t1, t2, t3 = delta_calcInverse(0.0,0.0,-5.0)
#x2, y2, z2 = delta_calcForward(t1, t2, t3)
#print x, y, z
print t1, t2, t3
#print x2, y2, z2


#!/usr/bin/python

import random
from delta import *

def test(x, y, z):
#    print "################"
#    print x, y, z
    status2, t1, t2, t3 = delta_calcInverse(x,y,z)
    status1, x, y, z = delta_calcForward(t1,t2,t3)
#    print status2, t1, t2, t3
#    print status1, x, y, z

    return status2 + status1

print "test start"
#test(0.0, 0.0, -12.9085629805)
#test(0.0, 0.0, -16.9085629805)

max_x = -500
max_y = -500
max_z = -500
min_x = 500
min_y = 500
min_z = 500

possible_vals = []

for x in range(10000):
    x = random.uniform(-17.5,17.5)
    y = random.uniform(-17.5,17.5)
    z = int(random.uniform(-35,-1))

    if test(x,y,z) == 0:
        if(x > max_x):
            max_x = x
        if(y > max_y):
            max_y = y
        if(z > max_z):
            max_z = z
        if(x < min_x):
            min_x = x
        if(y < min_y):
            min_y = y
        if(z < min_z):
            min_z = z
        possible_vals.append((x,y,z))
    

print possible_vals
print len(possible_vals)
print "x: (%f - %f)" % (min_x, max_x)
print "y: (%f - %f)" % (min_y, max_y)
print "z: (%f - %f)" % (min_z, max_z)


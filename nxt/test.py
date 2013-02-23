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

possible_vals = []

for x in range(10000):
    x = random.uniform(-17.5,17.5)
    y = random.uniform(-17.5,17.5)
    z = random.uniform(-35.0,0.0)

    if test(x,y,z) == 0:
        possible_vals.append((x,y,z))
    

print possible_vals
print len(possible_vals)

#!/usr/bin/python

import matplotlib
import pylab
import random
from delta import *
from math import ceil
from math import floor

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

for x in range(100000):
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
    

#print possible_vals
#print len(possible_vals)
print "x: (%f - %f)" % (min_x, max_x)
print "y: (%f - %f)" % (min_y, max_y)
print "z: (%f - %f)" % (min_z, max_z)

#for z in range(-24,-22):
for z in range(int(floor(min_z)), int(ceil(max_z))):
    x_points = []
    y_points = []
    for point in possible_vals:
        if(round(point[2]) == z):
            x_points.append(point[0])
            y_points.append(point[1])

    matplotlib.pyplot.figure()
    matplotlib.pyplot.scatter(x_points,y_points)
    matplotlib.pyplot.title("z = %f" % z)
    matplotlib.pyplot.xlim(floor(min_x),ceil(max_x))
    matplotlib.pyplot.ylim(floor(min_y),ceil(max_y))

matplotlib.pyplot.show()

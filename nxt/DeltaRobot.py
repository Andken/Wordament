#!/usr/bin/python

from math import pi
from math import sin
from math import cos
from math import tan
from math import atan
from math import sqrt
import sys

# adapted from: http://www.rjmcnamara.com/wp-content/uploads/2010/12/DeltaRobot/DeltaRobot.C

# robot geometry
# The units are Lego units
e = 12.0     # end effector
f = 23.0     # base
re = 22.0
rf = 8.0
 
# trigonometric constants
# const float sqrt3 = sqrt(3.0)
# const float pi = 3.141592653    # PI
# const float sin120 = sqrt3/2.0   
# const float cos120 = -0.5        
# const float tan60 = sqrt3
# const float sin30 = 0.5
# const float tan30 = 1/sqrt3
 
# forward kinematics: (theta1, theta2, theta3) -> (x0, y0, z0)
def delta_calcForward(theta1, theta2, theta3):
    t = (f-e)*tan(pi/6)/2
 
    y1 = -(t + rf*cos(theta1))
    z1 = -rf*sin(theta1)
    
    y2 = (t + rf*cos(theta2))*sin(pi/6)
    x2 = y2*tan(pi/3)
    z2 = -rf*sin(theta2)

    y3 = (t + rf*cos(theta3))*sin(pi/6)
    x3 = -y3*tan(pi/3)
    z3 = -rf*sin(theta3)

    dnm = (y2-y1)*x3-(y3-y1)*x2
    
    w1 = y1*y1 + z1*z1
    w2 = x2*x2 + y2*y2 + z2*z2
    w3 = x3*x3 + y3*y3 + z3*z3
     
    # x = (a1*z + b1)/dnm
    a1 = (z2-z1)*(y3-y1)-(z3-z1)*(y2-y1)
    b1 = -((w2-w1)*(y3-y1)-(w3-w1)*(y2-y1))/2.0
 
    # y = (a2*z + b2)/dnm
    a2 = -(z2-z1)*x3+(z3-z1)*x2
    b2 = ((w2-w1)*x3 - (w3-w1)*x2)/2.0
 
    # a*z^2 + b*z + c = 0
    a = a1*a1 + a2*a2 + dnm*dnm
    b = 2*(a1*b1 + a2*(b2-y1*dnm) - z1*dnm*dnm)
    c = (b2-y1*dnm)*(b2-y1*dnm) + b1*b1 + dnm*dnm*(z1*z1 - re*re)
  
    # discriminant
    d = b*b - 4.0*a*c
    if (d < 0):
        # non-existing point
        sys.exit(1)
 
    z0 = -0.5*(b+sqrt(d))/a
    x0 = (a1*z0 + b1)/dnm
    y0 = (a2*z0 + b2)/dnm
    return theta1, theta2, theta3
 
 
# inverse kinematics
# helper functions, calculates angle theta1 (for YZ-pane)
def delta_calcAngleYZ(x0, y0, z0):
    y1 = -0.5 * 0.57735 * f # f/2 * tg 30
    y0 -= 0.5 * 0.57735    * e    # shift center to edge
    # z = a + b*y
    a = (x0*x0 + y0*y0 + z0*z0 +rf*rf - re*re - y1*y1)/(2*z0)
    b = (y1-y0)/z0
    # discriminant
    d = -(a+b*y1)*(a+b*y1)+rf*(b*b*rf+rf) 
    if (d < 0):
        # non-existing point
        sys.exit(2)

    yj = (y1 - a*b - sqrt(d))/(b*b + 1) # choosing outer point
    zj = a + b*yj
    theta = atan(-zj/(y1 - yj)) + pi if(yj>y1) else 0.0
    return theta
 
 
# inverse kinematics: (x0, y0, z0) -> (theta1, theta2, theta3)
# returned status: 0=OK, -1=non-existing position
def delta_calcInverse(x0, y0, z0):
    theta1 = delta_calcAngleYZ(x0, y0, z0)
    theta2 = delta_calcAngleYZ(x0*cos(2*pi/3) + y0*sin(2*pi/3), y0*cos(2*pi/3)-x0*sin(2*pi/3), z0)  # rotate coords to +120 deg
    theta3 = delta_calcAngleYZ(x0*cos(2*pi/3) - y0*sin(2*pi/3), y0*cos(2*pi/3)+x0*sin(2*pi/3), z0)  # rotate coords to -120 deg
    return theta1, theta2, theta3


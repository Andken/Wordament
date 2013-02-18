#!/usr/bin/python

import sin, cos, sqrt, atan from math
import settings as s
import sys

# adapted from: http:#www.rjmcnamara.com/wp-content/uploads/2010/12/DeltaRobot/DeltaRobot.C



# forward kinematics: (theta1, theta2, theta3) -> (x0, y0, z0)
# returned status: 0=OK, -1=non-existing position
def delta_calcForward(theta1, theta2, theta3): #, float &x0, float &y0, float &z0) {
    t = (s.F-s.E)*s.TAN30/2
    dtr = s.PI/180.0
 
    theta1 *= dtr
    theta2 *= dtr
    theta3 *= dtr
 
    y1 = -(t + s.RF*cos(theta1))
    z1 = -s.RF*sin(theta1)
 
    y2 = (t + s.RF*cos(theta2))*s.SIN30
    x2 = y2*s.TAN60
    z2 = -s.RF*sin(theta2)
 
    y3 = (t + s.RF*cos(theta3))*s.SIN30
    x3 = -y3*s.TAN60
    z3 = -s.RF*sin(theta3)
 
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
    c = (b2-y1*dnm)*(b2-y1*dnm) + b1*b1 + dnm*dnm*(z1*z1 - s.RE*s.RE)
  
    # discriminant
    d = b*b - 4.0*a*c
    if d < 0: 
        # non-existing point
        sys.exit(1)
        
    z0 = -0.5*(b+sqrt(d))/a
    x0 = (a1*z0 + b1)/dnm
    y0 = (a2*z0 + b2)/dnm
    return x0, y0, z0
 
# inverse kinematics
# helper functions, calculates angle theta1 (for YZ-pane)
def delta_calcAngleYZ(x0, y0, z0):
    y1 = -0.5 * 0.57735 * s.F # f/2 * tg 30
    y0 -= 0.5 * 0.57735 * s.E    # shift center to edge
    # z = a + b*y
    a = (x0*x0 + y0*y0 + z0*z0 + s.RF*s.RF - s.RE*s.RE - y1*y1)/(2*z0)
    b = (y1-y0)/z0
    # discriminant
    d = -(a+b*y1)*(a+b*y1)+s.RF*(b*b*s.RF+s.RF) 
    if d < 0: 
        # non-existing point
        sys.exit(-1)

    yj = (y1 - a*b - sqrt(d))/(b*b + 1) # choosing outer point
    zj = a + b*yj
    theta = 180.0*atan(-zj/(y1 - yj))/pi + (180.0 if yj>y1 else 0.0)
    return theta

 
# inverse kinematics: (x0, y0, z0) -> (theta1, theta2, theta3)
# returned status: 0=OK, -1=non-existing position
def delta_calcInverse(x0, y0, z0):
    theta1 = delta_calcAngleYZ(x0, y0, z0)
    theta2 = delta_calcAngleYZ(x0*s.COS120 + y0*s.SIN120, y0*S.COS120-x0*s.SIN120, z0)  # rotate coords to +120 deg
    theta3 = delta_calcAngleYZ(x0*s.COS120 - y0*s.SIN120, y0*s.COS120+x0*s.SIN120, z0)  # rotate coords to -120 deg 
     
    return theta1, theta2, theta3

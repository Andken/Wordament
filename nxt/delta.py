#!/usr/bin/python

from math import pi
from math import sqrt
from math import atan
from math import sin
from math import cos
import sys

#
#
# NXT delta robot
#
# http:#blog.jfedor.org/2012/08/nxt-delta-robot.html
#
# This code requires the NBC/NXC enhanced firmware.
#
# The kinematics math is taken from here:
# http:#forums.trossenrobotics.com/tutorials/introduction-129/delta-robot-kinematics-3276/
#
#
# robot geometry
e = 12.0     # end effector
f = 46.0     # base
re = 22.0
rf = 8.0

# trigonometric constants
sqrt3 = sqrt(3.0)
sin120 = sqrt3/2.0   
cos120 = -0.5        
tan60 = sqrt3
sin30 = 0.5
tan30 = 1.0/sqrt3

# forward kinematics: (theta1, theta2, theta3) -> (x0, y0, z0)
# returned status: 0=OK, -1=non-existing position
def delta_calcForward(theta1, theta2, theta3):
    t = (f-e)*tan30/2
    dtr = pi/180.0

    theta1 *= dtr
    theta2 *= dtr
    theta3 *= dtr

    y1 = -(t + rf*cos(theta1))
    z1 = -rf*sin(theta1)

    y2 = (t + rf*cos(theta2))*sin30
    x2 = y2*tan60
    z2 = -rf*sin(theta2)

    y3 = (t + rf*cos(theta3))*sin30
    x3 = -y3*tan60
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
        return -1,0,0,0 # non-existing point

    z0 = -0.5*(b+sqrt(d))/a
    x0 = (a1*z0 + b1)/dnm
    y0 = (a2*z0 + b2)/dnm
    return 0,x0,y0,z0

def delta_calcAngleYZ(x0, y0, z0):
    y1 = -0.5 * 0.57735 * f # f/2 * tg 30
    #y1 = yy1
    y0 -= 0.5 * 0.57735    * e    # shift center to edge
    # z = a + b*y
    a = (x0*x0 + y0*y0 + z0*z0 +rf*rf - re*re - y1*y1)/(2*z0)
    b = (y1-y0)/z0
    # discriminant
    d = -(a+b*y1)*(a+b*y1)+rf*(b*b*rf+rf) 
    if (d < 0):
        return -1,0 # non-existing point
    yj = (y1 - a*b - sqrt(d))/(b*b + 1) # choosing outer point
    zj = a + b*yj
    theta = 180.0*atan(-zj/(y1 - yj))/pi + (180.0 if (yj>y1) else 0.0)
    if ((theta < 0) or (theta > 180)):
        return -1,0
    return 0,theta

# inverse kinematics: (x0, y0, z0) -> (theta1, theta2, theta3)
# returned status: 0=OK, -1=non-existing position
def delta_calcInverse(x0, y0, z0):
    theta1 = 0
    theta2 = 0
    theta3 = 0
    status, theta1 = delta_calcAngleYZ(x0, y0, z0)
    if (status == 0):
        status, theta2 = delta_calcAngleYZ(x0*cos120 + y0*sin120, y0*cos120-x0*sin120, z0)  # rotate coords to +120 deg
    if (status == 0):
        status, theta3 = delta_calcAngleYZ(x0*cos120 - y0*sin120, y0*cos120+x0*sin120, z0)  # rotate coords to -120 deg
    return status, theta1, theta2, theta3


#task main() {
#    t1
#    t2
#    t3
#
#    int errors = 0
#
#    int i, status
#
#    SetMotorRegulationTime(10) # the default is 100 ms, which doesn't work very well
#    PosRegEnable(OUT_A)
#    PosRegEnable(OUT_B)
#    PosRegEnable(OUT_C)
#
#    # move in circles
#    for (i = 0 i < 20*360 i+=30) {
#            # display the difference between target and actual motor positions
#            TextOut(0, LCD_LINE5, NumToStr(-t1-MotorRotationCount(OUT_A)))
#            TextOut(0, LCD_LINE6, NumToStr(-t2-MotorRotationCount(OUT_B)))
#            TextOut(0, LCD_LINE7, NumToStr(-t3-MotorRotationCount(OUT_C)))
#            status = delta_calcInverse(sind(i)*8, cosd(i)*8, -24, t1, t2, t3)
#            if (status == 0) {
#                TextOut(0, LCD_LINE1, NumToStr(t1))
#                TextOut(0, LCD_LINE2, NumToStr(t2))
#                TextOut(0, LCD_LINE3, NumToStr(t3))
#                PosRegSetAngle(OUT_A, -t1)
#                PosRegSetAngle(OUT_B, -t2)
#                PosRegSetAngle(OUT_C, -t3)
#                Wait(100)
#            } else {
#                errors++
#                TextOut(0, LCD_LINE4, NumToStr(errors))
#                PlayTone(440, 250)
#            }
#    }
#
#    # return to initial position
#    PosRegSetAngle(OUT_A, 0)
#    PosRegSetAngle(OUT_B, 0)
#    PosRegSetAngle(OUT_C, 0)
#    Wait(500)
#}

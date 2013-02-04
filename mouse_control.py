#!/usr/bin/python


import time
import sys
import Xlib.display
import Xlib.ext.xtest
from Xlib import X
import math
import random

class XObject(object):
    def __init__(self):
        self.display = Xlib.display.Display()
        self.screen = self.display.screen()
        self.root = self.screen.root

class Mouse(object):
    def __init__(self, xobject):
        self.xobject = xobject

    @property
    def display(self):
        return self.xobject.display

    @property
    def screen(self):
        return self.xobject.screen

    @property
    def root(self):
        return self.xobject.root

    def move(self, x, y, noise):
        x = x + random.randint(-1*noise,noise)
        y = y + random.randint(-1*noise,noise)
        self.root.warp_pointer(x, y)
        self.display.sync()
    
    def down(self, button=1):
        Xlib.ext.xtest.fake_input(self.display, Xlib.X.ButtonPress, button)
        self.display.sync()
    
    def up(self, button=1):
        Xlib.ext.xtest.fake_input(self.display, Xlib.X.ButtonRelease, button)
        self.display.sync()

    def drag_slowly(self, start, final, base_time=0.00125, noise=1):
        x0 = start[0]
        y0 = start[1]

        x_fin = final[0]
        y_fin = final[1]

        self.move(x0, y0, noise)
        distance = math.sqrt((x_fin-x0)*(x_fin-x0) + (y_fin-y0)*(y_fin-y0))
        for i in range(int(distance)):
            distance_ratio = i/distance
            x = int(x0 + round((x_fin-x0)*distance_ratio))
            y = int(y0 + round((y_fin-y0)*distance_ratio))
            self.move(x,y, noise)

            # delay before the next move
            time_epsilon = (random.random()*base_time/5)-(base_time * 0.1)
            time.sleep(base_time + time_epsilon)
        self.move(x_fin, y_fin, noise)

xobject = XObject()
m = Mouse(xobject)

m.move(1,700,1)
m.down()
m.drag_slowly((1,700),(700,700))
time.sleep(0.05)
m.drag_slowly((700,700),(700,1000))
m.up()

m.move(700,700,1)
m.down()
m.drag_slowly((700,700),(300,300))
m.up()

m.move(700,705,1)
m.down()
m.drag_slowly((700,705),(1,705))
m.up()





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

    def move(self, x, y):
        self.root.warp_pointer(x, y)
        self.display.sync()
    
    def down(self, button=1):
        Xlib.ext.xtest.fake_input(self.display, Xlib.X.ButtonPress, button)
        self.display.sync()
    
    def up(self, button=1):
        Xlib.ext.xtest.fake_input(self.display, Xlib.X.ButtonRelease, button)
        self.display.sync()

    def move_and_click(self, x, y, button=1):
        #TODO: jperla: maybe should move back?
        self.move(x, y)
        self.down(button)
        self.up(button)

    def drag_slowly(self, base_time, x0, y0, x_fin, y_fin, button=1):
        x0 = x0 + random.randint(-20,20)
        y0 = y0 + random.randint(-20,20)

        self.move(x0, y0)
        self.down(button)
        distance = math.sqrt((x_fin-x0)*(x_fin-x0) + (y_fin-y0)*(y_fin-y0))
        for i in range(int(distance)):
            distance_ratio = i/distance
            x = int(x0 + round((x_fin-x0)*distance_ratio)) + random.randint(-5,5)
            y = int(y0 + round((y_fin-y0)*distance_ratio)) + random.randint(-5,5)
            self.move(x,y)

            # delay before the next move
            time_epsilon = (random.random()*base_time/5)-(base_time * 0.1)
            time.sleep(base_time + time_epsilon)
        self.move(x_fin + random.randint(-20,20),y_fin + random.randint(-20,20))
        self.up(button)

xobject = XObject()
m = Mouse(xobject)

m.drag_slowly(0.0005, 300,300,700,700)
m.drag_slowly(0.0005, 300,300,700,700)
m.drag_slowly(0.0005, 300,300,700,700)





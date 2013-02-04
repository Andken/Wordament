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
    def __init__(self, xobject, size_of_box, origin):
        self.xobject = xobject
        self.size_of_box = size_of_box
        self.origin = origin
        self.current_pos = (0,0)
        
    def move(self, point, noise=0):
        x = point[0] + random.randint(-1*noise/2,noise/2)
        y = point[1] + random.randint(-1*noise/2,noise/2)
        self.current_pos = (x,y)
        self.xobject.root.warp_pointer(x, y)
        self.xobject.display.sync()
    
    def down(self, button=1):
        Xlib.ext.xtest.fake_input(self.xobject.display, Xlib.X.ButtonPress, button)
        self.xobject.display.sync()
    
    def up(self, button=1):
        Xlib.ext.xtest.fake_input(self.xobject.display, Xlib.X.ButtonRelease, button)
        self.xobject.display.sync()

    def drag_slowly(self, final, base_time=0.00125, noise=1):
        x0 = self.current_pos[0]
        y0 = self.current_pos[1]

        x_fin = final[0]
        y_fin = final[1]

        self.move(self.current_pos, noise)
        distance = math.sqrt((x_fin-x0)*(x_fin-x0) + (y_fin-y0)*(y_fin-y0))
        for i in range(int(distance)):
            distance_ratio = i/distance
            x = int(x0 + round((x_fin-x0)*distance_ratio))
            y = int(y0 + round((y_fin-y0)*distance_ratio))
            self.move((x,y), noise)

        self.move((x_fin, y_fin), noise)

    def translate(self, coord):
        x = self.origin[0] + coord[0]*self.size_of_box + self.size_of_box/2
        y = self.origin[1] + coord[1]*self.size_of_box + self.size_of_box/2
        return (x,y)

    def do_pattern(self, coords):
        self.up()
        self.move(self.translate(coords[0]))
        print self.translate(coords[0])
        self.down()
        for c in coords[1:]:
            self.drag_slowly(self.translate(c))
            time.sleep(0.5)

            print self.translate(c)

        self.up()

xobject = XObject()
m = Mouse(xobject, 75, (700,700))

m.do_pattern([(0,0),
              (0,1),
              (0,2),
              (0,3),
              (1,0),
              (1,1),
              (1,2),
              (1,3),
              (2,0),
              (2,1),
              (2,2),
              (2,3),
              (3,0),
              (3,1),
              (3,2),
              (3,3)
              ])


m.do_pattern([(0,0),
              (0,1),
              (1,1),
              (1,0)])


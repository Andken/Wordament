#!/usr/bin/python


import time
import sys
import Xlib.display
import Xlib.ext.xtest
from Xlib import X

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


xobject = XObject()
m = Mouse(xobject)

m.move(300,300)
m.down()
m.move(500,500)
m.up()




###while 1:
###    # Wait for display to send something, or a timeout of one second
###    readable, w, e = select.select([d], [], [], 1)
###
###    # if no files are ready to be read, it's an timeout
###    if not readable:
###        handle_timeout()
###
###    # if display is readable, handle as many events as have been recieved
###    elif disp in readable:
###        i = disp.pending_events()
###        while i > 0:
###            event = disp.next_event()
###            handle_event(event)
###            i = i - 1
###
###    # loop around to wait for more things to happen

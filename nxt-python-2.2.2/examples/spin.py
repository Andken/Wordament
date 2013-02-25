#!/usr/bin/env python

import nxt.locator
from nxt.motor import *
import time
from nxt.motcont import *

rot = 124



b = nxt.locator.find_one_brick()
m = MotCont(b)
m.start()
m.set_output_state(PORT_A, 100, 50, 1)
time.sleep(1)
print m.is_ready(PORT_A)
m.cmd(PORT_A, 100, 50, 1,1,1)
time.sleep(1)
print m.is_ready(PORT_A)
b.stop_program()

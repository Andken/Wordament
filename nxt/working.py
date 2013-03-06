#!/usr/bin/env python

import nxt.locator
from nxt.motor import *
import time
from nxt.motcont import *
from math import copysign
import thread

def turnmotor(motor, power, degrees):
	m.cmd(motor, power, degrees, 1, 1, 1)

def runinstruction(motor, speed, degrees):
	#THIS IS THE IMPORTANT PART!
	thread.start_new_thread(
		turnmotor,
		(motor, speed, degrees))


working_power = 100


b = nxt.locator.find_one_brick()
m = MotCont(b)
m.start()
m1 = Motor(b, PORT_A)

while 1:
    pos1 = 45
    pos2 = 0

    time.sleep(1)
    print "Before move: ", m1.get_tacho().rotation_count
    
    new_pos = abs(m1.get_tacho().rotation_count - pos1)
    power = -1*int(copysign(working_power,m1.get_tacho().rotation_count - pos1))
    runinstruction(PORT_A, power, new_pos);
    runinstruction(PORT_B, power, new_pos);
    runinstruction(PORT_C, power, new_pos);
    #    m.cmd(PORT_A, power, new_pos, 1,1,1)
    time.sleep(1)
    print "After move 1: ", m1.get_tacho().rotation_count
    
    new_pos = abs(m1.get_tacho().rotation_count - pos2)
    print m1.get_tacho().rotation_count, pos2
    power = -1*int(copysign(working_power,m1.get_tacho().rotation_count - pos2))
    
    
    print new_pos, power
    runinstruction(PORT_A, power, new_pos);
    runinstruction(PORT_B, power, new_pos);
    runinstruction(PORT_C, power, new_pos);
    #    m.cmd(PORT_A, power, new_pos, 1,1,1)
    time.sleep(1)
    print "After move 2: ", m1.get_tacho().rotation_count
#
#    time.sleep(1)
#    print "loop: ", m1.get_tacho()
#
##print m.is_ready(PORT_A)
##time.sleep(1)
##print m.is_ready(PORT_A)
b.stop_program()

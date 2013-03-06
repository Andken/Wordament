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
ma = Motor(b, PORT_A)
mb = Motor(b, PORT_B)
mc = Motor(b, PORT_C)

while 1:
    pos1a = 90
    pos1b = 45
    pos1c = 10
    pos2 = 0

    time.sleep(1)
    print "Before move: ", ma.get_tacho().rotation_count
    
    new_pos_a = abs(ma.get_tacho().rotation_count - pos1a)
    new_pos_b = abs(mb.get_tacho().rotation_count - pos1b)
    new_pos_c = abs(mc.get_tacho().rotation_count - pos1b)
    power_a = -1*int(copysign(working_power,ma.get_tacho().rotation_count - pos1a))
    power_b = -1*int(copysign(working_power,mb.get_tacho().rotation_count - pos1b))
    power_c = -1*int(copysign(working_power,mc.get_tacho().rotation_count - pos1b))
    runinstruction(PORT_A, power_a, new_pos_a);
    runinstruction(PORT_B, power_b, new_pos_b);
    runinstruction(PORT_C, power_c, new_pos_c);
    #    m.cmd(PORT_A, power, new_pos, 1,1,1)
    time.sleep(1)
    print "After move 1: ", ma.get_tacho().rotation_count
    
    new_pos_a = abs(ma.get_tacho().rotation_count - pos2)
    new_pos_b = abs(mb.get_tacho().rotation_count - pos2)
    new_pos_c = abs(mc.get_tacho().rotation_count - pos2)
    print ma.get_tacho().rotation_count, pos2
    power_a = -1*int(copysign(working_power,ma.get_tacho().rotation_count - pos2))
    power_b = -1*int(copysign(working_power,mb.get_tacho().rotation_count - pos2))
    power_c = -1*int(copysign(working_power,mc.get_tacho().rotation_count - pos2))
    
    
    print new_pos_a, power_a
    runinstruction(PORT_A, power_a, new_pos_a);
    runinstruction(PORT_B, power_b, new_pos_b);
    runinstruction(PORT_C, power_c, new_pos_c);
    #    m.cmd(PORT_A, power, new_pos, 1,1,1)
    time.sleep(1)
    print "After move 2: ", ma.get_tacho().rotation_count
#
#    time.sleep(1)
#    print "loop: ", ma.get_tacho()
#
##print m.is_ready(PORT_A)
##time.sleep(1)
##print m.is_ready(PORT_A)
b.stop_program()

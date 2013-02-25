#Script to control a NXT 2-axis CNC "Pancake maker"
#Illustrates controlling more than one motor at the same time without trying to
#sync them. Uses the thread module.
#Written 2/3/11 by Marcus Wanner
#
#For more info and warnings see:
#http://groups.google.com/group/nxt-python/browse_thread/thread/f6ef0865ae768ef

from nxt.motcont import *

import nxt, thread, time
b = nxt.find_one_brick()
m = MotCont(b)
m.start()
motors = [nxt.PORT_A, nxt.PORT_B, nxt.PORT_C]
p=100

def turnmotor(mi, power, degrees):
	m.cmd(motors[mi], power, degrees, 1, 0, 1)

#here are the instructions...
#the first value is the time to start the instruction
#the second is the axis (0 for x, 1 for y)
#the third is the power
#the fourth is the degrees
#it's probably not a good idea to run simultaneous turn
#functions on a single motor, so be careful with this
instructions = (
	[0, 0, -p, 45],
	[0, 1, -p, 45],
	[0, 2, -p, 45],
	[1, 0, p, 45],
	[1, 1, p, 45],
	[1, 2, p, 45],
)
#how long from start until the last instruction is ended
length = 2

def runinstruction(i):
	motorid, speed, degrees = i
	#THIS IS THE IMPORTANT PART!
	thread.start_new_thread(
		turnmotor,
		(motorid, speed, degrees))

#main loop
iteration = 0
while 1:
	seconds = 0
	while 1:
		print "Tick %d - %d" % (seconds, iteration)
		for i in instructions:
			if i[0] == seconds:
				runinstruction(i[1:])
		seconds = seconds + 1
		time.sleep(1)
		if seconds >= length:
			break
	iteration = iteration + 1

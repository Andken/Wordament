#!/usr/bin/python

import mouse_control

m = mouse_control.Mouse(75, (700,700))

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

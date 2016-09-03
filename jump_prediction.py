#!/bin/python

x1,v1,x2,v2 = raw_input("Please enter x1, v1, x2, v2: ").strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]


dx = x1 - x2
dv = v2 - v1

if(dv == 0):
    print "NO"
elif((dx % dv == 0) and (dx / dv > 0)):
    print "YES"
else:
    print "NO"

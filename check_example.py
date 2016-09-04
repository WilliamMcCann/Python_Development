#!/bin/python

a = int(raw_input("Please enter a: "))
b = int(raw_input("Please enter b: "))
c = int(raw_input("Please enter c: "))

print "a + b = %i" % (a + b)
print "b * c = %i" % (b * c)

d = str(type(c))
e = d[6:-1]
print "c is of type %s" % e

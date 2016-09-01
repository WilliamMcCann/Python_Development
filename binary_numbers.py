#!/usr/bin/env python

import sys
print "This program will convert a base 10 number into binary and count the max number of consecutive 1's in the binary form."
n = int(raw_input('Enter number: ').strip())

dec = str(bin(n))
print dec
print type(dec)
trimmed = dec[2:]
print "Trimmed = %s" % trimmed
list = trimmed.split("0")
print "List = %s" % list
print len(max(list))


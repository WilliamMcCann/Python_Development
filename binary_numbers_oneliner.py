#!/usr/bin/env python

print "This program will convert a base 10 number into binary and count the max number of consecutive 1's in the binary form."
print len(max((str(bin(int(raw_input().strip())))[2:]).split("0")))

#!/usr/bin/env python

import sys

n = int(sys.argv[1])
m = int(sys.argv[2]) 

def multiply(a,b):
	if a > 1:
		return (b + (multiply(a-1,b)))
	else:
		return b 

print multiply(n,m)

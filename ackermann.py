#!/bin/python
# hmmm...needs some work

m = int(raw_input("Enter m: "))
n = int(raw_input("Enter n: "))

import sys

sys.setrecursionlimit(50000)

def ack(m,n):
	if m==0:
		result=n+1
	elif n==0:
        	result=ack(m-1,1)
	else:
        	result=ack(m-1,ack(m,n-1))
	return result

print ack(m,n)

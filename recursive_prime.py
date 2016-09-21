#!/usr/bin/env python

def work(x,n):
        print("In work")
	if x == 1:
		return True
        else:
		if n % x == 0:
                	return False
	        if n % x != 0:
        		return(work(x-1, n))

def prime(n):
	print("In prime")
	x = (n / 2) + 1
	if n == 1:
		print "Not Prime"
	elif n == 2:
		print "Prime"
	elif (work(x,n) == True):
		print "Prime"
	else:
		print "Not Prime"

prime(int(raw_input("Please input the number to be checked for primality: ")))

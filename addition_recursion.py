#!/usr/bin/env python

print "This is a program that multiplies two numbers."
n = (int(raw_input('Enter the first number: ')))
m = (int(raw_input('Enter the first number: ')))

def multiply(a,b):
	if a > 1:
		return (b + (multiply(a-1,b)))
	else:
		return b 

print multiply(n,m)

#!/usr/bin/env python

print "This is a program that multiplies two numbers."
n = (int(raw_input('Enter the first number: ')))
m = (int(raw_input('Enter the first number: ')))

def multiply(a,b):
	if a > 1:
		return (a + (multiply(a,b-1)))
	if a == 1:
		return 1

print multiply(n,m)

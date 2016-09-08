#!/bin/python

print("This program throws a custom exception if you use a non-positive number")
n,p = map(int, raw_input("Enter an integer, and then an integer two which you'd like to raise it exponentially: ").split())
if n < 0 or p < 0:
	raise Exception("n and p should be non-negative")
else:
        return(n**p)

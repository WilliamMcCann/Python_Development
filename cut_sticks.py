#!/bin/python

import sys
import math

print"Program takes array of n sticks of different length and outputs the remaining number of sticks after each round of chopping off the length of the inital shortest stick." 


n = int(raw_input("Number of sticks: ").strip())
arr = map(int,raw_input("Length of sticks: ").strip().split(' '))

def sub_min(x):
    return x - cut_length

cut_length = min(arr)
#print cut_length
#print max(arr)
reps = int(math.ceil(max(arr)/min(arr)))
#print reps
for _ in range(reps):
    print(len([x for x in arr if x > 0]))
    arr = map(sub_min, arr)
    #print(arr[1])

#!/bin/python

print"This program takes a number of students and when they arrive and determines if class is cancelled."


t = int(raw_input("Please print number of test cases: ").strip())
for a0 in xrange(t):
    n,k = raw_input("Enter number of students followed by the number of students who must be on time: ").strip().split(' ')
    n,k = [int(n),int(k)]
    arr = map(int,raw_input("Please list student arrival times: ").strip().split(' '))
    count = 0
    for i in range(n):
        if arr[i] <= 0:
            count += 1
    if count < k:
        print "YES"
    else:
        print "NO"

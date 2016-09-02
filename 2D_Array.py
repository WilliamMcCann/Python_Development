#!/bin/python

print'Please enter a 6x6 array of integers'

arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)


sums = []


for i in range(4):
    for j in range(4):
        a = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
        sums.append(a)

print(max(sums))

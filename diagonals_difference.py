#!/bin/python

print "This program takes a matrix and prints the absolute difference of the sums of the matrix diagonals"

n = int(raw_input("Please enter the dimensions of an NxN matrix: ").strip())
print type(n)
print n

matrix = []
for i in range(n):
    print i
    temp = map(int, raw_input("Please enter a line from the NxN matrix: ").strip().split())
    matrix.append(temp)

diag1 = []
for j in range(n):
    a = matrix[j][j]
    diag1.append(a)
s1 = sum(diag1)

diag2 = []
for k in range(n):
    b = matrix[k][n-1]
    n = n-1
    diag2.append(b)
s2 = sum(diag2)
    
print abs(s1 - s2)

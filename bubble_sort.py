#!/bin/python

print("This is a simple implementation of bubble sorting.")
n = int(raw_input("Please enter the number of integers in the array: "))
a = map(int, raw_input("Please enter the integers to be sorted: ").split())

numberOfSwaps = 0

for i in range(n):
    
    
    for j in range(n-1):
        if a[j] > a[j + 1]:
            a[j], a[j+1] = a[j+1], a[j]
            numberOfSwaps += 1
            
    if (numberOfSwaps == 0):
        break

print("Array = %s") % (str(a))
print("Array is sorted in %d swaps." % (numberOfSwaps))
print("First Element: %d" % (a[0]))
print("Last Element: %d" % (a[-1]))


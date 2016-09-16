#!/bin/python

print("This is a simple implementation of bubble sorting.  It will print out the sorted interations.")
arr = map(int, raw_input("Please enter the integers to be sorted: ").split())

for i in range(len(arr) - 1):
	for q in range(len(arr) - 1 - i):
		print(arr)
		if arr[q] > arr[q + 1]:
			arr[q], arr[q + 1] = arr[q + 1], arr[q]
print(arr)

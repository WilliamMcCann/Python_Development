#!/usr/bin/env python

print("This program will sort an array using insertion sort and will print the sort iterations.")

arr = map(int, raw_input("Enter each item of the array separated by a space: ").strip().split())

print("arr = %s" % str(arr))

for i in range(len(arr)):
	print("arr in outer loop = %s" % str(arr))
	for q in range(1, len(arr)):
		value = arr[q]
		print("arr in inner loop = %s" % str(arr))
		if arr[q] < arr[q - 1]:
			arr[q] = arr[q - 1]
			arr[q - 1] = value
print(arr)

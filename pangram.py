#!/usr/bin/env python

import string

print("This program checks to see if a string is a pangram.")

s = raw_input("Enter string: ")
low = s.lower()
temp = []
#print(low)
for i in range(len(s)):
    if low[i] in string.ascii_lowercase:
        temp.append(low[i])
b = set(temp)
#print(b)
        
        
if len(b) == 26:
    print("pangram")
else:
    print("not pangram")

#!/usr/bin/env python

def insertionSort(ar):
        for q in range(1,len(ar)):
            for i in range(q):
                if(ar[q] < ar[i]):
                   temp=ar[q]
                   ar[q]=ar[i]
                   ar[i]=temp
            for x in ar:
                print x,
            print

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)

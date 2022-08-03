#!/usr/bin/python

import sys
x = sys.argv[1:][0]
odd = 0 
hon = 0
maxnum = 0
saveindex = 0
i = 0
y = 0
ar = []
for i in range(len(x)):
    if int(x[i]) == 1 or int(x[i])%2 != 0:
        ar.append(0)
    else: 
        ar.append(1)
for i in range(len(ar)):
    for y in range(len(ar)-i):
        if ar[i+y] == 0:
            hon += 1
        else: 
            odd += 1
        if hon == odd:
            if odd + hon > maxnum:
                saveindex = i
                maxnum = odd + hon
    hon,odd=0,0
print("".join(map(str,x[saveindex:maxnum+saveindex])))
#!/usr/bin/python
import sys

#print ('Argument List:', str(sys.argv))
#argument = sys.argv

a = list(sys.argv[1:][0].split(' '))
#print(a)
#sys.exit(0)

if a==[]:
    print('KO')
    sys.exit(0)
#print(a)
x,y,i = -1, 0, 0
while i in range(len(a)):
    while  i < len(a) and a[i].isdigit():
        x += 1
        i += 1
    while  i < len(a) and a[i].isdigit()==False:
        y += 1
        i += 1
#    print(x,y,i)
    
    if x!=y:
        print ("KO")
        sys.exit(0)
    x,y=0,0
    if  i == len(a):
#        print ("OK")
        break
x=[]
y=[]
i=0
z=0

while i in range(len(a)):
    while  i < len(a) and a[i].isdigit():
        x.append(a[i])
        i += 1
    while  i < len(a) and a[i].isdigit()==False:
        y.append(a[i])
        i += 1
#    print(x,y)
    x.reverse()    
    while len(y)!=0:
#        print(x,y)

        
        ay = float(x.pop(0))
        ax = float(x.pop(0))       
        operand = y.pop(0)
        if operand == '*':
            z = ax*ay
        elif operand == '/':
            z = ax/ay
        elif operand == '-':
            z = ax-ay
        elif operand == '+':
            z = ax+ay
        elif operand == '%':
            z = ax%ay
#        print(z)
        x.append(z)
        if len(x) == 2:
            x.reverse()
#        print(x,y,i)
#print(x[0])
#console.alert(x[0])
print(x[0], file = sys.stdout)
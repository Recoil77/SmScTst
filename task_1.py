#!/usr/bin/python
import sys
#print ('Argument List:', str(sys.argv))
#argument = sys.argv

a = sys.argv[1:]



#print(a)
a = "".join(map(str,a))
i = 0
z = []
flag = 0
gg =''
for x in a:
    #print(x)
    if x == "'" and flag == 0:
        flag = 1
#        print("Flag ON")
        continue
    if x == "'" and flag == 1:
        z.append(gg)
        flag = 0
        gg=''
#        print("Flag OFF")
        continue
    gg ="".join((gg,x)) 
a = z
#print(a)
#sys.exit(0)
for x in a:
  
#    print(x,end=" ")
#    x=x.strip("'")
    if x == '':
        print("OK")
        continue;
    elif x[0]=='[' and x[-1] == ']':
        print("OK")
        continue;
    elif x[0]=='(' and x[-1] == ')':
        print("OK")
        continue;
    elif x[0]=='{' and x[-1] == '}':
        print("OK")
        continue;

    elif x[0]=='[' :
        if x[-1] != ']':
            print("KO")
            continue;

    elif x[0]=='(' :
        if x[-1] != ')':
            print("KO")
            continue;

    elif x[0]=='{' :
        if x[-1] != '}':
            print("KO")
            continue;

    elif x[-1]=='{' or x[-1]=='(' or x[-1]=='[' or x[-1]=='}' or x[-1]==')' or x[-1]==']':
        print("KO")
        continue;
    elif x[0]=='}' or x[0]==')' or x[0]==']':
        print("KO")
        continue;
    print("OK")
        
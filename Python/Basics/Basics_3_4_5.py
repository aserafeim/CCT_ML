# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 11:01:20 2022

@author: alexs
"""

import math
#### for/while loops, if statements, basic functions.


###Iterations 


#for 'Variable' in 'structure':
        
dic={'one':1,'two':2,'three':3}
list=[1,2,6,4,5]

for i in list:
    
    print(i)

### range(beginning,end,step ) creates a tuple that is iterable

print(range(0,5,2))

### range(0,3)=[0,1,2,3]

for i in range(0,len(list),2):
    print(list[i])
    i=i+1

for i in range(10):
    for j in range(10):
        print(i+j)    

for i in dic.keys():
    print(dic[i])

### While loops: they will operate until logical statement becomes False

#### While 'Logical statement':
    #### statements, operations etc.
i=0
while i<10:
    print(i)
    i=i+1

# while True:
#     print('Never ending')
    
print('IF Statements')
####If statements: logical gateways. They activate a piece of code is a logical
### expression is satisfied.

i=11
j=0
if i>10:
    print('Success')
    
elif i==2:
    print(i)

else:
    print('Failure')

if i>10 or j>1:
    print(i,j)
else:
    print('failure')
    
print('Functions')
#### Functions

def sum1(a,b):
    c=a+b
    d=a*b
    
    return c,d 


def pyth(a,b):
    
    return (a**2+b**2)**(1/2)

c,d=sum1(1,5)

e=pyth(3,3)

    

    
    
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:32:37 2022

@author: alexs
"""

#####Reference website https://www.w3schools.com/python/python_lists.asp

###empty list definition
list_1=[]

list_1=[1,2,3,4,5,6]

list_2=[1,2,'3']

print(list_1[0])


list_3=[list_1,list_2]

list_3[0] ###returns the list 1

list_3[0][0] ###returns first element of list_1

###Backwards access

list_1[-1] ### returns 6

list_1[0]=5 ### change first element to 5

### List slicing returns a list with elements from indeces 2 to 5 of list_1
k1=list_1[2:6]

### returns sliced list with numbers from 2 until the end
k2=list_1[2:]

k3=list_1[:3]

###insert '1' in a list_1 in postion 1

list_1.insert(1,'1')

###Append function of a list 

list_1.append(7)
###list comprehension 

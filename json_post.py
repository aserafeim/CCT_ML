# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 11:24:33 2021

@author: alexs
"""


# Python program to read
# json file
 
 
import json
 
# Opening JSON file
f = open('TTT1.json',)
 
# returns JSON object as
# a dictionary
data = json.load(f)

#Find temperature range of each phase. 

#Iterate over temperatures with a certain Temperature step and interpolate at each temperature and phase region to calculate the critical times
        # ##Define temp range and temperature increment to calculate [Tinitial, Tfinal] DTi
        # Ti=Tinitial
        # ##start iterating Ti
        # while Ti>Tfinal :
        ##Iterate through phases
# finding the global maximum and minimum of the temperature data
max=None
min=None
Phases=data['Phase Data']
for i in Phases.keys():
    pxy[i]={}
    print(i) #here we get ferrite, pearlite, bainite
    for j in Phases[i].keys():
        print(j) #here we get % of each phase
        for k in Phases[i][j]['Temperature']:
            print(k)
            if max is None:
                max=k
                min=k
            elif k>max:
                max=k
                # print(k)
            elif k<min:
                min=k
                # print(k)
print(min, max)













           ##If yes interpolate the times for all the fractions in that phase.
            
            
            # i=+1
            # Ti=Tinitial-DTi*i
# Closing file
f.close()
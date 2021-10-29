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
Ti=500
Phases=data['Phase Data']
for i in Phases.keys():
    for j in Phases[i].keys():
       if Phases[i][j]['Temperature'][-1]>Ti & Phases[i][j]['Temperature'][0]<Ti :
           
           
            
            ##If yes interpolate the times for all the fractions in that phase. 
            
            
            # i=+1
            # Ti=Tinitial-DTi*i
# Closing file
f.close()
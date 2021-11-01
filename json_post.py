# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 11:24:33 2021

@author: alexs
"""


# Python program to read
# json file
 
 
import json
from scipy import interpolate
 
# Opening JSON file
f = open('TTT1.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
####Data inter is the dictionary where all the interpolated data will go
Data_inter={}

#Find temperature range of each phase. 

max=None
min=None
Phases=data['Phase Data']
for i in Phases.keys():
    for j in Phases[i].keys():
        for k in Phases[i][j]['Temperature']:
            if max is None:
                max=k
                min=k
            elif k>max:
                max=k
            elif k<min:
                min=k
            # print(min, max)
#Iterate over temperatures with a certain Temperature step (Dti) and interpolate at each temperature and phase region to calculate the critical times
Range=[max, min]
DTi=5
k=0
        # ##Define temp range and temperature increment to calculate [Tinitial, Tfinal] DTi
Ti=Range[0]
        # ##start iterating Ti
        
#### Create dictionary with interpolation functions for all phases and fractions

####Phase inter is the dic where the interpolation functions of each phase and fraction will go.

Phase_inter={}
Phases=data['Phase Data']
for i in Phases.keys():
    Phase_inter[i]={}
    ####Set each phase in the interpolated data dictionaryas empty dic so that we can add the fraction data.
    Data_inter[i]={}
    for j in Phases[i].keys():
        Data_inter[i][j]={}
        Data_inter[i][j]={'Temperature':[],'Time':[]}
        Phase_inter[i][j]=interpolate.interp1d(Phases[i][j]['Temperature'],Phases[i][j]['Time'])

while Ti>Range[-1] :

    for i in Phases.keys():
        for j in Phases[i].keys():   
            if Phases[i][j]['Temperature'][-1]>Ti and Phases[i][j]['Temperature'][0]<Ti:
                # Temp_list.append(Ti)
                Data_inter[i][j]['Temperature'].append(Ti)
                # Time_list.append(float(Phase_inter[i][j](Ti)))
                Data_inter[i][j]['Time'].append(float(Phase_inter[i][j](Ti)))

    k+=1
    Ti-=DTi*k
# Closing file
# f.close()
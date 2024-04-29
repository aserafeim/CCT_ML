# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 13:35:14 2022

@author: alexs
"""

import json
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

###Maybe replace with click and select
f = open('C55S.json')

data = json.load(f)

phases=['Ferrite','Pearlite','Bainite']
####create a structure that loops over all the phases and plots the lines
###Enter ferrite phase----Enter fraction percentage----Time, Temperature 

fig, ax = plt.subplots()  # Create a figure containing a single axes.
for phase in phases :
    for fractions in data[phase]:
        #print(Main[phase][fractions]['Time'])
        #print(Main[phase][fractions]['Temperature'])
        ax.set_xscale('log')
        ax.plot(data[phase][fractions]['Time'],data[phase][fractions]['Temperature'],label=phase+''+fractions)  # Plot some data on the axes.
        ax.legend()
        

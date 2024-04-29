# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 23:25:17 2022

@author: alexs
"""

import os
import pandas as pd
import json
import matplotlib.pyplot as plt

base_dir = r'\Users\alexs\sciebo\CTT_TTT Images\Atlas_New\JSON files\British En Steels'

#Get all files in the directory
phases=['Ferrite','Pearlite','Bainite']
data_list = []
for file in os.listdir(base_dir):
    
    #If file is a json, construct it's full path and open it, append all json data to list
    if 'json' in file:
        
        json_path = os.path.join(base_dir, file)
        f = open(json_path)
        data = json.load(f)
        # data_list.append(json_data)

        fig, ax = plt.subplots()  # Create a figure containing a single axes.
        fig.canvas.set_window_title(file)
        for phase in phases :
            for fractions in data[phase]:
                #print(Main[phase][fractions]['Time'])
                #print(Main[phase][fractions]['Temperature'])
                ax.set_xscale('log')
                ax.plot(data[phase][fractions]['Time'],data[phase][fractions]['Temperature'],label=phase+''+fractions)  # Plot some data on the axes.
                ax.legend()
                ax.set_ylabel('Temperature (°C)',fontsize=12)
                ax.set_xlabel('Times (s)',fontsize=12)
                # filename=r'\Users\alexs\sciebo\CTT_TTT Images\python\working\images'+'png'
                fig.savefig(r'\Users\alexs\sciebo\CTT_TTT Images\python\working\images'+ '\\' + file[:-4] +'png')
                plt.close('all')



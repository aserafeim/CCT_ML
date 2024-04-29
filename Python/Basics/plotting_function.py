# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 11:28:10 2022

@author: aserafeim
"""

import matplotlib.pyplot as plt

def plotting_data(df,ele,var1,var2=None):
    
    fig,ax=plt.subplots()
    fig=ax.scatter(df[ele],df[var1],c=df[var2],cmap='inferno')
    ax.set_xlabel(ele+' '+'content')
    ax.set_ylabel(var1)
    ax.set_yscale('log')

    



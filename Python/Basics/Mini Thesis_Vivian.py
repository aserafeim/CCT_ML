# -*- coding: utf-8 -*-
"""
Created on Fri May 27 12:43:57 2022

@author: vivia
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.close('all')
dataframe = pd.read_excel(r'D:\sciebo\CTT_TTT Images\Python\Basics')
# dataframe = pd.read_excel(r'C:\Users\alexs\sciebo\Steel_properties_ML_Mini_Thesis\Mid Mn Data Collection.xlsx')

# dataframe.columns

df_clean=dataframe.drop(['S. No', 'Title', 'DOI','Ni','Cu','Homogenization Temp (C)',
        'Homogenization Time (s)', 'Hot Forging Temp (C)',
        'Hot Forging Thickness Reduction (%)', 'Hot Forging\nThickness (mm)',
        'Reheated\nTemp (C)', 'Hot Rolling Temp (C)',
        'Hot Rolling Thickness Reduction (%)', 'Hot Rolling Thickness (mm)',
        'Homogenization Annealing Temp (C)',
        'Homogenization Annealing Time (s)', 'Quenching',
        'Cold Rolling Thickness Reduction (%)', 'Cold Rolling Thickness (mm)',
        'Austenitizing Temp\n(C)', 'Austenitizing Time\n(s)', 'Quenching.1',
        'Heating Rate\n(C/s)','Heating Rate\n(C/s).1', 'Second\nAnnealing\nTemp (C)',
        'Second\nAnnealing\nTime\n(s)', 'Second\nAnnealing\nQuenching',
        'Tempering\nTemp\n(C)', 'Tempering\nTime\n(s)', 'Tempering\nQuenching', 'Cooling Rate\n(C/s)',
       'Quenching.2', 'Ferrite\n(%)',
       'Martensite\n(%)', 'Martensite +\nAustenite\n(%)',
       'Prior Austenite Grain Size\n(microm)', 'Martensite Substructure Size',
       'Retained Austenite Size\n(Microm)', 'Retained Ferrite Size\n(Microm)',
       'Martensite +\nAustenite Size\n(Microm)',
       'Mn content in Retained Austensite\n(wt%)',
       'Yield Point Elongation\n(%)\nHow long lueders band is',
       'Charpey Energy\n(J)'],axis=1)

df_clean=df_clean.dropna()

print(df_clean.nunique())

cr = df_clean['Mn']
# Scatter plot retained austenite vs IA temperature + Mn scaling
fig1, axs1 = plt.subplots(figsize=(80/25.4,80/25.4))
plt.scatter(data=df_clean, x="Intercritical Annealing Temp\n(C)", 
                y="Retained\nAustenite\n(%)", c = cr, cmap = 'tab20')
clr = plt.colorbar()
clr.set_label(label = 'Mn Content (%)', fontsize=11)
axs1.set_xlabel("Annealing Temperature (°C)",fontsize=11)
axs1.set_ylabel('Retained Austenite (%)',fontsize=11)

for label in (axs1.get_xticklabels() + axs1.get_yticklabels()):
 	label.set_fontsize(11)

fig1.savefig('Fig1.png',dpi=600,bbox_inches='tight')

#####
##### Yield and tensile strength vs annealing temperature.
fig2, axs2 = plt.subplots(figsize=(80/25.4,80/25.4))
axs2.scatter(data=df_clean, x="Intercritical Annealing Temp\n(C)", 
                y="Yield Strength\n(MPa)")
axs2.scatter(data=df_clean, x="Intercritical Annealing Temp\n(C)", 
                y="Ultimate Tensile Strength\n(MPa)")
axs2.set_xlabel("Annealing Temperature (°C)",fontsize=11)
axs2.set_ylabel('Strength (MPa)',fontsize=11)
axs2.legend(fontsize=8,loc='upper left')

for label in (axs2.get_xticklabels() + axs2.get_yticklabels()):
 	label.set_fontsize(11)

fig2.savefig('Fig2.png',dpi=600,bbox_inches='tight')


####
#### Yield and Tensile strenght vs RA
fig3, axs3 = plt.subplots(figsize=(80/25.4,80/25.4))
axs3.scatter(data=df_clean, x="Retained\nAustenite\n(%)", 
                y="Yield Strength\n(MPa)")
axs3.scatter(data=df_clean, x="Retained\nAustenite\n(%)", 
                y="Ultimate Tensile Strength\n(MPa)")
axs3.set_xlabel("Retained Austenite (%) ",fontsize=13)
axs3.set_ylabel('Strength (MPa)',fontsize=13)
axs3.legend(fontsize=5,loc='upper right')

for label in (axs3.get_xticklabels() + axs3.get_yticklabels()):
 	label.set_fontsize(13)

fig3.savefig('Fig3.png',dpi=1200,bbox_inches='tight')

####
#### Tensile strenght, UE vs RA
fig4, axs4 = plt.subplots(figsize=(80/25.4,80/25.4))
axs4.scatter(data=df_clean, x="Retained\nAustenite\n(%)", 
                y="Ultimate Tensile Strength\n(MPa)", c='red')
axs5 = axs4.twinx()
axs5.scatter(data=df_clean, x="Retained\nAustenite\n(%)", 
                y="Uniform Elongation\n(%)",c='orange')
axs4.set_xlabel("Retained Austenite (%) ",fontsize=13)
axs4.set_ylabel('Ultimate Tensile Strength (MPa)',fontsize=13, c='red')
axs5.set_ylabel('Uniform Elongation (%)',fontsize=13, c='orange')

for label in (axs4.get_xticklabels() + axs4.get_yticklabels()):
 	label.set_fontsize(13)

fig4.savefig('Fig4.png',dpi=1200,bbox_inches='tight')

####
#### Pair plot with C, Mn, Al, Si
# fig5, axs6 = plt.subplots(figsize=(80/25.4,80/25.4))
axs6 = sns.pairplot(data=df_clean,vars=['C','Mn', 'Al'])
# fig5.savefig('Fig5.png',dpi=1200,bbox_inches='tight')
plt.savefig('Pairplot.png',dpi=600,bbox_inches='tight' )

###
#### Box plot composition components.
fig6, axs7 = plt.subplots(figsize=(80/25.4,80/25.4))
axs7=df_clean.boxplot(column=['C', 'Mn', 'Si', 'Al'], 
                      grid=False, color='Black', ax=axs7)

for label in (axs7.get_xticklabels() + axs7.get_yticklabels()):
  label.set_fontsize(13)

fig6.savefig('Fig6.png',dpi=1200,bbox_inches='tight')

# # Count no. of C%
# fig2, axs2 = plt.subplots(figsize=(6,4))
# sns.countplot(x="C", data=df_clean, ax=axs2)
# axs2.set_xlabel("C weight percentage",fontsize=24)
# axs2.set_ylabel('Count',fontsize=24)

# for label in (axs2.get_xticklabels() + axs2.get_yticklabels()):
#  	label.set_fontsize(24)

# fig2.savefig('Fig2.png',dpi=1200,bbox_inches='tight')


# # Corelation map
# fig3, axs3 = plt.subplots(figsize=(6,4))
# sns.heatmap(df_clean.corr('kendall'), annot=True, ax=axs3)

# fig3.savefig('Fig3.png',dpi=1200,bbox_inches='tight')

# cold_roll = np.logical_and(np.isnan(dataframe['Cold Rolling Thickness Reduction (%)']), 
#                           np.isnan(dataframe['Cold Rolling Thickness (mm)']))
# #False - cold rolled & Ture - not cold rolled


# hot_roll = np.logical_and(np.isnan(dataframe['Hot Rolling Temp (C)']), 
#                            np.isnan(dataframe['Hot Rolling Thickness (mm)']))
# #False - cold rolled & Ture - not cold rolled



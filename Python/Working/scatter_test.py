import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

main_elements=['C', 'Mn', 'Cr', 'Ni', 'Si', 'Mo']
other_elements=['P', 'S', 'V', 'W']

crit_temps=['Ms','Mf','Ac1','Ac3']
start_times=['Ferrite','Pearlite','Bainite']

### import dataframe from CSV file

df = pd.read_csv('Crit_temp.csv')

### remove specific alloying elements

drop_elements=['Co', 'N', 'Ti', 'Al', 'Cu']
df.drop(drop_elements, inplace=True, axis=1)

### remove grain size data

df.drop('Grain Size:', inplace=True, axis=1)

### remove colon from column names

df.columns = df.columns.str.replace(':', '')

### remove colon from column names

df.columns = df.columns.str.replace('_1_Time', '')

#------------------------------------------#

### Ms vs C

z=sns.lmplot(x='C', y='Ms', data=df, ci=None)
plt.savefig("Ms vs. C.png",dpi=600,bbox_inches='tight')

# fig,ax=plt.subplots()
# fig=ax.scatter(x,y)
# plt.xlim(0.25,1)
# ax.set_xlabel('C'+' '+'content'+' '+'(%)')
# ax.set_ylabel('Ms temperature'+' '+'(degree celsius)')

# z = np.polyfit(x, y, 1)
# p = np.poly1d(z)
# plt.plot(x,p(x),"r--")

# plt.savefig("Ms vs. C.png",dpi=600,bbox_inches='tight')

# ### Mf vs C

# fig,ax=plt.subplots()
# fig=ax.scatter(df['C'],df['Mf'])
# plt.xlim(0.25,1)
# ax.set_xlabel('C'+' '+'content'+' '+'(%)')
# ax.set_ylabel('Mf temperature'+' '+'(degree celsius)')
# plt.savefig("Mf vs. C.png",dpi=600,bbox_inches='tight')

# ### Bainite time vs C

# fig,ax=plt.subplots()
# fig=ax.scatter(df['C'],df['Bainite_1_Time'])
# ax.set_yscale('log')
# plt.xlim(0.25,1)
# ax.set_xlabel('C'+' '+'content'+' '+'(%)')
# ax.set_ylabel('Bainite start time'+' '+'(s)')
# plt.savefig("Bainite vs. C.png",dpi=600,bbox_inches='tight')

# ### Bainite vs Cr

# fig,ax=plt.subplots()
# fig=ax.scatter(df['Cr'],df['Bainite_1_Time'])
# ax.set_yscale('log')
# plt.xlim(0.0,5)
# plt.ylim(0.0,300)
# ax.set_xlabel('Cr'+' '+'content'+' '+'(%)')
# ax.set_ylabel('Bainite start time'+' '+'(s)')
# plt.savefig("Bainite vs. Cr.png",dpi=600,bbox_inches='tight')

# ### Bainite vs Mo

# fig,ax=plt.subplots()
# fig=ax.scatter(df['Mo'],df['Bainite_1_Time'])
# ax.set_yscale('log')
# plt.xlim(0.5,6)
# plt.ylim(0.0,1000)
# ax.set_xlabel('Mo'+' '+'content'+' '+'(%)')
# ax.set_ylabel('Bainite start time'+' '+'(s)')
# plt.savefig("Bainite vs. Mo.png",dpi=600,bbox_inches='tight')

# ### Bainite vs V

# fig,ax=plt.subplots()
# fig=ax.scatter(df['V'],df['Bainite_1_Time'])
# ax.set_yscale('log')
# plt.xlim(0.1,2)
# plt.ylim(0.0,500)
# ax.set_xlabel('V'+' '+'content'+' '+'(%)')
# ax.set_ylabel('Bainite start time'+' '+'(s)')
# plt.savefig("Bainite vs. V.png",dpi=600,bbox_inches='tight')

# ### Ac1 vs Ni

# fig,ax=plt.subplots()
# fig=ax.scatter(df['Ni'],df['Ac1'])
# plt.xlim(0.1,5)
# plt.ylim(650,800)
# ax.set_xlabel('Ni'+' '+'content'+' '+'(%)')
# ax.set_ylabel('Ac1 temperature'+' '+'(degree celsius)')
# plt.savefig("Ac1 vs. Ni.png",dpi=600,bbox_inches='tight')

# ### Ac3 vs Ni

# fig,ax=plt.subplots()
# fig=ax.scatter(df['Ni'],df['Ac3'])
# plt.xlim(0.5,5)
# plt.ylim(700,850)
# ax.set_xlabel('Ni'+' '+'content'+' '+'(%)')
# ax.set_ylabel('Ac3 temperature'+' '+'(degree celsius)')
# plt.savefig("Ac3 vs. Ni.png",dpi=600,bbox_inches='tight')

# ### Ac1 vs Cr

# fig,ax=plt.subplots()
# fig=ax.scatter(df['Cr'],df['Ac1'])
# plt.xlim(0.5,7)
# ax.set_xlabel('Cr'+' '+'content'+' '+'(%)')
# ax.set_ylabel('Ac1 temperature'+' '+'(degree celsius)')
# plt.savefig("Ac1 vs. Cr.png",dpi=600,bbox_inches='tight')

# ### Ac3 vs Cr

# fig,ax=plt.subplots()
# fig=ax.scatter(df['Cr'],df['Ac3'])
# plt.xlim(0.5,6)
# plt.ylim(760,890)
# ax.set_xlabel('Cr'+' '+'content'+' '+'(%)')
# ax.set_ylabel('Ac3 temperature'+' '+'(degree celsius)')
# plt.savefig("Ac3 vs. Cr.png",dpi=600,bbox_inches='tight')

# ### Bainite vs Ms

# fig,ax=plt.subplots()
# fig=plt.scatter(df['Ms'],df['Bainite_1_Time'],c=df['C'],cmap='inferno')
# plt.colorbar()
# ax.set_yscale('log')
# plt.ylim(0.0,1000)
# ax.set_xlabel('Ms'+' '+'temperature'+' '+'(degree celsius)')
# ax.set_ylabel('Bainite start time'+' '+'(s)')
# plt.savefig("Bainite vs. Ms.png",dpi=600,bbox_inches='tight')

# ### Ms vs Cr

# fig,ax=plt.subplots()
# fig=plt.scatter(df['Cr'],df['Ms'],c=df['C'],cmap='inferno')
# plt.colorbar()
# plt.xlim(0.5,1.75)
# plt.ylim(100,450)
# ax.set_xlabel('Cr'+' '+'content'+' '+'(%)')
# ax.set_ylabel('Ms temperature'+' '+'(degree celsius)')
# plt.savefig("Ms vs. Cr.png",dpi=600,bbox_inches='tight')

# ### Ms vs Si

# fig,ax=plt.subplots()
# fig=plt.scatter(df['Si'],df['Ms'],c=df['C'],cmap='inferno')
# plt.colorbar()
# plt.xlim(0.25,0.42)
# plt.ylim(100,450)
# ax.set_xlabel('Si'+' '+'content'+' '+'(%)')
# ax.set_ylabel('Ms temperature'+' '+'(degree celsius)')
# plt.savefig("Ms vs. Si.png",dpi=600,bbox_inches='tight')

# ### Ms vs Ni

# fig,ax=plt.subplots()
# fig=plt.scatter(df['Ni'],df['Ms'],c=df['C'],cmap='inferno')
# plt.colorbar()
# plt.xlim(0.2,2)
# plt.ylim(100,450)
# ax.set_xlabel('Ni'+' '+'content'+' '+'(%)')
# ax.set_ylabel('Ms temperature'+' '+'(degree celsius)')
# plt.savefig("Ms vs. Ni.png",dpi=600,bbox_inches='tight')

# ### Ms vs Mn

# fig,ax=plt.subplots()
# fig=plt.scatter(df['Mn'],df['Ms'],c=df['C'],cmap='inferno')
# plt.colorbar()
# plt.xlim(0.4,1.05)
# plt.ylim(100,450)
# ax.set_xlabel('Mn'+' '+'content'+' '+'(%)')
# ax.set_ylabel('Ms temperature'+' '+'(degree celsius)')
# plt.savefig("Ms vs. Mn.png",dpi=600,bbox_inches='tight')

# ### Box plots

# sns.set(style='whitegrid')
# fig,ax = plt.subplots(figsize=(16,12))
# bp1=sns.boxplot(data=df[main_elements], width=0.7, showfliers = False)
# ax.set_xlabel('Elements',fontsize=30)
# ax.set_ylabel('Element concentration'+' '+'(%)',fontsize=30)
# plt.tick_params(axis='both', which='major', labelsize=30)
# plt.tight_layout()
# plt.savefig("Box Plot - main elements.png")

# sns.set(style='whitegrid')
# fig,ax = plt.subplots(figsize=(16,12))
# bp2=sns.boxplot(data=df[other_elements], width=0.7, showfliers = False)
# ax.set_xlabel('Elements',fontsize=30)
# ax.set_ylabel('Element concentration'+' '+'(%)',fontsize=30)
# plt.tick_params(axis='both', which='major', labelsize=30)
# plt.tight_layout()
# plt.savefig("Box Plot - other elements.png")

# sns.set(style='whitegrid')
# fig,ax = plt.subplots(figsize=(16,12))
# bp3=sns.boxplot(data=df[crit_temps], width=0.7, showfliers = False)
# ax.set_xlabel('Critical temperatures',fontsize=30)
# ax.set_ylabel('Temperature'+' '+'(degree Celsius)',fontsize=30)
# plt.tick_params(axis='both', which='major', labelsize=30)
# plt.tight_layout()
# plt.savefig("Box Plot - crit temps.png")

# sns.set(style='whitegrid')
# fig,ax = plt.subplots(figsize=(16,12))
# bp4=sns.boxplot(data=df[start_times], width=0.7, showfliers = False)
# ax.set_xlabel('Phase transformations',fontsize=30)
# ax.set_yscale('log')
# ax.set_ylabel('Time for tranformation start'+' '+'(s)',fontsize=30)
# plt.tick_params(axis='both', which='major', labelsize=30)
# plt.tight_layout()
# plt.savefig("Box Plot - start times.png")
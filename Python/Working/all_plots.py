import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

### import dataframe from CSV file

df = pd.read_csv('Crit_temp.csv')

### remove specific alloying elements

drop_elements=['Co', 'N', 'Ti', 'Al', 'Cu']
df.drop(drop_elements, inplace=True, axis=1)

### remove grain size data

df.drop('Grain Size:', inplace=True, axis=1)

### remove colon from column names

df.columns = df.columns.str.replace(':', '')

# ---------------------------------------- #

### pair plots

sns.set_style('darkgrid')

elements=['C', 'Mn', 'Si', 'P', 'S', 'Cr', 'Ni', 'V', 'Mo', 'W']
# main_elements=['C', 'Mn', 'Cr', 'Ni']
main_elements=['C', 'Mn', 'Ni']
# other_elements=list((Counter(elements) - Counter(main_elements)).elements())
other_elements=['Si', 'Cr', 'V', 'Mo', 'W']
P_S=['P', 'S']
crit_temps=['Ms','Mf','Ac1','Ac3']
start_times=['Ferrite_1_Time','Pearlite_1_Time','Bainite_1_Time']
gs=['Grain Size']

pp1=sns.pairplot(df, vars=main_elements)

pp2=sns.pairplot(df, vars=crit_temps)

pp3=sns.pairplot(df, vars=start_times)

pp1.savefig("Pair Plot - elements.png")
pp2.savefig("Pair Plot - crit temps.png")
pp3.savefig("Pair Plot - start times.png")

### box plots

sns.set(style='whitegrid')
fig,ax = plt.subplots(figsize=(8,6))
bp1=sns.boxplot(data=df[main_elements], width=0.7)
ax.set_xlabel('Elements')
ax.set_ylabel('Element concentration'+' '+'(%)')
plt.savefig("Box Plot - main elements.png")

sns.set(style='whitegrid')
fig,ax = plt.subplots(figsize=(8,6))
bp2=sns.boxplot(data=df[other_elements], width=0.7)
ax.set_xlabel('Elements')
ax.set_ylabel('Element concentration'+' '+'(%)')
plt.savefig("Box Plot - other elements.png")

sns.set(style='whitegrid')
fig,ax = plt.subplots(figsize=(8,6))
bp2=sns.boxplot(data=df[P_S], width=0.7)
ax.set_xlabel('Elements')
ax.set_ylabel('Element concentration'+' '+'(%)')
plt.savefig("Box Plot - P and S.png")

sns.set(style='whitegrid')
fig,ax = plt.subplots(figsize=(8,6))
bp3=sns.boxplot(data=df[crit_temps], width=0.7)
ax.set_xlabel('Critical temperatures')
ax.set_ylabel('Temperature'+' '+'(degree Celsius)')
plt.savefig("Box Plot - crit temps.png")

sns.set(style='whitegrid')
fig,ax = plt.subplots(figsize=(8,6))
bp4=sns.boxplot(data=df[start_times], width=0.7)
ax.set_xlabel('Phase transformations')
ax.set_yscale('log')
ax.set_ylabel('Time for tranformation start'+' '+'(s)')
plt.savefig("Box Plot - start times.png")

### scatter plot


# start times vs elements
 
for i in range(0,len(elements)):
    for j in range(0,len(start_times)):
        fig,ax=plt.subplots()
        fig=ax.scatter(df[elements[i]],df[start_times[j]],c=df['C'],cmap='inferno')
        ax.set_xlabel(elements[i]+' '+'content'+' '+'(%)')
        ax.set_ylabel(start_times[j]+' '+'(s)')
        ax.set_yscale('log')
        plt.savefig(start_times[j]+" "+"vs."+" "+elements[i]+".png",dpi=600,bbox_inches='tight')
        
# crit temps vs elements

for i in range(0,len(elements)):
    for j in range(0,len(crit_temps)):
        fig,ax=plt.subplots()
        fig=ax.scatter(df[elements[i]],df[crit_temps[j]],c=df['C'],cmap='inferno')
        ax.set_xlabel(elements[i]+' '+'content'+' '+'(%)')
        ax.set_ylabel(crit_temps[j]+' '+'temperature'+' '+'(degree Celsius)')
        plt.savefig(crit_temps[j]+" "+"vs."+" "+elements[i]+".png",dpi=600,bbox_inches='tight')
        
# start times vs crit temps

for i in range(0,len(crit_temps)):
    for j in range(0,len(start_times)):
        fig,ax=plt.subplots()
        fig=ax.scatter(df[crit_temps[i]],df[start_times[j]],c=df['C'],cmap='inferno')
        ax.set_xlabel(crit_temps[i]+' '+'temperature'+' '+'(degree Celsius)')
        ax.set_ylabel(start_times[j]+' '+'(s)')
        ax.set_yscale('log')
        plt.savefig(start_times[j]+" "+"vs."+" "+crit_temps[i]+".png",dpi=600,bbox_inches='tight')
        
### correlation matrix

# dataframe

corr = df.corr()
corr.style.background_gradient(cmap='coolwarm').set_precision(2)

# heatmap

ax.set_yscale('linear')
sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values)
plt.savefig("correlation matrix - heatmap.png")
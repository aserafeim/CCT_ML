import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.close('all')
### Import dataframe from CSV file

df = pd.read_csv('Crit_temp.csv')

### Set style

# sns.set(style='white')

### Set figure size

fig,ax = plt.subplots(figsize=(10,2))

### Create boxplot

sns.boxplot(df['C'], color='plum', width=.5, notch=False)

### Add title and label

plt.title('C content', fontsize=14)
plt.xlabel('C%')

### Remove spines around figure

sns.despine()

### Define range of values in x-axis

plt.xlim([0,2])
plt.xticks(np.arange(0,2.5,0.5))

### Add text to diagram

props = dict(boxstyle='round', facecolor='plum', alpha=0.2)
ax.text(0.8,0.3, "Eutectoid Steel", fontsize=12, bbox=props)



### Compare several parameters (C,Mn,Si)

# sns.set(style='whitegrid')
fig,ax = plt.subplots(figsize=(8,6))
g = sns.boxplot(data=df[['C','Mn','Si']], width=0.7)
plt.title('Comparative content of alloying elements', fontsize=16)

### Edit y-axis

yint = [0,0.5,1,1.5,2]
plt.yticks(yint)

### Remove specfic spines from figure

sns.despine(top=True,right=True,left=True,bottom=False)

### Ms, Mf, Ac1, Ac3

# sns.set(style='whitegrid')
fig,ax = plt.subplots(figsize=(8,6))
h = sns.boxplot(data=df[['Ms:','Mf:','Ac1:','Ac3:']], width=0.7)
plt.title('Distribution of critical temperatures', fontsize=16)

### Time for transformation start

# sns.set(style='whitegrid')
fig,ax = plt.subplots(figsize=(8,6))
i = sns.boxplot(data=df[['Ferrite_1_Time','Pearlite_1_Time','Bainite_1_Time']], width=0.7)
plt.title('Distribution of transformation start times', fontsize=16)






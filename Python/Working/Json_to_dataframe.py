# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 08:59:37 2022

@author: aserafeim
"""
import pandas as pd
import json
import numpy as np

filename='En 28_p101'
with open(filename+'.json','r') as f:
    data = json.loads(f.read())
kinetics={}
comp={}
crit_temp={}
names=[]


element=[]
# elements=['C','Mn','Mo','Cr','Si','Ni','V']
process=['Austenitization Time:','Austenitization Temp:','Grain Size:']
Temperatures=['Ms:', 'Mf:', 'Ac1:', 'Ac3:']
phases=['Ferrite','Pearlite','Bainite']
status=['Status']
###Store keys in names list
### and create dictionary with T-t information
for i in phases:
    for j in data[i].keys():
        for k in data[i][j].keys():
            names.append(i+'_'+j+'_'+k)
            kinetics[i+'_'+j+'_'+k] = data[i][j][k]

#####Print the data --- not required
for i in range(0,len(names),2):
    print(names[i])
    for j in range(len(kinetics[names[i]])):
        k2,k3=kinetics[names[i]][j],kinetics[names[i+1]][j]
        print(k2,k3)

for i in data.keys():
    if i not in Temperatures+process+phases+status:
        element.append(i)

elements=element+process        
#### create the composition and grain size line of the 
for i in data.keys():
    if i in elements:
            comp[i]=data[i]

df=pd.DataFrame(comp,index=['row 1'])

###Loop over all Time temperature curve and concat them  
for i in range(0,len(names),2):
    df1=pd.DataFrame(list(zip(kinetics[names[i]],kinetics[names[i+1]])),columns=[names[i],names[i+1]])
    df=pd.concat([df,df1],axis=0) 

### Fill Nan  values of the chemical composition and grain size with
### identical values and drop the first row
df=df.fillna(value=comp)    
df.drop(['row 1'])

df.to_csv(filename+'.csv')
# df.to_excel(filename+'.xlsx') 

###Data frame with values of composition and Ms, Ac temperatures

for i in data.keys():
    if i in elements +Temperatures:
            crit_temp[i]=data[i]

df_b=pd.DataFrame(crit_temp,index=[filename])
df_b.to_csv(filename+'crit_temp'+'.csv')

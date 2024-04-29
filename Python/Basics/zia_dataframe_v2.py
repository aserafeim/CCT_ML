filename = '46Mn7.json'     #-----INPUT NAME OF JSON FILE-----#

#import libraries

import json
import pandas as pd

#open json data and load data into 'data' dictionary and 'df' dataframe

f = open(filename)
data = json.load(f)

df = pd.read_json(filename)

#remove packed phase T-t data from columns

df.drop('Ferrite', inplace=True, axis=1)
df.drop('Pearlite', inplace=True, axis=1)
df.drop('Bainite', inplace=True, axis=1)

#remove duplicate non-kinteics data caused by different phase concentration

df.drop_duplicates(inplace=True)

#create dictionaries for storage of different datasets

kinetics={}
comp={}
crit_temp={}
names=[]
element=[]

#create lists of particular data

#process=['Austenitization Time:','Austenitization Temp:','Grain Size:']
process=['Austenitization Temp:']
Temperatures=['Ms:', 'Mf:', 'Ac1:', 'Ac3:']
phases=['Ferrite','Pearlite','Bainite']
status=['Status']
# elements=['C','Si','Mn','Cr','Ni','Mo','V']
elements=['C','Si','Mn']

#create dictionary with T-t data
new=elements+process+Temperatures+status
phases=['Ferrite','Pearlite','Bainite']

for i in phases:
    for j in data[i].keys():
        for k in data[i][j].keys():
            names.append(i+'_'+j+'_'+k)
            kinetics[i+'_'+j+'_'+k] = data[i][j][k]

#loop over T-t curves for each phase concentration and concat the data  
            
for i in range(0,len(names),2):
     df1=pd.DataFrame(list(zip(kinetics[names[i]],kinetics[names[i+1]])),columns=[names[i],names[i+1]])
     df=pd.concat([df,df1],axis=0)
     
#fill composition column nan values

df[new]=df[new].fillna(method='ffill')

# if 'C' in data.keys():
#     df['C'].fillna( method ='ffill', inplace = True)

# if 'Si' in data.keys():
#     df['Si'].fillna( method ='ffill', inplace = True)
    
# if 'Mn' in data.keys():
#     df['Mn'].fillna( method ='ffill', inplace = True)
    
# if 'Cr' in data.keys():
#     df['Cr'].fillna( method ='ffill', inplace = True)
    
# if 'Ni' in data.keys():
#     df['Ni'].fillna( method ='ffill', inplace = True)
    
# if 'Mo' in data.keys():
#     df['Mo'].fillna( method ='ffill', inplace = True)
    
# if 'V' in data.keys():
#     df['V'].fillna( method ='ffill', inplace = True)

# #fill other non-kinetics column nan values

# if 'Ms:' in data.keys():
#     df['Ms:'].fillna( method ='ffill', inplace = True)

# if 'Mf:' in data.keys():
#     df['Mf:'].fillna( method ='ffill', inplace = True)

# if 'Ac1:' in data.keys():
#     df['Ac1:'].fillna( method ='ffill', inplace = True)   
    
# if 'Ac3:' in data.keys():
#     df['Ac3:'].fillna( method ='ffill', inplace = True)
    
# if 'Austenitization Time:' in data.keys():
#     df['Austenitization Time:'].fillna( method ='ffill', inplace = True)
    
# if 'Austenitization Temp:' in data.keys():
#     df['Austenitization Temp:'].fillna( method ='ffill', inplace = True)
    
# if 'Grain Size:' in data.keys():
#     df['Grain Size:'].fillna( method ='ffill', inplace = True)
    
# if 'Status' in data.keys():
#     df['Status'].fillna( method ='ffill', inplace = True)

#drop first row
    
df = df.iloc[1: , :]
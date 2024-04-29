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
boo={}
boo1={}
comp={}
crit_temp={}
names=[]
phase_name=[]
element=[]
time=[]
time1=[]
Temperature=[]
temp1=[]


#create lists of particular data

process=['Austenitization Time:','Austenitization Temp:','Grain Size:']
temps=['Ms:', 'Mf:', 'Ac1:', 'Ac3:']
phases=['Ferrite','Pearlite','Bainite']
status=['Status']
elements=['C','Si','Mn','Cr','Ni','Mo','V']
phases=['Ferrite','Pearlite','Bainite']
nonk=elements+process+temps+status

#create binary columns for each phase concentration

for i in phases:
    for j in data[i].keys():
        for k in data[i][j].keys():
            names.append(i+'_'+j+'_'+k)
            kinetics[i+'_'+j+'_'+k] = data[i][j][k]
            boo[i+'_'+j] = data[i][j][k]
            # boo1[i+'_'+j]=[True for i in range(len(data[i][j][k]))]
                  
#create binary column headers

for i in phases:
    for j in data[i].keys():
        phase_name.append(i+'_'+j) ###could be added in the code above
        
#loop over T-t curves for each phase concentration and store everything in two T-t lists  
            
for i in range(0,len(names),2):
    time.append(kinetics[names[i]])
    Temperature.append(kinetics[names[i+1]])
    # time1+=kinetics[names[i]]
    # temp1+=kinetics[names[i+1]]
    
# for i in range(1,len(names),2):
#     Temperature.append(kinetics[names[i]])
    
#concat binary columns
        
for i in range(0,len(phase_name),1):
     df2=pd.DataFrame(list(zip(boo[phase_name[i]])),columns=[phase_name[i]])
     df=pd.concat([df,df2],axis=0)

#create two T-t columns with all kinetics data, and fix row indexing through new dataframe

#### Done need this if you build timelist and templist in line 72
timelist=[0]
for count, value in enumerate(time):
    for c, val in enumerate (value):
        timelist.append(val)     
     
templist=[0]
for count, value in enumerate(Temperature):
    for c, val in enumerate (value):
        templist.append(val)     

        #### Check pandas insert
df_clean= pd.DataFrame(timelist, columns=['time'])
df_clean["Temperature"] = templist

for col in df.columns:
    df_clean[col]=pd.Series(list(df [col] ))
    
#rearrange T-t columns to be after 'Status'

time_col = df_clean['time']
df_clean.pop('time')
df_clean.insert(df.columns.get_loc('Status') + 2, time_col.name, time_col, allow_duplicates=True)

temp_col = df_clean['Temperature']
df_clean.pop('Temperature')
df_clean.insert(df.columns.get_loc('Status') + 2, temp_col.name, temp_col, allow_duplicates=True)

#fill binary columns with 0 where nan values

df_clean[phase_name]=df_clean[phase_name].fillna(value=0)

#fill binary columns with 1 where non-zero
##wont need that if you define the boolean vector before
for i in range(0,len(phase_name),1):
    df_clean.loc[df_clean[phase_name[i]] > 0, phase_name[i]] = 1

#fill composition column nan values

# df_clean[nonk]=df_clean[nonk].fillna(method='ffill')

if 'C' in data.keys():
    df_clean['C'].fillna( method ='ffill', inplace = True)

if 'Si' in data.keys():
    df_clean['Si'].fillna( method ='ffill', inplace = True)
    
if 'Mn' in data.keys():
    df_clean['Mn'].fillna( method ='ffill', inplace = True)
    
if 'Cr' in data.keys():
    df_clean['Cr'].fillna( method ='ffill', inplace = True)
    
if 'Ni' in data.keys():
    df_clean['Ni'].fillna( method ='ffill', inplace = True)
    
if 'Mo' in data.keys():
    df_clean['Mo'].fillna( method ='ffill', inplace = True)
    
if 'V' in data.keys():
    df_clean['V'].fillna( method ='ffill', inplace = True)

#fill other non-kinetics column nan values

if 'Ms:' in data.keys():
    df_clean['Ms:'].fillna( method ='ffill', inplace = True)

if 'Mf:' in data.keys():
    df_clean['Mf:'].fillna( method ='ffill', inplace = True)

if 'Ac1:' in data.keys():
    df_clean['Ac1:'].fillna( method ='ffill', inplace = True)   
    
if 'Ac3:' in data.keys():
    df_clean['Ac3:'].fillna( method ='ffill', inplace = True)
    
if 'Austenitization Time:' in data.keys():
    df_clean['Austenitization Time:'].fillna( method ='ffill', inplace = True)
    
if 'Austenitization Temp:' in data.keys():
    df_clean['Austenitization Temp:'].fillna( method ='ffill', inplace = True)
    
if 'Grain Size:' in data.keys():
    df_clean['Grain Size:'].fillna( method ='ffill', inplace = True)
    
if 'Status' in data.keys():
    df_clean['Status'].fillna( method ='ffill', inplace = True)

#drop first row

df_clean = df_clean.iloc[1: , :]
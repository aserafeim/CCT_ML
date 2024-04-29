# -*- coding: utf-8 -*-
"""
Created on Mon May  9 22:43:14 2022

@author: alexs
"""

from Json_unpack import *
from tip_temperature import *
import seaborn as sns
import matplotlib.pyplot as plt
from plotting_function import plotting_data

import time
import os, json

plt.close('all')
start_time = time.time()
elements_dic={}
# path_to_json = r'C:\Users\alexs\sciebo\CTT_TTT Images\Atlas_New\JSON files\British En Steels'
# path_to_json = r'C:\Users\kjeau\Desktop\Python\CCT_ML-main'
# path_to_json=r'D:\sciebo\CTT_TTT Images\Datenbank Stahlwissen\JSON files'
path_to_json = r'D:\sciebo\CTT_TTT Images\Atlas_New\JSON files\German Steels - Atlas'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

# print(json_files)

df_Temp_k=pd.DataFrame()
df_Temp_T=pd.DataFrame()
for i in json_files:
    test=unpack_json(i[:-5],path_to_json)
    df_k,df_T,data=test.unpack()
    
    test_tip=find_tip(df_k)
    test_tip.search()
    
    ### Combining the information from all JSON files
    df_Temp_k=pd.concat([df_Temp_k,df_k],axis=0)
    df_Temp_T=pd.concat([df_Temp_T,df_T],axis=0)
    

print("--- %s seconds ---" % (time.time() - start_time))

elements=[x for x in df_Temp_T.columns if len(x)<=2]

# for i in elements:
    
#     elements_dic[i]=0
    
df_Temp_T[elements]=df_Temp_T[elements].fillna(0)

# df_Temp_T.hist(bins=20)
# df_Temp_k.hist(bins=20)

### Rearrange phase starting time columns to the end

ferrite_col = df_Temp_T['Ferrite_1_Time']
df_Temp_T.pop('Ferrite_1_Time')
df_Temp_T.insert(df_Temp_T.columns.get_loc(df_Temp_T.columns[-1]) + 1, ferrite_col.name, ferrite_col, allow_duplicates=True)

pearlite_col = df_Temp_T['Pearlite_1_Time']
df_Temp_T.pop('Pearlite_1_Time')
df_Temp_T.insert(df_Temp_T.columns.get_loc('Ferrite_1_Time') + 1, pearlite_col.name, pearlite_col, allow_duplicates=True)

bainite_col = df_Temp_T['Bainite_1_Time']
df_Temp_T.pop('Bainite_1_Time')
df_Temp_T.insert(df_Temp_T.columns.get_loc('Pearlite_1_Time') + 1, bainite_col.name, bainite_col, allow_duplicates=True)

### Convert dataframe to CSV file

df_Temp_T.to_csv('Crit_temp.csv')

# set
# fig,ax=plt.subplots()

### Create scatter plot for all alloying elements

for i in elements:
    plotting_data(df_Temp_T,i,'Bainite_1_Time','C')
    
plotting_data(df_Temp_T,'Mn','Pearlite_1_Time','Si')
    # fig,ax=plt.subplots()
    # fig=ax.scatter(df_Temp_T[elements[i]],df_Temp_T['Bainite_1_Time'],c=df_Temp_T['C'],cmap='inferno')
    # ax.set_xlabel(elements[i]+' '+'content')
    # ax.set_ylabel('Bainite_1_time')
    # ax.set_yscale('log')
    
# plt.figure()
# sns.countplot(x='Mn', data=data_clean)
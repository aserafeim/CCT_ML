# -*- coding: utf-8 -*-
"""
Created on Mon May  9 22:43:14 2022

@author: alexs
"""

from Json_unpack import *
from tip_temperature import *
import seaborn as sns
import matplotlib.pyplot as plt


import time
import os, json

plt.close('all')
start_time = time.time()
elements_dic={}
# path_to_json = r'C:\Users\alexs\sciebo\CTT_TTT Images\Atlas_New\JSON files\British En Steels'
path_to_json = r'C:\Users\alexs\sciebo\CTT_TTT Images\Atlas_New\JSON files\German Steels - Atlas'
# path_to_json=r'D:\sciebo\CTT_TTT Images\Datenbank Stahlwissen\JSON files'
# path_to_json = r'D:\sciebo\CTT_TTT Images\Atlas_New\JSON files\German Steels - Atlas'
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

df_Temp_T.to_csv('Crit_temp.csv')

set
fig,ax=plt.subplots()

fig1=ax.scatter(df_Temp_T['Mn'],df_Temp_T['Bainite_1_Time'],c=df_Temp_T['C'],cmap='inferno')
ax.set_xlabel('Mn content')
ax.set_yscale('log')
# fig.colorbar(fig1,ax=ax)

fig,ax=plt.subplots()

fig1=ax.scatter(df_Temp_T['Ni'],df_Temp_T['Bainite_1_Time'],c=df_Temp_T['C'],cmap='inferno')
ax.set_xlabel('Ni content')
ax.set_yscale('log')
# fig.colorbar(fig1,ax=ax)


fig,ax=plt.subplots()

fig1=ax.scatter(df_Temp_T['Mo'],df_Temp_T['Bainite_1_Time'],c=df_Temp_T['C'],cmap='inferno')
ax.set_xlabel('Mo content')
ax.set_yscale('log')
# fig.colorbar(fig1,ax=ax)


fig,ax=plt.subplots()
fig1=ax.scatter(df_Temp_T['V'],df_Temp_T['Bainite_1_Time'],c=df_Temp_T['C'],cmap='inferno')
ax.set_xlabel('V content')
ax.set_yscale('log')


fig,ax=plt.subplots()

fig1=ax.scatter(df_Temp_T['Mn'],df_Temp_T['Pearlite_1_Time'],c=df_Temp_T['C'],cmap='inferno')
ax.set_xlabel('Mn content')
ax.set_yscale('log')
# fig.colorbar(fig1,ax=ax)

fig,ax=plt.subplots()

fig1=ax.scatter(df_Temp_T['Ni'],df_Temp_T['Pearlite_1_Time'],c=df_Temp_T['C'],cmap='inferno')
ax.set_xlabel('Ni content')
ax.set_yscale('log')
# fig.colorbar(fig1,ax=ax)

fig,ax=plt.subplots()

fig1=ax.scatter(df_Temp_T['Mo'],df_Temp_T['Pearlite_1_Time'],c=df_Temp_T['C'],cmap='inferno')
ax.set_xlabel('Mo content')
ax.set_yscale('log')
# fig.colorbar(fig1,ax=ax)

fig1=fig,ax=plt.subplots()
ax.scatter(df_Temp_T['V'],df_Temp_T['Pearlite_1_Time'],c=df_Temp_T['C'],cmap='inferno')
ax.set_xlabel('V content')
ax.set_yscale('log')
# fig.colorbar(fig1,ax=ax)

# plt.figure()
# sns.countplot(x='Mn', data=data_clean)
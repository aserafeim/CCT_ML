# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 11:21:03 2022

@author: alexs
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler


data=pd.read_csv('Crit_temp_total.csv')


data_clean=data.drop(['Unnamed: 0','Mf:','Austenitization Time:','Grain Size:','N','Al','Ti','Ferrite_1_Time','Pearlite_1_Time'],axis=1)
data_clean['Austenitization Temp:'].fillna(data_clean['Austenitization Temp:'].mean())
data_clean=data_clean.dropna(subset=['Bainite_1_Time','Austenitization Temp:','Ac3:'])

col_ar=['C',
 'Mn',
 'Si',
 'P',
 'S',
 'Cr',
 'Cu',
 'Ni',
 'V',
 'Mo',
 'W',
 'Co',
 'Austenitization Temp:',
 'Ms:',
 'Ac1:',
 'Ac3:',
 'Bainite_1_Time']

data_clean=data_clean[col_ar]

# data_clean=data_clean.drop(['Ac3:'],axis=1)

features=data_clean.columns[:-4]
target=data_clean.columns[-4:]

X=data_clean[features]
Y=data_clean[target]

scaler=StandardScaler()
scaler.fit(X)
X=scaler.transform(X)

# X=StandardScaler.fit_transform(X)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=700)
error=[]
index=[]
for i in range(2,100,2):
    
    regres=DecisionTreeRegressor(max_depth=i)
    regres.fit(X_train,Y_train)
    
    Y_prediction=regres.predict(X_test)
    Y_pred2=regres.predict(X_train)
    
    RMSE2=np.sqrt(mean_squared_error(y_true=Y_test, y_pred=Y_prediction,multioutput='raw_values'))
    # print('RMSE between train and test',RMSE2)
    # error.append(RMSE2)
    y_true = Y_test 
    y_pred = Y_prediction
    rmspe = (np.sqrt(np.mean(np.square((y_true - y_pred) / y_true)))) * 100
    error.append(rmspe[3])
    index.append(i)
    
# print('relative error',rmspe)
    # RMSE2=np.sqrt(mean_squared_error(y_true=Y_train, y_pred=Y_pred2,multioutput='raw_values'))
    # print('RMSE in the trainining', RMSE2)

# y_true = Y_test 
# y_pred = Y_prediction

# rmspe = (np.sqrt(np.mean(np.square((y_true - y_pred) / y_true)))) * 100
# print('relative error',rmspe)

fig, ax=plt.subplots()

ax.plot(index,error)
ax.set_yscale('log')





# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 16:58:08 2022

@author: aserafeim
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import VarianceThreshold,SelectKBest, f_regression
from scipy import stats

plt.close('all')
# dataframe = pd.read_excel(r'C:\Users\vivia\sciebo\Steel_properties_ML_Mini_Thesis\Mid Mn Data Collection.xlsx')
dataframe = pd.read_excel(r'D:\sciebo\Steel_properties_ML_Mini_Thesis\Mid Mn Data Collection.xlsx')

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
        'Charpey Energy\n(J)','Mo','Si','V','Nb','Ti','N','Zr','B','Cr','S','P'],axis=1)




df_clean=df_clean.dropna()

features=df_clean.columns[:-4]
target=df_clean.columns[-4:]

X=df_clean[features]
Y=df_clean[target]

#### variance threshold
# sel=VarianceThreshold(threshold=(0.8))
# x_vt=sel.fit_transform(df_clean[features])

# fe_vt=df_clean.columns[sel.get_support(indices=True).tolist()]


#### Univariate feature selection

# sel_ufs=SelectKBest(f_regression,k=5)
# x_ufs=sel_ufs.fit_transform(df_clean[features],df_clean[target])

# fe_ufs=df_clean.columns[sel_ufs.get_support(indices=True).tolist()]

#### Normalization 
X = StandardScaler().fit_transform(X)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=100)

error_test = {}
error_train = {}
error_r2 = {}

for i in target:
    error_test[i] = []
    error_train[i] = []
    error_r2[i] = []
    
index=[]

z_s=stats.zscore(df_clean)<3

df_clean[z_s.all(axis=1)]

for i in range(2,120,2):
    regressor2 = DecisionTreeRegressor(max_depth=i)
    regressor2.fit(X_train, Y_train)
    Y_prediction = regressor2.predict(X_test)
    Y_prediction_train = regressor2.predict(X_train)
    # RMSE2 =np.sqrt( mean_squared_error(y_true = Y_test, y_pred = Y_prediction,multioutput='raw_values'))
    # print(RMSE2)
    y_true = Y_test 
    y_pred = Y_prediction
    # rmspe_test = (np.sqrt(np.mean(np.square((y_true - y_pred) / y_true)))) * 100
    # rmspe_train = (np.sqrt(np.mean(np.square((Y_train - Y_prediction_train) / Y_train)))) * 100
    MSE=mean_absolute_error(Y_test,Y_prediction,multioutput='raw_values')
    # rmspe_test = np.mean(np.abs((y_true - y_pred)) / y_true) * 100
    # rmspe_train = np.mean(np.abs((Y_train - Y_prediction_train)) / Y_train) * 100
    r2_error=r2_score(y_true, y_pred, multioutput='raw_values')
    # print('depth:',i)
    # print(rmspe)    

    
    for count, k in enumerate(target):
        # error_train[k].append(rmspe_train[k])
        error_test[k].append(MSE[count])
        error_r2[k].append(r2_error[count])
    index.append(i)


for count, k in enumerate(target):

    fig,ax=plt.subplots()
    # ax.plot(index,error_train[k],label='Train error_'+k)
    ax.plot(index,error_test[k],label='Test error_'+k)
    ax.set_yscale('log')
    ax.plot(index,error_r2[k],label='Test error_r2'+k)
    # ax.set_yscale('log')
    
    ax.set_xlabel('Tree Depth')
    ax.set_ylabel('Error_'+k)
    ax.legend()
    print(k,min(error_test[k]))
    print(k,max(error_r2[k]))
    
    fig, ax = plt.subplots()
    
    ax.scatter(Y_test[k], Y_prediction[:,count])
    ax.set_xlabel(k+' Experimental')
    ax.set_ylabel(k+' Elongation Predicted')
    ax.set_ylim(min(ax.get_xlim()[0],ax.get_ylim()[0]),max(ax.get_xlim()[1],ax.get_ylim()[1]))
    ax.set_xlim(min(ax.get_xlim()[0],ax.get_ylim()[0]),max(ax.get_xlim()[1],ax.get_ylim()[1]))
    diag_line, = ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--")
    plt.show()


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
from sklearn.metrics import mean_squared_error, r2_score,max_error,mean_squared_error,mean_absolute_error,mean_absolute_percentage_error
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from Error_searching import error_lookup
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

# def lookup_error(X_test,Y_test,Y_pred):
plt.close('all')
# dataframe = pd.read_excel(r'C:\Users\vivia\sciebo\Steel_properties_ML_Mini_Thesis\Mid Mn Data Collection.xlsx')
# dataframe = pd.read_excel(r'D:\sciebo\Steel_properties_ML_Mini_Thesis\Mid Mn Data Collection.xlsx')
dataframe = pd.read_excel(r'C:\Users\alexs\sciebo\Steel_properties_ML_Mini_Thesis\Python codes\ML\dataframe with cold & hot.xlsx')

# dataframe.columns

# df_clean=dataframe.drop(['S. No', 'Title', 'DOI','Ni','Cu','Homogenization Temp (C)',
#         'Homogenization Time (s)', 'Hot Forging Temp (C)',
#         'Hot Forging Thickness Reduction (%)', 'Hot Forging\nThickness (mm)',
#         'Reheated\nTemp (C)', 'Hot Rolling Temp (C)',
#         'Hot Rolling Thickness Reduction (%)', 'Hot Rolling Thickness (mm)',
#         'Homogenization Annealing Temp (C)',
#         'Homogenization Annealing Time (s)', 'Quenching',
#         'Cold Rolling Thickness Reduction (%)', 'Cold Rolling Thickness (mm)',
#         'Austenitizing Temp\n(C)', 'Austenitizing Time\n(s)', 'Quenching.1',
#         'Heating Rate\n(C/s)','Heating Rate\n(C/s).1', 'Second\nAnnealing\nTemp (C)',
#         'Second\nAnnealing\nTime\n(s)', 'Second\nAnnealing\nQuenching',
#         'Tempering\nTemp\n(C)', 'Tempering\nTime\n(s)', 'Tempering\nQuenching', 'Cooling Rate\n(C/s)',
#        'Quenching.2', 'Ferrite\n(%)',
#        'Martensite\n(%)', 'Martensite +\nAustenite\n(%)',
#        'Prior Austenite Grain Size\n(microm)', 'Martensite Substructure Size',
#        'Retained Austenite Size\n(Microm)', 'Retained Ferrite Size\n(Microm)',
#        'Martensite +\nAustenite Size\n(Microm)',
#        'Mn content in Retained Austensite\n(wt%)',
#        'Yield Point Elongation\n(%)\nHow long lueders band is',
#        'Charpey Energy\n(J)','Mo','Si','V','Nb','Ti','N','Zr','B','Cr','S','P'],axis=1)

df_clean=dataframe.drop(['Unnamed: 0', 'P', 'S', 'Mo', 'V', 'Cr', 'Nb',
        'B', 'Zr', 'N', 'Ti'],axis=1)

# df_clean=df_clean.dropna()

df_clean=df_clean[df_clean.Si < 1.5]
df_clean=df_clean[df_clean.Mn < 8]
df_clean=df_clean[4 < df_clean.Mn]

features=df_clean.columns[:-5]
# target=df_clean.columns[[-4,-1]]
target=df_clean.columns[-3:-1]


### -1 : UTS
### -2 : Total elongation
### -3 : Uniform elongation
### -4 : Yield strength
### -5 : Retained Austenite

# df_clean[target].hist()
df_clean=df_clean.dropna(subset=target)
df_clean=df_clean.dropna(subset=features)

# df_clean=df_clean[0.5<df_clean['Uniform Elongation\n(%)']]

X=df_clean[features]
Y=df_clean[target]

# Y=np.sqrt(Y)
X = StandardScaler().fit_transform(X)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=500)
# Y_train=np.sqrt(Y_train)

X_train_d=pd.DataFrame(X_train)
X_train_d=X_train_d.loc[X_train_d.index.repeat(10)].reset_index(drop=True)
X_train_d=X_train_d.sample(frac=1).reset_index(drop=True)
X_train = X_train_d.to_numpy()


Y_train_d=pd.DataFrame(Y_train)
Y_train_d=Y_train_d.loc[Y_train_d.index.repeat(10)].reset_index(drop=True)
Y_train_d=Y_train_d.sample(frac=1).reset_index(drop=True)
Y_train = Y_train_d.to_numpy()





# error_test = {}
# error_train = {}
# error_r2 = {}

# for i in target:
#     error_test[i] = []
#     error_train[i] = []
#     error_r2[i] = []
    
index=[]

net=(300,300,300,300,)
regr = MLPRegressor(hidden_layer_sizes=net, activation='relu',random_state=100,solver='adam', max_iter=100000)

# print(cross_val_score(regr,X_train,Y_train,cv=3))

regr.fit(X_train,Y_train)

Y_prediction=regr.predict(X_test)
# Y_prediction=np.power(Y_prediction,2)
# Y_test=np.power(Y_test,2)
print(net)
print(regr.score(X_test,Y_test))

r2=r2_score(Y_test,Y_prediction,multioutput='raw_values')
print(r2)
MAE=mean_absolute_error(Y_test,Y_prediction,multioutput='raw_values')
print(MAE)
MAPE=mean_absolute_percentage_error(Y_test,Y_prediction,multioutput='raw_values')
print(MAPE)
MSE=mean_squared_error(Y_test,Y_prediction,multioutput='raw_values')
print(MSE)



for count, k in enumerate(target):
    fig, ax = plt.subplots()
    if len(target)==1:
        ax.scatter(Y_test, Y_prediction)
    else:
        ax.scatter(Y_test[k], Y_prediction[:,count])
    ax.set_xlabel(k+'_Experimental')
    ax.set_ylabel(k+'_Predicted')
    ax.set_ylim(min(ax.get_xlim()[0],ax.get_ylim()[0]),max(ax.get_xlim()[1],ax.get_ylim()[1]))
    ax.set_xlim(min(ax.get_xlim()[0],ax.get_ylim()[0]),max(ax.get_xlim()[1],ax.get_ylim()[1]))
    diag_line, = ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--")
    plt.show()


# X_crit=error_lookup(X_test,y_true,y_pred)

# fig,ax=plt.subplots()
# ax.plot(index,error_train[k],label='Train error_'+k)
# ax.plot(index,error_test[k],label='Test error_'+k)
# ax.set_yscale('log')
# ax.plot(index,error_r2[k],label='Test error_r2'+k)
# # ax.set_yscale('log')

# ax.set_xlabel('Tree Depth')
# ax.set_ylabel('Error_'+k)
# ax.legend()
# print(k,min(error_test[k]))


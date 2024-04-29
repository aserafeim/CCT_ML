import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
from sklearn import svm
from statsmodels.tools.eval_measures import rmse
import statsmodels.api as sm
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
from sklearn.feature_selection import RFECV
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LassoCV
from sklearn.neural_network import MLPRegressor
from sklearn import metrics

### import dataframe from csv

data=pd.read_csv('Crit_temp.csv')

### drop columns and fill columns wherever needed

data_clean=data.drop(['Unnamed: 0','Mf:','Austenitization Time:','Grain Size:','N','Al','Ti','Ferrite_1_Time','Pearlite_1_Time'],axis=1)
data_clean['Austenitization Temp:'].fillna(data_clean['Austenitization Temp:'].mean())
data_clean=data_clean.dropna(subset=['Bainite_1_Time','Austenitization Temp:','Ac3:'])

### define column order

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

### creating feature set and target set

features=data_clean.columns[:-4]
target=data_clean.columns[-4:]

x=data_clean.drop(target,axis=1)
# y=data_clean[target]
y=data_clean['Bainite_1_Time']
y=y.to_frame()

### feature scaling (normalization)

scaler=StandardScaler()

scaler.fit(x)
x=scaler.transform(x)

# scaler.fit(y)
# y=scaler.transform(y)

### define test set and training set

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=400)

### model training

mlp=MLPRegressor(hidden_layer_sizes=(100,100,100,),activation='logistic',max_iter=2000)
mlp.fit(x_train,y_train)

### regression metrics

mae=metrics.mean_absolute_error(y_train,mlp.predict(x_train))
mse=metrics.mean_squared_error(y_train,mlp.predict(x_train))
rsq=metrics.r2_score(y_train,mlp.predict(x_train))

y_pred=mlp.predict(x_test)

print(mae,mse,rsq)

fig,ax=plt.subplots()
# fig=ax.scatter(y_test[:,0],y_pred[:,0])
fig=ax.scatter(y_test,y_pred)
ax.set_xscale('log')
ax.set_yscale('log')

# fig,ax=plt.subplots()
# fig=ax.scatter(y_test[:,1],y_pred[:,1])
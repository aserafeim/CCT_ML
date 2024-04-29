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

x=data_clean[features]
# y=data_clean[target]
y=data_clean['Ms:']
y=y.to_frame()

### feature scaling (normalization)

scaler=StandardScaler()

scaler.fit(x)
x=scaler.transform(x)

scaler.fit(y)
y=scaler.transform(y)

### define test set and training set

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=1)

### create model

reg=svm.SVR(kernel='linear',C=1.0,epsilon=0.1)
reg.fit(x_train,y_train)

### model evaluation

y_pred=reg.predict(x_test)
print(rmse(y_pred,y_test))

fig,ax=plt.subplots()
fig=ax.scatter(y_test,y_pred)









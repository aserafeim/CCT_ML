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

x_train=data_clean[features]
# y=data_clean[target]
y=data_clean['Ms:']
# y=y.to_frame()


scaler=StandardScaler()

scaler.fit(x_train)
x=scaler.transform(x_train)

x=pd.DataFrame(x, columns = x_train.columns)

### variance threshold (removing low var features)

sel=VarianceThreshold(threshold=(0.8))
x_vt=sel.fit_transform(x)

fe_vt=x.columns[sel.get_support(indices=True).tolist()]

### univariate feature selection

sel_ufs=SelectKBest(f_regression,k=8)
x_ufs=sel_ufs.fit_transform(x,y)

fe_ufs=x.columns[sel_ufs.get_support(indices=True).tolist()]

### recursive feature elimination

sel_rfc=RFECV(RandomForestClassifier(),scoring='accuracy')

sel_rfc.fit(x,y)
sel_rfc.score(x,y)
fe_rfc=x.columns[sel_rfc.get_support(indices=True).tolist()]

### feature selection using SelectFromModel

n=SelectFromModel(LassoCV())
n.fit_transform(x,y)

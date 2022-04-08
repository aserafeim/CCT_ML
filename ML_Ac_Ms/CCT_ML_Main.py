# -*- coding: utf-8 -*-
"""
Created on Wed May 26 04:47:53 2021

@author: aserafeim
"""
import numpy as np
import pandas as pd
import os
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVR
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.cluster import KMeans
from sklearn.model_selection import validation_curve
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import learning_curve
from sklearn.kernel_ridge import KernelRidge
from math import sqrt
from itertools import cycle, islice
from pandas.plotting import parallel_coordinates

plt.close('all')
data_raw= pd.read_excel('Raw_ZTU_data.xlsx')
data=data_raw.copy()
col=data.columns
drop=['Art', 'Laufende Nr', 'Werkstoff-Nr.', 'Werksbezeichnung', 'Kurzname','Schmelze','As', 'Co','Ac1b [C]', 'Ac1e [C]', 'Anmerkungen']
data=data.drop(columns=drop)


#remove rows with no composition ie carbon = Nan

test=data.dropna(subset=['C'])

#remove rows with no Ms and/or Ac

test2=test.dropna(subset=['Ac1 [C]', 'Ac3 [C]', 'Ms [C]'])

#remove rows that are duplicates i.e. duplicate composition.

composition=['C', 'Si', 'Mn', 'P', 'S', 'Cr', 'Mo', 'Ni', 'V', 'Al',
       'Cu', 'Ti', 'Nb', 'N', 'B', 'W']
test3=test2.drop_duplicates(subset=composition)

#Replace NaN in N with mean

val={'N': test3['N'].mean()}

test4=test3.fillna(value=val)
#Replace NaN values in composition with zeroes

data_final=test4.fillna(0.0)

#Plot histogram of element distribution   
# data_final.hist(column=composition,bins=20)
#plot scatter plots


features=data_final.columns[:-3]
target=data_final.columns[-3:]

X=data_final[features]
Y=data_final[target]

X = StandardScaler().fit_transform(X)


#PCA

pca = PCA(n_components = None, svd_solver='randomized',whiten=True)

X_trainedPCA = pca.fit_transform(X)

var=np.cumsum(np.round(pca.explained_variance_ratio_, decimals=3)*100)
plt.ylabel('Variance')
plt.xlabel('# of features')
plt.title('PCA')
plt.ylim(min(var),100.5)
plt.style.context('seaborn-whitegrid')
plt.axhline(y=80, color = 'r', linestyle='--')
plt.plot(var)
plt.xticks(np.arange(len(var)),np.arange(1,len(var)+1))
plt.savefig('PCA.png',dpi=600,bbox_inches='tight')


#Feature variance

# var_thresh=VarianceThreshold(threshold=0.0)
# scaler=RobustScaler()
# scaled=scaler.fit_transform(data_final)

# data_scaled=pd.DataFrame(scaled)
# test_var=var_thresh.fit(data_scaled)

#Feature corelation

# corr = data_final.corr()
  

# sn.heatmap(corr, annot = True)

#############
###Training##
#############


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=324)


######Regression#######

regressor = LinearRegression()
regressor.fit(X_train, Y_train)

Y_prediction = regressor.predict(X_test)


RMSE = np.sqrt(mean_squared_error(y_true = Y_test, y_pred = Y_prediction,multioutput='raw_values'))
print(RMSE)


######Tree########


train_scores, valid_scores = validation_curve(Ridge(), X, Y, "alpha",
                                              np.logspace(-7, 3, 3),
                                              cv=5)

regressor2 = DecisionTreeRegressor(max_depth=20)
regressor2.fit(X_train, Y_train)

Y_prediction = regressor2.predict(X_test)

RMSE2 =np.sqrt( mean_squared_error(y_true = Y_test, y_pred = Y_prediction,multioutput='raw_values'))
print(RMSE2)




f, ax = plt.subplots(figsize=(6, 6))

ax.scatter(np.array(Y_test)[:,2], Y_prediction[:,2], c=".3")
ax.set_ylim(min(min(np.array(Y_test)[:,2]), min(Y_prediction[:,2])),max(max(np.array(Y_test)[:,2]), max(Y_prediction[:,2])))
ax.set_xlim(min(min(np.array(Y_test)[:,2]), min(Y_prediction[:,2])),max(max(np.array(Y_test)[:,2]), max(Y_prediction[:,2])))
f.suptitle('Ms Temperature- RMSE:'+str(round(RMSE2[2])))
ax.set_xlabel('Ms Experimental')
ax.set_ylabel('Ms Predicted')
diag_line, = ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c=".3")
plt.show()
f.savefig('Ms_prediction.png',dpi=600,bbox_inches='tight')

f, ax = plt.subplots(figsize=(6, 6))

ax.scatter(np.array(Y_test)[:,1], Y_prediction[:,1], c=".3")
ax.set_ylim(min(min(np.array(Y_test)[:,1]), min(Y_prediction[:,1])),max(max(np.array(Y_test)[:,1]), max(Y_prediction[:,1])))
ax.set_xlim(min(min(np.array(Y_test)[:,1]), min(Y_prediction[:,1])),max(max(np.array(Y_test)[:,1]), max(Y_prediction[:,1])))
f.suptitle('Ac3 temperature- RMSE:'+str(round(RMSE2[1])))
ax.set_xlabel('Ac3 Experimental')
ax.set_ylabel('Ac3 Predicted')
diag_line, = ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c=".3")
plt.show()
f.savefig('Ac3_prediction.png',dpi=600,bbox_inches='tight')


f, ax = plt.subplots(figsize=(6, 6))

ax.scatter(np.array(Y_test)[:,0], Y_prediction[:,0], c=".3")
ax.set_ylim(min(min(np.array(Y_test)[:,0]), min(Y_prediction[:,0])),max(max(np.array(Y_test)[:,0]), max(Y_prediction[:,0])))
ax.set_xlim(min(min(np.array(Y_test)[:,0]), min(Y_prediction[:,0])),max(max(np.array(Y_test)[:,0]), max(Y_prediction[:,0])))
f.suptitle('Ac1 Temperature- RMSE:'+str(round(RMSE2[0])))
ax.set_xlabel('Ac1 Experimental')
ax.set_ylabel('Ac1 Predicted')
diag_line, = ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c=".3")
plt.show()
f.savefig('Ac1_prediction.png',dpi=600,bbox_inches='tight')


# plt.figure()
# plt.scatter(Y_test, Y_prediction)
















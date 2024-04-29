import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.neural_network import MLPRegressor
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.utils import shuffle
from sklearn.model_selection import GridSearchCV
import warnings
import pickle
import sklearn
warnings.filterwarnings("ignore")

### import dataframe from csv

data=pd.read_csv('crit_temp_bs_bt.csv')

### remove outliers

data = data[data.C < 0.8]
data = data[data.Mn < 1.8]
data = data[data.Si < 0.6]
data = data[data.Cr < 2]
data = data[data.Cu < 0.5]
data = data[data.Ni < 2.5]
data = data[data.V < 0.1]
data = data[data.Mo < 1]
data = data[data.W < 0.1]
# data = data[data['Bainite_1_Time'] < 20]
# data = data[data.Co < 0.5]

# data = data[data.Pearlite_1_Time < 5000]
# data = data[data.Bainite_1_Time < 40]

### drop columns and fill columns wherever needed

data_clean = data.drop(['Unnamed: 0','Mf:','Austenitization Time:','Grain Size:','N','Al','Ti'],axis=1)
data_clean['Austenitization Temp:'].fillna(data_clean['Austenitization Temp:'].mean())
data_clean = data_clean.dropna(subset=['Bainite_1_Time','Austenitization Temp:'])

### creating feature set and target set

data_clean = shuffle(data_clean)
data_clean.reset_index(inplace=True, drop=True)
target=['Bainite_1_Time']
x = data_clean[['C','Mn','Si','Cr','Ni','Mo','P','S','Austenitization Temp:']]
y = data_clean[target]
# y = np.log(y)



### feature scaling (normalization)

scaler = StandardScaler()
# scaler = MinMaxScaler(feature_range=(-1, 1))

scaler.fit(x)
x = scaler.transform(x)

### define test set and training set

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=1)

### replicate training sets

# x_train_d = pd.DataFrame(x_train)
# x_train_d = x_train_d.loc[x_train_d.index.repeat(2)].reset_index(drop=True)
# x_train = shuffle(x_train_d).to_numpy()


# y_train_d = pd.DataFrame(y_train)
# y_train_d = y_train_d.loc[y_train_d.index.repeat(2)].reset_index(drop=True)
# y_train = shuffle(y_train_d).to_numpy()

### model training

# current=(500,500,500,500,500,)

a=np.logspace(-7,1,20)
mlp = MLPRegressor(hidden_layer_sizes=(50,50,50,),activation='relu',max_iter=10000,random_state=1)
# mlp.fit(x_train,y_train)

# y_pred = mlp.predict(x_test)


clf = GridSearchCV(estimator=mlp, param_grid=dict(alpha=a),cv=5,verbose=3,n_jobs=1)

#,scoring='neg_mean_absolute_percentage_error'
clf.fit(x_train,y_train)
print(clf.best_score_)
print(clf.best_estimator_.alpha)

Y_prediction = clf.predict(x_test)
# y_pred = np.exp(Y_prediction)
# Y_test = np.exp(y_test)

y_pred = Y_prediction
Y_test = y_test
### model score

# print("model score = ",(mlp.score(x_test,y_test)))

### regression metrics

mae=metrics.mean_absolute_error(y_test,y_pred)
mse=metrics.mean_squared_error(y_test,y_pred)
rsq=metrics.r2_score(y_test,y_pred)
mape=metrics.mean_absolute_percentage_error(y_test,y_pred)

print("mae = ",mae," , mse = ",mse," , rsq = ",rsq," , mape = ",mape)


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


# model_name = 'NN_B1_t_Standard_25x3_log_output.sav'
# scaler_name='NN_B1_t_scaler.sav'

# pickle.dump(clf, open(model_name, 'wb'))
# pickle.dump(scaler, open(scaler_name, 'wb'))

# np.save('NN_B1_t_X_test',x_test)

# Y_test.to_csv('NN_B1_t_Y_test.csv')

### cross validation score

# cv_score = cross_val_score(mlp,x,y,cv=5)

# print("cv score = ",cv_score)
# print("%0.2f accuracy with a standard deviation of %0.2f" % (cv_score.mean(), cv_score.std()))
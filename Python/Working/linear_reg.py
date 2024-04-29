import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.utils import shuffle
from sklearn.model_selection import GridSearchCV
from sklearn import datasets, linear_model
from sklearn.linear_model import LassoCV
import warnings
import pickle
import sklearn
import statsmodels.api as sm
from scipy import stats

plt.close('all')

def plot_expvspred(Y_test,Y_prediction,target):
    
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
        
        return fig

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



target=['start_Bainite_1_Temperature']

data_clean = data.drop(['Unnamed: 0','Mf:','Austenitization Time:','Grain Size:','N','Al','Ti','P','S'],axis=1)
data_clean['Austenitization Temp:'].fillna(data_clean['Austenitization Temp:'].mean())
data_clean = data_clean.dropna(subset=[target[0],'Austenitization Temp:'])


### creating feature set and target set

# data_clean = shuffle(data_clean)
data_clean.reset_index(inplace=True, drop=True)

x = data_clean[['C','Mn','Si','Ni','Cr','Mo','Austenitization Temp:']]
y = data_clean[target]


### feature scaling (normalization)

scaler = StandardScaler()
# scalery = MinMaxScaler(feature_range=(-1, 1))
# scalery = StandardScaler()
# y=np.log(y)

scaler.fit(x)
x = scaler.transform(x)

# scalery.fit(y)
# y=scalery.transform(y)


# ### define test set and training set

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=1234)

regr = linear_model.LinearRegression()

las=linear_model.Lasso()

# model=sm.OLS(y_train,x_train)
# results=model.fit()

# aa=results.resid


lacv=LassoCV
a=np.logspace(-3,1,100)
# clf = GridSearchCV(estimator=las, param_grid=dict(alpha=a),cv=5,verbose=3,n_jobs=1)

clf = lacv(cv=5,verbose=3)


clf.fit(x_train,y_train)

# cv_res=clf.cv_results_

# df = pd.DataFrame(clf.cv_results_)

# print('Best score', clf.score(x_train,y_train))
# print('Best parameter', clf.best_estimator_.alpha)
# scores = cross_val_score(las, x_train, y_train, cv=3)

# # fig,ax=plt.subplots()

# # ax.scatter(aa.index,aa)

y_pred=clf.predict(x_test)


mae=metrics.mean_absolute_error(y_test,y_pred)
mse=metrics.mean_squared_error(y_test,y_pred)
rsq=metrics.r2_score(y_test,y_pred)
mape=metrics.mean_absolute_percentage_error(y_test,y_pred)


print("mae = ",mae," , mse = ",mse," , rsq = ",rsq," , mape = ",mape)

fig1=plot_expvspred(y_test,y_pred,target)
# y = np.log(y)
params = np.append(clf.intercept_,clf.coef_)
predictions = y_pred

newX = pd.DataFrame({"Constant":np.ones(len(x_train))}).join(pd.DataFrame(x_train))
MSE = (sum((y_train-predictions)**2))/(len(newX)-len(newX.columns))

# Note if you don't want to use a DataFrame replace the two lines above with
# newX = np.append(np.ones((len(X),1)), X, axis=1)
# MSE = (sum((y-predictions)**2))/(len(newX)-len(newX[0]))

var_b = MSE*(np.linalg.inv(np.dot(newX.T,newX)).diagonal())
sd_b = np.sqrt(var_b)
ts_b = params/ sd_b

p_values =[2*(1-stats.t.cdf(np.abs(i),(len(newX)-len(newX[0])))) for i in ts_b]

sd_b = np.round(sd_b,3)
ts_b = np.round(ts_b,3)
p_values = np.round(p_values,3)
params = np.round(params,4)

myDF3 = pd.DataFrame()
myDF3["Coefficients"],myDF3["Standard Errors"],myDF3["t values"],myDF3["Probabilities"] = [params,sd_b,ts_b,p_values]
print(myDF3)
# print(results.summary())
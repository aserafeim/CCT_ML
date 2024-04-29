import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler

data=pd.read_csv('CRIT_TEMP.csv')

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
data = data[data.Co < 0.5]

data = data[data.Pearlite_1_Time < 5000]

### drop columns and fill columns wherever needed

data_clean=data.drop(['Unnamed: 0','Mf:','Austenitization Time:','Grain Size:','N','Al','Ti','Ferrite_1_Time','Pearlite_1_Time'],axis=1)
data_clean['Austenitization Temp:'].fillna(data_clean['Austenitization Temp:'].mean())
data_clean=data_clean.dropna(subset=['Bainite_1_Time','Austenitization Temp:','Ac3:'])
data_clean=data_clean.dropna(subset=['Ms:'])

### replicating rows 

data_clean=data_clean.loc[data_clean.index.repeat(3)].reset_index(drop=True)

features=data_clean.columns[:-4]
target=data_clean.columns[-4:]

# X=data_clean[features]
# Y=data_clean[target]

X=data_clean[['C','Mn','Si','Cr','Ni','Mo','P','S','Austenitization Temp:']]
# Y=data_clean[['Ferrite_1_Time','Pearlite_1_Time','Bainite_1_Time']]
Y=data_clean[['Bainite_1_Time']]

scaler=StandardScaler()
scaler.fit(X)
X=scaler.transform(X)

# X=StandardScaler.fit_transform(X)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=3)

regres=DecisionTreeRegressor(max_depth=20)
regres.fit(X_train,Y_train)

Y_prediction=regres.predict(X_test)

fig, ax = plt.subplots()
ax.scatter(Y_test, Y_prediction)
ax.set_xlabel('Test')
ax.set_ylabel('Prediction')
ax.set_ylim(min(ax.get_xlim()[0],ax.get_ylim()[0]),max(ax.get_xlim()[1],ax.get_ylim()[1]))
ax.set_xlim(min(ax.get_xlim()[0],ax.get_ylim()[0]),max(ax.get_xlim()[1],ax.get_ylim()[1]))
diag_line, = ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--")
plt.show()





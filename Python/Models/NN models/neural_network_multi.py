import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn import metrics

### import dataframe from csv

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

data_clean=data.drop(['Unnamed: 0','Mf:','Austenitization Time:','Grain Size:','N','Al','Ti'],axis=1)
data_clean['Austenitization Temp:'].fillna(data_clean['Austenitization Temp:'].mean())
data_clean=data_clean.dropna(subset=['Ferrite_1_Time','Pearlite_1_Time','Bainite_1_Time','Austenitization Temp:','Ac3:','Ms:'])

### boxplot of elements content

# elements=['C', 'Mn', 'Si', 'P', 'S', 'Cr', 'Cu', 'Ni', 'V', 'Mo', 'W', 'Co','Bainite_1_Time']

# sns.set(style='whitegrid')
# fig,ax = plt.subplots(figsize=(8,6))
# g = sns.boxplot(data=data_clean[elements], width=0.7)
# plt.title('Comparative content of alloying elements', fontsize=16)

### replicating rows 

data_clean=data_clean.loc[data_clean.index.repeat(2)].reset_index(drop=True)

### creating feature set and target set

features=data_clean.columns[:-4]
target=data_clean.columns[-4:]

# x=data_clean.drop(target,axis=1)
# y=data_clean[target]
x=data_clean[['C','Mn','Si','Cr','Ni','Mo','P','S','Austenitization Temp:']]
y=data_clean[['Ms:','Ac1:','Ac3:','Ferrite_1_Time','Pearlite_1_Time','Bainite_1_Time']]
# y=data_clean[['Bainite_1_Time']]

### feature scaling (normalization)

scaler=StandardScaler()

scaler.fit(x)
x=scaler.transform(x)

# scaler.fit(y)
# y=scaler.transform(y)

### define test set and training set

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=1)

### model training

mlp=MLPRegressor(hidden_layer_sizes=(500,500,),activation='logistic',max_iter=10000)
mlp.fit(x_train,y_train)

### regression metrics

mae=metrics.mean_absolute_error(y_train,mlp.predict(x_train))
mse=metrics.mean_squared_error(y_train,mlp.predict(x_train))
rsq=metrics.r2_score(y_train,mlp.predict(x_train))
mape=metrics.mean_absolute_percentage_error(y_train,mlp.predict(x_train))

y_pred=mlp.predict(x_test)

print(mae,mse,rsq,mape)

### plot prediction against test of target

fig, ax = plt.subplots()
ax.scatter(y_test, y_pred)
ax.set_xlabel('Test')
ax.set_ylabel('Prediction')
ax.set_ylim(min(ax.get_xlim()[0],ax.get_ylim()[0]),max(ax.get_xlim()[1],ax.get_ylim()[1]))
ax.set_xlim(min(ax.get_xlim()[0],ax.get_ylim()[0]),max(ax.get_xlim()[1],ax.get_ylim()[1]))
diag_line, = ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--")
plt.show()
import pandas as pd

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

### repeat rows n times

df=data_clean.loc[data_clean.index.repeat(3)].reset_index(drop=True)
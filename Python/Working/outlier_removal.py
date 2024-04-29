import pandas as pd
from scipy import stats

df=pd.read_csv('Crit_temp.csv')

### IQR (percentile)

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

df1 = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

### Based on condition

df2 = df[df.Cr < 5]

# sc=stats.zscore(df[1:])


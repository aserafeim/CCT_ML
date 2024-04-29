# -*- coding: utf-8 -*-
"""
Created on Tue May 31 12:10:23 2022

@author: aserafeim
"""
import pandas as pd
import numpy as np


a=np.array([[1,2,3],[3,4,5],[6,7,8]])
d = {'col1': [0, 1, 2, 3], 'col2': pd.Series([2, 3], index=[2, 3])}

d1 = {'col1': [5, 6, 7, 8], 'col3': pd.Series([54,12, 23], index=[1,2, 3])}
test=pd.DataFrame(data=d, index=[0, 1, 2, 3])
test1=pd.DataFrame(data=d1, index=[0, 1, 2, 3])

##Nan value handling

test.isna()

# test.fillna(0)


###descriptive statistics
desc=test.describe()


###accessing values
test['col2'][2]


###concat

###concat by collumn
test_conc_col=pd.concat([test,test1],axis=0)

###concat by row

# test_conc_row=pd.concat([test,test1],axis=1)

test_conc_col.hist()
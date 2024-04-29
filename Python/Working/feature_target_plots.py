import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.polynomial import Polynomial
from numpy.polynomial import Chebyshev
plt.close('all')
df_b = pd.read_csv('crit_temp_bs_bt.csv')

# x=['C', 'Mn', 'Si', 'P', 'S', 'Cr', 'Cu', 'Ni', 'V', 'Al', 'Ti', 'Mo', 'W', 'N', 'Austenitization Temp']
x=['C', 'Mn', 'Si', 'P', 'S', 'Cr', 'Ni', 'Austenitization Temp']

y1=['Ms','Ac1','Ac3','Bainite_1_Temperature_at min','start_Bainite_1_Temperature']
y2=['Ferrite_1_Time','Pearlite_1_Time','Bainite_1_Time']

### remove colon from column name

df_b.columns = df_b.columns.str.replace(':', '')
df_b=df_b.dropna(axis=0,subset=['Austenitization Temp'])
### replace 0 with nan

# df.replace(0, np.nan, inplace=True)

# for i in range(0,len(x)):
#     for j in range(0,len(y1)):
#         fig1=sns.lmplot(x=x[i], y=y1[j], data=df, ci=None)
#         # plt.savefig(r'images/' + x[i]+" "+"vs."+" "+y1[j]+".png",dpi=600,bbox_inches='tight')

# for i in range(0,len(x)):
#     for j in range(0,len(y2)):
#         fig2=sns.lmplot(x=x[i], y=y2[j], data=df, ci=None)
#         fig2.set(yscale='log')
        # plt.savefig(r'images/' + x[i]+" "+"vs."+" "+y2[j]+".png",dpi=600,bbox_inches='tight')
        
# hist_x=df.hist(column=x,figsize=(10,12))
        
# hist_y1=df.hist(column=y1,figsize=(10,12))
# hist_y2=df.hist(column=y2,figsize=(10,12))



for i in y1+y2:
    fig,axs= plt.subplots(4,4)
    
    # print(df[i].isna().sum())
    
    for count,j in enumerate(x):
        df=df_b.loc[df_b[j]!=0]
        df=df_b.dropna(axis=0,subset=[i])
        print(df.shape,df[i].isna().sum())
        z = np.polyfit(df[j], df[i], 1)
        p = np.poly1d(z)
        
        if 'Time' in i:
            axs[0,0].set_title(i)
            axs[count // 4, count % 4].scatter(df[j],df[i],cmap='inferno',label=j)
            axs[count // 4, count % 4].plot(df[j],p(df[j]),label=j)
            axs[count // 4, count % 4].set_yscale('log')
            axs[count // 4, count % 4].set_xlabel(j)
            axs[count // 4, count % 4].legend()
        else:    
            axs[0,0].set_title(i)
            axs[count // 4, count % 4].scatter(df[j],df[i],cmap='inferno',label=j)
            axs[count // 4, count % 4].plot(df[j],p(df[j]),label=j)
            axs[count // 4, count % 4].set_xlabel(j)
            axs[count // 4, count % 4].legend()


#     plt.savefig(r'images/' + i+".png",dpi=600,bbox_inches='tight')
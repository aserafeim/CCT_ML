import json
import pandas as pd
import os

### Create class 

class unpack_json:
    
    def __init__(self,filename,path=None):
        self.filename=filename
        self.path=path
        
    def unpack(self):
        # filename='En 28_p101'
        if self.path:
            file=self.path + '\\' +self.filename
        else:
            file=self.filename
            
        with open(file+'.json','r') as f:
            data = json.loads(f.read())
            
### Define names of the variables and initialize dictionaries and lists
        
        kinetics={}
        comp={}
        names=[]
        element=[]
        boo={}
        time=[]
        temp=[]
        phase_name=[]
        
        process=['Austenitization Time:','Austenitization Temp:','Grain Size:']
        temperatures=['Ms:', 'Mf:', 'Ac1:', 'Ac3:']
        phases=['Ferrite','Pearlite','Bainite']
        status=['Status']

### Check if process and phases exist in the json file and adjust the list

        for i in phases:
            if i not in data.keys():
                phases.remove(i)
        
        for i in process:
            if i not in data.keys():
                process.remove(i)

### Store keys in list names and create dictionary with T-t information

        for i in phases:
            for j in data[i].keys():
                for k in data[i][j].keys():
                    names.append(i+'_'+j+'_'+k)
                    kinetics[i+'_'+j+'_'+k] = data[i][j][k]
                    boo[i+'_'+j]=[True for i in range(len(data[i][j][k]))]

### Create a list (elements) that comprises of all non-kinetics data
 
        for i in data.keys():
            if i not in temperatures+process+phases+status:
                element.append(i)

### Create dictionary of all non-kinetics data
        
        parameters=element+process+temperatures+status

        for i in data.keys():
            if i in parameters:
                    comp[i]=data[i]
            
### Create dataframe with comp data            
            
        df=pd.DataFrame(comp,index=['row 1'])

### Create T-t columns

        for i in phases:
            for j in data[i].keys():
                phase_name.append(i+'_'+j)
        
        for i in range(0,len(names),2):
            time+=kinetics[names[i]]
            temp+=kinetics[names[i+1]]        

### Store boolean kinetics columns in dataframe

        for i in range(0,len(phase_name),1):
             df2=pd.DataFrame(list(zip(boo[phase_name[i]])),columns=[phase_name[i]])
             df=pd.concat([df,df2],axis=0)
     
### Drop the first row     
     
        df = df.iloc[1: , :]

### Insert T-t columns into dataframe

        df.insert(df.columns.get_loc(phase_name[0]), 'Temperature', temp, allow_duplicates=True)
        df.insert(df.columns.get_loc(phase_name[0]), 'time', time, allow_duplicates=True)

### Fill nan values in non-kinetics columns with repeating values

        df=df.fillna(value=comp)   

### Replace boolean columns nan values with 0

        df[phase_name]=df[phase_name].fillna(value=0)
        
### Reset index numbering in dataframe

        df.reset_index(drop=True, inplace=True)
        
        return df

### Locate json files and create dataframes from all files in folder
        
path_to_json=r'C:\Users\kjeau\Desktop\Python\CCT_ML-main'

json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

df1=pd.DataFrame()

### Unpack json files and create one dataframe with all dataframes combined

for i in json_files:
    test=unpack_json(i[:-5],path_to_json)
    df=test.unpack()
    df1=pd.concat([df1,df],axis=0)
    
### Fill element column nan values with 0    

elements=['C','Mn','Si','P','S','Cr','Cu','Ni','V','Al','Ti','Mo','N','B','W','Nb','Sn','Co']
    
df1[elements]=df1[elements].fillna(value=0)

### Fill boolean column nan values to 0

phase_percent=['Ferrite_1','Ferrite_10','Ferrite_50','Ferrite_99',
'Pearlite_1','Pearlite_10','Pearlite_50','Pearlite_90','Pearlite_99',
'Bainite_1','Bainite_10','Bainite_40','Bainite_50','Bainite_85','Bainite_90','Bainite_95','Bainite_99']

df1[phase_percent]=df1[phase_percent].fillna(value=0)

### Rearrange columns

df1=df1[['C','Mn','Si','P','S','Cr','Cu','Ni','V','Al','Ti','Mo','N','B','W','Nb','Sn','Co',
         'Status','Grain Size:','Austenitization Temp:','Austenitization Time:',
         'Ms:','Mf:','Ac1:','Ac3:','Temperature','time',
         'Ferrite_1','Ferrite_10','Ferrite_50','Ferrite_99',
         'Pearlite_1','Pearlite_10','Pearlite_50','Pearlite_90','Pearlite_99',
         'Bainite_1','Bainite_10','Bainite_40','Bainite_50','Bainite_85','Bainite_90','Bainite_95','Bainite_99']]

### Save final dataframe to CSV file

df1.to_csv('BIG_DATA.csv')
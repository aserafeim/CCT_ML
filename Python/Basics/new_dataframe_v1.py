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
                
        parameters=element+process+temperatures+status

### Create dictionary of all non-kinetics data
 
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
 
### Convert dataframe to csv format       
 
        df.to_csv(self.filename+'.csv')
        
        return df
        
# path_to_json=r'C:\Users\kjeau\Desktop\Python\dataframe'
path_to_json=r'C:\Users\alexs\sciebo\CTT_TTT Images\Atlas_New\JSON files\German Steels - Atlas'

json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

for i in json_files:
    test=unpack_json(i[:-5],path_to_json)
    df=test.unpack()

### Create new dataframe with ms,mf,ac1,ac3
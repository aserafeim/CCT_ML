# -*- coding: utf-8 -*-
"""
Created on Mon May  9 22:38:17 2022

@author: alexs
"""
import pandas as pd
import json
import numpy as np

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
        crit_temp={}
        names=[]
        element=[]
        min_times={}
        
       
        process=['Austenitization Time:','Austenitization Temp:','Grain Size:']
        Temperatures=['Ms:', 'Mf:', 'Ac1:', 'Ac3:']
        phases=['Ferrite','Pearlite','Bainite']
        status=['Status']
        
        ####check if process and phases exist in the json file and adjust the list.
        
        for i in phases:
            if i not in data.keys():
                phases.remove(i)
        
        for i in process:
            if i not in data.keys():
                process.remove(i)
        
        ###Store keys in list names
        ### and create dictionary with T-t information
        for i in phases:
            for j in data[i].keys():
                for k in data[i][j].keys():
                    names.append(i+'_'+j+'_'+k)
                    kinetics[i+'_'+j+'_'+k] = data[i][j][k]
    
        ### Create a list (elements) that comprises of the elements and process 
        ### parameters
        for i in data.keys():
            if i not in Temperatures+process+phases+status:
                element.append(i)
        elements=element+process
        print(element,self.filename)
        ### create the composition and grain size/austenitization line of the
        ### dataframe
        for i in data.keys():
            if i in elements:
                    comp[i]=data[i]
        
        df=pd.DataFrame(comp,index=['row 1'])
        
        ###Loop over all Time temperature curves in the dictionary kinetics and concat them  
        for i in range(0,len(names),2):
            df1=pd.DataFrame(list(zip(kinetics[names[i]],kinetics[names[i+1]])),columns=[names[i],names[i+1]])
            df=pd.concat([df,df1],axis=0) 
        
        ### Fill Nan  values of the chemical composition and grain size with
        ### identical values and drop the first row
        df=df.fillna(value=comp)    
        # df.drop(['row 1'])
        df = df.iloc[1: , :]
        
        # df.to_csv(self.filename+'.csv')
        # df.to_excel(self.filename+'.xlsx') 
        
        
        
        ##Calculate minimum times (tip) for each phase
        for i in df.columns:
            if '_1_Time' in i:
                
                print(i, df[i].min())
                min_times[i]=df[i].min()
                
        ###Data frame with values of composition and Ms, Ac temperatures
        
        for i in data.keys():
            if i in elements +Temperatures:
                    crit_temp[i]=data[i]
        ### update crit_temp_dictionary to include the min times as well.
            
        crit_temp.update(min_times)
        df_b=pd.DataFrame(crit_temp,index=[self.filename])
        # df_b.to_csv(self.filename+'crit_temp'+'.csv')
        
        return df, df_b, data
    
    

# test=unpack_json('json file name')
# df_k,df_T,data=test.unpack()
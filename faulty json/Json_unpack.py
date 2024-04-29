# -*- coding: utf-8 -*-
"""
Created on Mon May  9 22:38:17 2022

@author: alexs

Class that uppacks TTTs from JSOn file into a dataframe. Input is the filename of the json
without the ending and the return is kinetic dataframe in default form, boolean kinetic, 
critical temperatures and the dictionary that contains the raw JSON file.
"""
import pandas as pd
import json
import numpy as np

class unpack_json:
    
    def __init__(self,filename=None,path=None):
        self.filename=filename
        self.path=path
        
    def unpack(self,boolean='False'):
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
        min_temp={}
        start_temp={}
        boo = {}
        phase_name = []
        time=[]
        Time=[]
        time1=[]
        Temperature=[]
        
       
        process=['Austenitization Time:','Austenitization Temp:','Grain Size:']
        self.process=process
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
                phase_name.append(i+'_'+j)
                for k in data[i][j].keys():
                    names.append(i+'_'+j+'_'+k)
                    kinetics[i+'_'+j+'_'+k] = data[i][j][k]
                    boo[i+'_'+j]=[True for i in range(len(data[i][j][k]))]
                    if k=='Time':
                        Time += data[i][j][k] 
                    else:
                        Temperature+= data[i][j][k]

    
        ### Create a list (elements) that comprises of the elements and process 
        ### parameters
        for i in data.keys():
            if i not in Temperatures+process+phases+status:
                element.append(i)
        self.elements=element+process
        print(element,self.filename)
        ### create the composition and grain size/austenitization line of the
        ### dataframe
        for i in data.keys():
            if i in self.elements:
                    comp[i]=data[i]
        
        df=pd.DataFrame(comp,index=['row 1'])
        df_b=pd.DataFrame(comp,index=['row 1'])
        # print(df_b.head)
        
        

        df_clean= pd.DataFrame(Time, columns=['Time'])
        df_clean["Temperature"] = Temperature
        
        
        ###Loop over all Time temperature curves in the dictionary kinetics and concat them  
        for i in range(0,len(names),2):
            df1=pd.DataFrame(list(zip(kinetics[names[i]],kinetics[names[i+1]])),columns=[names[i],names[i+1]])
            df=pd.concat([df,df1],axis=0) 
        
        
        ### Concat boolean and time temperature
        for i in range(0,len(phase_name),1):
            df2=pd.DataFrame(list(boo[phase_name[i]]),columns=[phase_name[i]])
            df_b=pd.concat([df_b,df2],axis=0)     
        
        ### Fill Nan  values of the chemical composition and grain size with
        ### identical values and drop the first row
        
        df=df.fillna(value=comp)   
        df_b=df_b.fillna(value=comp)
        
        ###Remove first row and then fill the Nan values in the boolean columns
        df = df.iloc[1: , :]
        df_b= df_b.iloc[1: , :]
        df_b=df_b.fillna(False)
        
        ### Insert Time and Temperature columns in the dataframe
        
        df_b.insert(df_b.columns.get_loc(element[-1])+ 1, 'Temperature', df_clean['Temperature'])
        df_b.insert(df_b.columns.get_loc(element[-1])+ 2, 'Time', df_clean['Time'])
        
        df=df.reset_index()
    
        ##Calculate minimum times (tip) for each phase
        for i in df.columns:
            if '_1_Time' in i:
                
                ## Get temperature index  !!!!! Only works if the data is paired 
                ## as Bainite_1_Time, Bainite_1_Temperature
                if i=='Bainite_1_Time':
                    j=df.columns[df.columns.get_loc('Bainite_1_Time')+1]
                    min_temp[j+'_at min'] = df[j][df[i].idxmin()]
                    start_temp['start_'+j] = df[j].max()
                print(i, df[i].min())
                min_times[i] = df[i].min()

                
        ###Data frame with values of composition and Ms, Ac temperatures
        
        for i in data.keys():
            if i in self.elements +Temperatures:
                    crit_temp[i]=data[i]
        ### update crit_temp_dictionary to include the min times as well.
            
        crit_temp.update(min_times)
        crit_temp.update(min_temp)
        crit_temp.update(start_temp)
        df_c=pd.DataFrame(crit_temp,index=[self.filename])
        
        
        return df,df_b, df_c, data
    
    def keep_relevant(self,df,elements,csv_inp=None):
        
        '''method to keep only the 1 % and 99 % of the data for the transformation
        returns a dataframe that has the other columns and corresponding rows removed'''
        
        relevant_columns=elements+self.process+['Time','Temperature']
        
        df=df.reset_index(drop=True)
        for i in df.columns:
            if ('_99' not in i) and not i.endswith('_1') and (i not in relevant_columns):
                ### Get the indexes of the rows that correspond the dropped column
                print(df[i])
                ind = df.loc[df[i]].index
                ### Drop the rows that contain TRUE for column i
                df = df.drop(ind,axis=0)
                ### Drop column i
                df = df.drop([i],axis = 1)
        return df        

# test=unpack_json('En 28_p101')
# df_k,df_b,df_T,data=test.unpack()

# df_b2=test.keep_relevant(df_b)
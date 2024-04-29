# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 15:05:46 2022

@author: aserafeim
"""

class find_tip:
    
    def __init__(self,df):
        self.df=df

        
    def search(self):
        
        for i in self.df.columns:
            if 'Bainite_1_Time' in i:
                print(self.df[i].min())
                #### replace with multiplication of Time vector with boolean values
    


        
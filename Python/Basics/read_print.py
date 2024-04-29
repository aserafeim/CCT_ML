# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 18:22:54 2022

@author: kjeau
"""

import json
import pandas as pd

f = open('46Mn7.json', 'r')
db = json.load(f)

df = pd.read_json('46Mn7.json')

print(('Ms'), ('='), db['Ms:'])
print(('Mf'), ('='), db['Mf:'])
print(('Ac1'), ('='), db['Ac1:'])
print(('Ac3'), ('='), db['Ac3:'])
print(('Aus Temp'), ('='), db['Austenitization Temp:'])

if ('Austenitization Time:') in db.keys():
    print(('Aus Time'), ('='), db['Austenitization Time:'])

if ('Grain Size:') in db.keys():
    print(('Grain Size'), ('='), db['Grain Size:'])

if ('C') in db.keys():
    print(('C%'), ('='), db['C'])
    
if ('Mn') in db.keys():
    print(('Mn%'), ('='), db['Mn'])
    
if ('Si') in db.keys():
    print(('Si%'), ('='), db['Si'])

if ('Cr') in db.keys():
    print(('Cr%'), ('='), db['Cr'])
    
if ('Ni') in db.keys():
    print(('Ni%'), ('='), db['Ni'])
    
if ('Mo') in db.keys():
    print(('Mo%'), ('='), db['Mo'])

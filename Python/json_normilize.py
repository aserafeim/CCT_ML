# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 21:19:11 2022

@author: alexs
"""
import pandas as pd
import numpy as np

l1=[x for x in range(0,10)]
l2=[x for x in range(10,15)]
data = [
    {
        "state": "Florida",
        "shortname": "FL",
        "info": {"governor": "Rick Scott"},
        "counties": [
            {"name": "Dade", "population": 12345},
            {"name": "Broward", "population": 40000},
            {"name": "Palm Beach", "population": 60000},
            {'l1': l1}
        ],
    },
    {
        "state": "Ohio",
        "shortname": "OH",
        "info": {"governor": "John Kasich"},
        "counties": [
            {"name": "Summit", "population": 1234},
            {"name": "Cuyahoga", "population": 1337},
            {'l1': l1}
        ],
    },
]

result = pd.json_normalize(data,['counties'])
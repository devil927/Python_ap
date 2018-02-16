# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 18:19:56 2018

@author: Tushar
"""
# importing the library

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# dataset

dataset=pd.read_csv('Data.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,3].values

# for missing values in data

from sklearn.preprocessing import Imputer
imp=Imputer(missing_values="NaN", strategy="mean", axis=0)
imp=imp.fit(x[:,1:3])
x[:,1:3]=imp.transform(x[:,1:3])

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 16:35:12 2021

@author: liujiale
"""

import numpy as np
import pandas as pd
from keras.models import load_model
from keras import backend as K
import joblib
from keras.utils import to_categorical
#import seaborn as sns
import matplotlib.pyplot as plt
import os
from sys import argv
import math

if len(argv)!=5:
    print('\n----------\n usage: python predictor.py file1 file2 file3 file4\n---------\n')

model=load_model('scripts/model.h5')

intrafeature1 = argv[1]
intrafeature2 = argv[2]
ccmpred = argv[3]
alnstat = argv[4]

data_1=pd.read_csv(intrafeature1,header=None,sep='\s+')
data_2=pd.read_csv(intrafeature2,header=None,sep='\s+')
data1=np.array(data_1.iloc[:,3:-3]).reshape([1,-1,37])
data2=np.array(data_2.iloc[:,3:-3]).reshape([1,-1,37])
test_x1=np.zeros((1,500,37))
test_x1[:,:data1.shape[1],:]=data1
test_x2=np.zeros((1,500,37))
test_x2[:,:data2.shape[1],:]=data2


ccmpred=np.loadtxt(ccmpred)
ccmpred=ccmpred[:data1.shape[1],data1.shape[1]:]
test_x3=np.zeros((1,500,500))
test_x3[:,:data1.shape[1],:data2.shape[1]]=ccmpred.reshape((1,data1.shape[1],data2.shape[1]))

test_x5=np.zeros((1,500,500,3))
alnstat=np.load(alnstat)
test_x5[0,:data1.shape[1],:data2.shape[1],:]=alnstat[:data1.shape[1],data1.shape[1]:]
data_r=np.tile(test_x1,[500,1])
data_c=np.tile(test_x2,[1,500]).reshape((1,-1,37))
test_x4=np.concatenate((data_c,data_r),axis=-1).reshape((1,500,500,37*2))
pred = model.predict([test_x1,test_x2,test_x3,test_x5,test_x4],batch_size=1 )



index=np.argsort(pred[:,:data1.shape[1],:data2.shape[1],:].reshape((-1,2))[:,-1],axis=-1)[::-1]
print(index[:50])

print('\nTop 50 residue pairs:\n')
for order in index[:50]:
    i= math.floor((order+1)/data2.shape[1])
    j=(order+1)%data2.shape[1]
    print(data_1.iloc[i-1,:3].values,data_2.iloc[j-1,:3].values)

    
'''
print(pred[:,:data1.shape[1],:data2.shape[1],:].reshape((-1,2))[:,-1][index[:50]])
top_index=test_y[:,:data1.shape[1],:data2.shape[1],:].reshape((-1,2))[:,-1][index[:50]]
print(top_index)
'''

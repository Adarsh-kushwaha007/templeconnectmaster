# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:21:25 2024

@author: 91892
"""
from scipy.misc import imread
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

sInputFileNmae = 'https://github.com/Apress/practical-data-science/blob/b56ad14b578e9f5c1e183c2890833efbadf3aa76/VKHCG/05-DS/9999-Data/Angus.jpg'
InputData=imread(sInputFileNmae,flatten=False,mode='RGBA')

print('Input data values ====================================')
print('X:',InputData.shape[0])
print('Y:',InputData.shape[1])
print('RGB:',InputData.shape[2])
print('======================================================')
ProcessRawData=InputData.flatten()
y=InputData.shape[2] + 2
x=int(ProcessRawData.shape[0]/y)
ProcessData=pd.DataFrame(np.reshape(ProcessRawData, (x, y)))
sColumns= ['XAxis','YAxis','Red', 'Green', 'Blue','Alpha']
ProcessData.columns=sColumns
ProcessData.index.names =['ID']
print('Rows: ',ProcessData.shape[0])
print('Columns :',ProcessData.shape[1])
print('=====================================================')
print('Process Data Values =================================')
print('=====================================================')
plt.imshow(InputData)
plt.show()
print('=====================================================')
# Output Agreement ===========================================
OutputData=ProcessData
print('Storing File')
sOutputFileName='C:/VKHCG/05-DS/9999-Data/HORUS-Picture.csv'
OutputData.to_csv(sOutputFileName, index = False)
print('=====================================================')
print('Picture to HORUS - Done')
print('=====================================================')
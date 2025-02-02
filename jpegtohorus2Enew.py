# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:09:08 2024

@author: 91892
"""

import imageio
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests
from io import BytesIO

# Download the image from the web (use the raw image URL)
sInputFileName = 'https://raw.githubusercontent.com/Apress/practical-data-science/master/VKHCG/05-DS/9999-Data/Angus.jpg'
response = requests.get(sInputFileName)
img_data = BytesIO(response.content)

# Read the image using imageio
InputData = imageio.imread(img_data)

# Display the image information
print('Input Data Values ============================================')
print('X: ', InputData.shape[0])
print('Y: ', InputData.shape[1])

# Check number of channels (3 = RGB, 4 = RGBA)
num_channels = InputData.shape[2]
print(f'Number of Channels (RGB or RGBA): {num_channels}')
print('==============================================================')

# Flatten the image data
ProcessRawData = InputData.reshape(-1, num_channels)

# Create X Axis and Y Axis columns
x_axis = np.repeat(np.arange(InputData.shape[0]), InputData.shape[1])
y_axis = np.tile(np.arange(InputData.shape[1]), InputData.shape[0])

# Handle RGB and RGBA images
if num_channels == 3:
    # RGB Image
    ProcessData = pd.DataFrame({
        'X Axis': x_axis,
        'Y Axis': y_axis,
        'Red': ProcessRawData[:, 0],
        'Green': ProcessRawData[:, 1],
        'Blue': ProcessRawData[:, 2]
    })
elif num_channels == 4:
    # RGBA Image
    ProcessData = pd.DataFrame({
        'X Axis': x_axis,
        'Y Axis': y_axis,
        'Red': ProcessRawData[:, 0],
        'Green': ProcessRawData[:, 1],
        'Blue': ProcessRawData[:, 2],
        'Alpha': ProcessRawData[:, 3]
    })

# Display the processed data
print('Rows: ', ProcessData.shape[0])
print('Columns: ', ProcessData.shape[1])
print('==============================================================')
print('Process Data Values ==========================================')
print('==============================================================')

# Show the image using matplotlib
plt.imshow(InputData)
plt.show()

# Save the processed data to a CSV file locally
sOutputFileName = 'HORUS-Picture.csv'
OutputData = ProcessData
print('Storing File')
OutputData.to_csv(sOutputFileName, index=False)
print('==============================================================')
print('Picture to HORUS - Done')
print('==============================================================')
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 14:39:31 2022

@author: dell
"""

import numpy as np
import pickle

loaded_model = pickle.load(open(r'C:\Users\pc\OneDrive\Desktop\diabetes_prediction\trained_model.sav', 'rb'))
input_data=(5,116,74,0,0,25.6,0.201,30)
input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
prediction=loaded_model.predict(input_data_reshaped)
print(prediction)
if prediction[0]==0:
  print("the user is not diabetic")
else:
  print("the user is diabetic")
##this is main.py file
# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main

print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))

# Run unit tests automatically
main(module='test_module', exit=False)




## this is the function file


import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError('List must contain nine numbers.')
  else:
    arr = np.array(list)
    arr = arr.reshape(3,3)
    calculations = {
      'mean':[np.mean(arr,0).tolist(),np.mean(arr,1).tolist(), np.mean(arr).tolist()],
      'variance':[np.var(arr,0).tolist(), np.var(arr,1).tolist(), np.var(arr).tolist()],
      'standard deviation':[np.std(arr,0).tolist(), np.std(arr,1).tolist(), np.std(arr).tolist()],
      'max': [np.max(arr,0).tolist(), np.max(arr,1).tolist(), np.max(arr).tolist()],
      'min': [np.min(arr,0).tolist(), np.min(arr,1).tolist(), np.min(arr).tolist()],
      'sum': [np.sum(arr,0).tolist(), np.sum(arr,1).tolist(), np.sum(arr).tolist()]
    }
    
    return calculations

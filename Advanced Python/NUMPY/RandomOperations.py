import numpy as np

np.random.seed()
arr = np.random.randint(1,500,30).reshape(6,5)
print(arr)
print(arr[2:,2:])
print(arr[3:5,2:4])

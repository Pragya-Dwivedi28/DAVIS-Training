#where() --> to find indices where elements are greater than 3

import numpy as np

arr = np.array([1,2,3,4,5])
#find indices where elements are greater than 3
indices = np.where(arr>3)
print(indices)

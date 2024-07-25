#seed() -->to generate the same random numbers in a given range for everyone

import numpy as np
np.random.seed(125)
arr =  np.random.randint(1,100,12)
print(arr)

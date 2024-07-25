#to print the random number between a range

import numpy as np

rand = np.random.randint(0,10,2)  # 2 integer numbers from range 0-10
print(rand)

rand1 = np.random.rand(4)    #1-D array having numbers from range 0-1
print(rand1)

rand2 = np.random.rand(2,3)   #array of 2 rows and 3 columns having numbers from range 0-1
print(rand2)

rand3 = np.random.randint(0,100,10)    # 10 integer numbers from range 0-100
print(rand3)

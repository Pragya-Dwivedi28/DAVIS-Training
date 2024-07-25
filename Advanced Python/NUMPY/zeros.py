import numpy as np

#numpy.zeros() without dtype and order
a = np.zeros(6)
print(a)

#numpy.zeros() without order
a = np.zeros((6,), dtype=int)
print(a)

#numpy.zeros() with shape
a= np.zeros((6,2))
print(a)

#numpy.zeros() with the shape
a= np.zeros((6,2)) *10
print(a)

import numpy as np

#ones in the diagonal of an array [numpy.eye()]

arr6 = np.eye(3)   #for 2-D array having 3 rows and 3 columns
print(arr6)

arr7= np.eye(3,4)  #for 2-D array having 3 rows and 4 columns
print(arr7)


#diag() --> to insert different elemets diagonally

arr8 = np.diag((3,4,1,6))
print(arr8)
print(arr8.ndim)
print(arr8.shape)

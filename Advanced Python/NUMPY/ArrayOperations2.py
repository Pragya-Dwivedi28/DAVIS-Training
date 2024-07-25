#perform mathematical functions on array

import numpy as n

n.random.seed(122)
mat = n.random.randint(1,21,9).reshape(3,3)
print(mat)
print("The sum of whole array is :",n.sum(mat))
print("The commulative sum of whole array is :",n.cumsum(mat))
print("The minimum in whole array is :",n.min(mat))
print("The maximum in whole array is :",n.max(mat))
print("-----------------------")
print("The sum of 1st row, 2nd row & 3rd row of array :",n.sum(mat,axis=1))        #1--> to perform row-wise operations
print("The row-wise minimum in the whole array :",n.min(mat,axis=1))
print("The row-wise maximum in the whole array :",n.max(mat,axis=1))
print("The row-wise commulative sum of the whole array :",n.cumsum(mat,axis=1))

print("-----------------------")
print("The sum of 1st column, 2nd column & 3rd column of array :",n.sum(mat,axis=0))       #0--> to perform column-wise operations
print("The row-wise minimum in the whole array :",n.min(mat,axis=0))
print("The row-wise maximum in the whole array :",n.max(mat,axis=0))
print("The column-wise commulative sum of the whole array :",n.cumsum(mat,axis=0))

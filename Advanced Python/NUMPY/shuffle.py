#shuffle() --> to shuffle the elements of existing array

import numpy as n
n.random.seed(122)
mat = n.random.randint(1,21,10)
print(mat)
n.random.shuffle(mat)
print("After shuffling thhe array is :",mat)
print("The unique values, their index and count in the array :",n.unique(mat,return_index=True, return_counts=True))
print("Total number of unique values are :",n.unique(mat).size)

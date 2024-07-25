#arange() -->to generate a sequence of numbers from a given range

import numpy as np

arr = np.arange(1,15)
print(arr)

print("Even numbers in the given range :",arr[arr%2==0])

print("Odd numbers in the given range :",arr[arr%2==1])

print("Odd numbers in the given range :",arr[arr%2!=0])
print("Numbers which are greater than 8 in the range :",arr[arr>8])

arr[arr%2==0]=0  #replacing even numbers with zero
print(arr)

arr1 = np.arange(1,8)
print("New array :",arr1)
print(arr1+2)
print(arr1*2)
print(arr1**2)

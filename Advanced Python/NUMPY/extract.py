# extract() --> to extract elements from an array

import numpy as np

arr = np.array([1,2,3,4,5,6])

extracted_elements = np.extract(arr>3,arr)

print("The elements greater thean than 3 :", extracted_elements)

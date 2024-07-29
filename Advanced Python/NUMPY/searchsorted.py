# searchsorted() --> to find indices at which elements should be inserted to maintain the array's sorted order

import numpy as np

sorted_array = np.array([1,3,5,7,9])

index = np.searchsorted(sorted_array,6)
print("Index to insert 6:", index)

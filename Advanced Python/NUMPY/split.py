#split() -->to split the array into equal-sized array

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
# Split the array into 3 equal-sized sub-arrays
sub_arrays = np.split(arr, 3)
# Print the sub-arrays
for sub_arr in sub_arrays:
  print(sub_arr)

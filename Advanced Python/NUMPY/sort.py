#sort() --> used to sort the elements of an array

import numpy as np
arr = np.array([3, 1, 2, 4, 5])
# Sort the array in ascending order (creates a new sorted array)
sorted_arr = np.sort(arr)
# Print the sorted array
print("Sorted array (ascending):", sorted_arr)
# Sort the array in descending order
sorted_arr_desc = np.sort(arr)[::-1]
# Print the sorted array in descending order
print("Sorted array (descending):", sorted_arr_desc)


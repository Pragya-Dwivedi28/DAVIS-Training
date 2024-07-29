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

#sorting in 2D-Array

matrix = np.array([[3, 1, 2],[6, 5, 5]])
# Sort the array in ascending order (creates a new sorted array)
sorted_matrix = np.sort(matrix, axis=1)
# Print the sorted array
print("Sorted matrix (ascending along rows):", sorted_matrix)

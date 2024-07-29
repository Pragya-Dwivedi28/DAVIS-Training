#save() & load() -->for Saving and Loading NumPy Arrays

import numpy as np

scores = np.array([85,92,78,88,95,72,89])

np.save('student_scores.npy', scores)

loaded_scores = np.load('student_scores.npy')

print("Original scores :", scores)
print("Loaded scores :", loaded_scores)

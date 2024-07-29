#percentile() -->in numpy

import numpy as np
# Test scores of 30 students
test_scores = np.array([65, 75, 80, 85, 90, 92, 94, 95, 96, 98, 100, 102, 104, 106, 108,
110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138])
q1 = np.percentile(test_scores, 25)
print("Lower Quartile (25th Percentile):", q1)

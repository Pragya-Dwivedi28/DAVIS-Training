#std() --> to calculate the standard deviation
#var() --> to calculate the variance

import numpy as np

# Calculate the Mean First, you calculate the mean (average) scores for each class.
# Score of Class A students
classA= np.array([85, 88, 90, 92, 95])
# Score of Class A students
classB= np.array([70, 80, 85, 95, 100])
classA_mean=np.mean(classA)
classB_mean=np.mean(classB)
print('Class A Score Average',classA_mean )
print('Class B Score Average',classB_mean )

# now u calculate the standard deviation for each class to understand the spread or consistency of the scores.
classA_std=np.std(classA)
classB_std=np.std(classB)
print('Class A Standard Deviation',classA_std )
print('Class B Standard Deviation',classB_std )

#Variance is a statistical measure that quantifies how data points in a dataset are spread out or dispersed from the mean (average).

classA_var = np.var(classA)
classB_var = np.var(classB)
print('Class A Variance',classA_var)
print('Class B Variance',classB_var)

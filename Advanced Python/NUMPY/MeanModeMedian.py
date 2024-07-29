# mean() --> to calculates the average value of an array
# mode() --> to calculates the mode value of an array
# median() --> tp find the median value (middle value when sorted) of an array.


import numpy as np
temperatures = np.array([72, 68, 74, 80, 79, 82, 75])
average_temperature = np.mean(temperatures)
print("Mean of the temperature :",average_temperature)

from scipy import stats as stats
temperature1 = np.array([72, 68, 74, 80, 79, 82, 75,72])
print(stats.mode(temperature1))

incomes = np.array([45000, 55000, 60000, 65000, 70000, 80000, 90000])
median_income = np.median(incomes)
print("Median of the temperature :", median_income)

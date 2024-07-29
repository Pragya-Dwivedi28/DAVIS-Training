#filtering of an array

import numpy as np
# Temperature readings (in Celsius)
temperatures = np.array([20.5, 22.0, 19.8, 23.5, 18.0, 24.2, 26.1])
# Filter temperatures within the range of 20°C to 25°C
filtered_temperatures = temperatures[(temperatures >= 20) & (temperatures <= 25)]
print("Filtered Temperatures:")
print(filtered_temperatures)

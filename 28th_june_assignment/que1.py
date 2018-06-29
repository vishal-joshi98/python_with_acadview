# QUESTION 1
import numpy as np

ran_array = np.random.rand(10, 1)      # generating array of random no and shape is 10,1
print(ran_array)

array_mean = np.mean(ran_array, dtype = np.float64)  # calculating mean of random element array
print("\n\n\t MEAN : ",array_mean)
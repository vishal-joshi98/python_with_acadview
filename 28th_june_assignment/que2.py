# QUESTION 2
import numpy as np

ran_arr = np.random.rand(20, 1)  # creating array of shape 20,1 of random number
print(ran_arr)

stand_devi = np.std(ran_arr, dtype = np.float64)   # CALCULATING STANDARD DEVIATION

print("\n\t STANDARD DEVIATION = ", stand_devi)

varienc = np.var(ran_arr, dtype = np.float64)    # calculating varience
print("\n\t VARIENCE  = ",varienc)



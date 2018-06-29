# QUESTION 4:
import numpy as np
import math
def fun_app(k):
    """
    THIS FUNCTION APPLY A FUNCTION F(X) = 1/ (1+exp(-X)) ON EACH ELEMENT OF ARRAY
    :param k:ARRAY OF SHAPE OF( 10 ,1)
    :return:
    """
    return  1 / (1 + np.exp(-k))      # appliying on each element and returning value


a = np.random.randint(low=1, high=100, size = (10, 1))    # CREATING RANDOM NO ARRAY WHOSE SHAPE IS (10,1)

print(a)

print("\nSHAPE OF ARRAY : ", np.shape(a))     # SHAPE = (10,1)

a = fun_app(a)
print("\n\t AFTER APPLIYING FUNCTION ON EACH ELEMENT OF ARRAY \n ARRAY : ", a)


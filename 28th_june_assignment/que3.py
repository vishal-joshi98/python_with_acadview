# QUESTION 3
import numpy as np

A = np.random.rand(10, 20)

B = np.random.rand(20, 25)

C = np.dot(A , B)  # MULTIPLY TWO MATRIX AND

print("\n\t\t NEW MATRIX (A X B) :", C)  # PRINTING MULTIPLICATION OF MATRIX A AND B

print("\n\t SHAPE OF TWO MATRIX : ", np.shape(C))   # PRITNIG SHAPE OF NEW MATRIX WHICH IS 10 25

print("\n\t SUM OF ALL ELEMENT OF NEW MATRIX  : ", np.sum(C))





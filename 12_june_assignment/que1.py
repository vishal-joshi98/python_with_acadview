# QUESTION 1: FUNCTION FOR CALCULATION AREA OF CIRCLE
import math


def area(radious):  # FUNCTION FOR CALCULATION AREA OF CIRCLE
    ar = (math.pi) * (radious**2)
    print("ARE OF CIRCLE :" , ar)

r = float(input(" ENTER THE RADIOUS OF CIRCLE"))
area(r)
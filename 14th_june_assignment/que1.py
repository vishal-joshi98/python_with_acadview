import math  # IMPORTING MATH PACKAGE FOR PI
# QUESTION 1:   CIRCLE CLASS AND TWO METHOD
class circle:
    def __init__(self,radious):  #intializing radious
        self.r = radious
    def getarea(self):         # calculating area of circle
        area = (math.pi)*pow(self.r, 2)
        print("\n  AREA OF CIRCLE :", area)
    def getCircumference(self):  # CALCULATING CIRCUMFERENCE OF CIRCLE
        cir = 2 * (math.pi) * self.r
        print(" \n CIRCUMFERENCE OF  CIRCLE :", cir)
c = circle(float(input("\n ENTER THE RADIOUS OF CIRCLE")))
c.getarea()
c.getCircumference()
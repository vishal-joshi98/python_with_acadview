# QUESTION 4: CREATING SHAPE CLASS AND INHERIT AND OVERRIDE ITS METHOD AREA IN DIFFERENT CLASS
import math   #IMPORTING MATH PACKAGE FOR CALCULATING SQUARE
class Shape:
    def __init__(self, length, breadth):
        self.shape_length = length
        self.shap_breadth = breadth
    def area(self):
        print("THIS METHOD OVERRIDE IN ITSE CHILD CLASSES")

class Reactangle(Shape):
    def area(self):
        """
        AREA METHID TO CALCULATE AREA OF RECTANGLE AND IT IS OVERRIDE THE METHOD OF SHAPE CLASS
        :return:
        """
        area_rectangle = self.shape_length * self.shap_breadth
        print("\n AREA OF RECTANGLE = ", area_rectangle)

class Square(Shape):
    def area(self):
        """
        OVERRIDEN AREA METHOD FOR CALCULATE AREA OF SQUARE
        :return:
        """
        area_Square = math.pow(self.shape_length, 2)
        print(" AREA OF SQUARE = ", area_Square)

length = float(input("ENTER THE LENGTH OF SHAPE : "))
breadth = float(input("ENTER THE BREADTH OF SHAPE : "))
rectangle1 = Reactangle(length, breadth)
square1 = Square(length, breadth)
rectangle1.area()
square1.area()
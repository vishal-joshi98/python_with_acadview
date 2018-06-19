# QUESTION 1:  INHERITANCE
class Animal:
    """
    THIS IS BASE CLASS
    """
    def animal_attribute(self):
        """
        THIS IS BASE CLASS METHOD
        """
        print("\n THIS IS BASE CLASS ANIMAL METHOD")

class Tiger(Animal):
    """
    THIS IS CHILD CLASS OF ANIMAL CLASS
    """

base_obj = Tiger()   #CREATING OBJECT OF CHILD CLASS TIGER
base_obj.animal_attribute()    # ACCESSING   BASE CLASS METHOD THROUGH CHILD CLASSS

# QUESTION 4: CALLING FACTORIAL FUNCTION USING THREAD
import threading
import math   # IMPORT MATH PACKAGE  FOR CALCULATING FACTORIAL

class Thread(threading.Thread):
    """
    Thread calling factorial function
    """
    def __init__(self, No):
        threading.Thread.__init__(self)
        self.No = No
    def run(self):
        factorial(self.No)    # calling factorial

def factorial(No):
    fact = math.factorial(No)
    print("FACTORIAL OF %d = %d" %(No, fact))

f_no = int(input("\n ENTER THE NO WHOSE YOU WANT TO CALCULATE FACTORIAL"))

# CREATING NEW THREAD
thread1 = Thread(f_no)
# START NEW THREAD
thread1.start()


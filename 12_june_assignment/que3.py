#QUESTION 3: MULTIPLICATION TABLE OF 12
def table(no):  #FUNCTION FOR CALCULATION TABLE OF 12
    if no <= 10:
        print("12 x " , no , " = " , 12 * no)
        table(no+1)   # RECURSION
    else:
        return 0
print("\n MULTIPLICATION TABLE OF 12 :\n")
table(1)
# QUESTION 4 : POWER OF A NUMBER
def power(a, b):  #RECURSION FUNCTION FOR CALCULATION POWER OF A RAISED B
    if b == 0:
        return 1
    elif b >= 2:
        return a * power(a, b-1)  # POWER FUNCTION CALLING ITSELF
    else:
        return a
print("ENTER THE VALE OF A AND B WHERE A AND B ARE \n A^B\n")
a1 = int(input("ENTER A: "))
b1 = int(input("\n ENTER B :"))
p = power(a1, b1)
print("\n\nPOWER OF", a1, " RAISED TO", b1, "(A^B)   :  ", p)





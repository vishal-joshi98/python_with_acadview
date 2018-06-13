# QUESTION 3: LIST INPUT AND SQUARE OF THOSE INPUT
def square(li):
    lis2 = []
    for i in li:
        lis2.append(int(i)**2)
    print("\n SQUARE OF PREVIOUS LIST :\n" , lis2)
lis = input("ENTER THE ELEMENT OF LIST:\n").strip().split()
square(lis)
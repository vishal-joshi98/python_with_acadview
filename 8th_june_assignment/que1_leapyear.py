# que 1: leap year
def leap(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                print("leap year")
            else:
                print("not")
        else:
            print("leap year")
    else:
        print("not")

y1 = int(input("enter the year\n"))
leap(y1)

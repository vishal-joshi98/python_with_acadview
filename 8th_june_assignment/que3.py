# que 3: oldest and youngest
def det(age1,age2,age3):
    print(age1,age2,age3)
    print("\n")
    if age1 > age2 and age1 > age3:
        if age2 < age3:
            print("FIRST PERSON IS OLDEST  AND SECOND PERSON IS YOUNGEST")
        else:
            print("FIRST PERSON IS OLDEST  AND THIRD PERSON IS YOUNGEST")
    elif age2 > age1 and age2 > age3:
        if age1 < age3:
            print("\n SECOND PERSON IS OLDEST AND FIRST PERSON IS YOUNGEST")
        else:
            print(" SECOND PERSON IS OLDEST  AND THIRD PERSON IS YOUNGEST")
    else:
        if age1 < age2:
            print("\n THIRD PERSON IS OLDEST AND FIRST PERSON IS YOUNGEST")
        else:
            print("THIRD PERSON IS OLDEST  AND SECOND PERSON IS YOUNGEST")


a1, a2, a3 = input("ENTER THE AGE OF THREE PERSON\n").strip().split(" ")
det(int(a1) , int(a2) , int(a3))
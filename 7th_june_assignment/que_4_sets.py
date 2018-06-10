#sets question 1:
def operation(set1,set2):
    # PRINTING THE ELEMENT OF SETS
    print("\n\n FIRST SET ELEMENT:  ",set1)
    print("\n\nSECOND SET VALUE:   ",set2)

    # DIFFERENCE OF TWO SETS SET1-SET2
    if set1>set2:
        print("\n\nDIFFERENCE OF TWO SETS :    ",set1-set2)
    else:
        print("\n\nDIFFERENCE OF TWO SETS :    ",set2-set1)

    #COMPARING TWO SETS
    if set1>set2:
        print("\n\nSET 2 IS SUBSET OF SET 1")
    else:
        print(" \n\nSET 1 IS  SUBSET OF SET 2")

    #   INTERSECTION OF TWO SETS
    print("\n\nINTERSECTION OF TWO SETS :    ", set1 & set2)

set1=set(input("ENTER THE VALUE OF FIRST SET 1:   ").strip().split(" "))
set2=set(input("\nENTER THE VALUE OF SECOND SET2 :   ").strip().split(" "))
operation(set1,set2)

# QUESTION 8: USER LIST AND DELETE SPECIFIC ELEMENT
def delete(lis,element):
    c = lis.count(element)
    for i in range(c):
        lis.remove(element)

    print(" AFTER DELETING SPECIFIC ELEMENT IN LIST \n REMAINING LIST :",lis)

lis1=input("\n ENTER THE LIST ").strip().split()
element1 = input("ENTER ELEMENT WHICH YOU WANT TO DELETE FROM LIST")
delete(lis1 , element1)


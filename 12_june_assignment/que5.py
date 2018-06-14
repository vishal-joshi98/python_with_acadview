# QUESTION 5 :FACTORAIL NO
def fact(no):
    if no == 0 or no == 1:
        return 1
    else:
        return no * fact(no - 1)

n = int(input("ENTER NO FOR WHICH YOU WANT TO FIIND FACTORIAL : "))
if n < 0:
    print("\n NO SHOULD BE POSITIVE ")
    exit()
else:
    f = fact(n)
print("FACTORIAL OF ", n, " =", f)
dic = {}
dic[n] = f
print(dic)
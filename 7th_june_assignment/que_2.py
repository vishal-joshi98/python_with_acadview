# que2: largest and smallest in tuple
def element(tup):
    largest=max(tup)
    smallest=min(tup)
    print("largest element in tuple :  ",largest)
    print("smallest element in tuple:  ",smallest)

tup=tuple(input("enter tuple  : ").strip().split(" "))
element(tup)

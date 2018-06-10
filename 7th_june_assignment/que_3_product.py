# que 3: product of tuple element
def product(tup):
    pro=1
    for i in tup:
        pro=pro*int(i)

    print("product of tuple: ",pro)

tup=tuple(input("enter the tuple").strip().split(" "))
product(tup)

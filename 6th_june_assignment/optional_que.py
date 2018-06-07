#question 1 optional : count even and odd number
def counting(lis):
    od=[]
    ev=[]
    for i in lis:
        if  int(i)%2==0:
            ev.append(i)
        else:
            od.append(i)
    print("odd are: ",od)
    print("Even are: ",ev)

lis=input("enter list of integers\n").strip().split(" ")
print (lis)
counting(lis)

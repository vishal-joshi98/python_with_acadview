#question 3: counting object in list
def counting(lis):
      dic={}
      for i in lis:
            dic[i]=0
      for k in lis:
            if k in lis:
                  dic[k]=dic[k]+1
      print(dic)
           


lis=list(input("enter the object of list"))
counting(lis)

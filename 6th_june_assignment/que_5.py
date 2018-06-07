#question 5 : merging two list
def merging(l1,l2):
      l3=l1+l2
      l3.sort()
      print("after merging in one array and sort:",l3)

l1=list(input("enter the first array element"))
l2=list(input("enter the second array element "))
merging(l1,l2)

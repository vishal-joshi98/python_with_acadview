# question 5: dictionary
def dictionary(dic):
    while len(dic)<11:
        name=input("\nENTER THE NAME OF  STUDENT")
        dic[name]=int(input("\nENETR THE MARKS"))
    print(" NAME AND MARKS OF STUDENT WHERE\n\n KEY = NAME OF STUDENT  ADN VALUE= MARKS:\n",dic)

dic={}
dictionary(dic)

#question 7: word count
def counting(str):
    dic={}
    for i in str:
        dic[i]=str.count(i)
    print("  DICTIONARY :\n",dic)

str="MISSISSIPPI"
counting(str)

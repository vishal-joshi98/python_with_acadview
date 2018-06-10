#que 6: SORT DICTIONARY
def dic_sort(dic):
    while len(dic)<11:
        name=input("\nENTER THE NAME OF  STUDENT")
        dic[name]=int(input("\nENETR THE MARKS"))
    print(" BEFORE SORTING  DICTIONARY :\n",dic)
    sort_dict=sorted(dic.items(),key=lambda t:t[1])
    print("\n AFTER SORTING DICTIONARY :\n",dict(sort_dict))

dic={}
dic_sort(dic)

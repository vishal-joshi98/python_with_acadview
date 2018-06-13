# QUESTION 7: KEYS CORRESPONDING TO THE VALUES
def key_value(dic):
    for i1 , j in dic.items():  # FOR LOOP FOR PRINTING KEYS CORRESPONDING TO VALUES
        print(i1 , "->" , j)

c = int(input(" ENTER THE TOTAL LENGTH OF DICTIONARY "))  # INPUT FROM USER FOR LENGTH OF DICTIONARY
dic1 = {}
for i in range(c):
    data = input("ENTER THE KEY AND VALUE").strip().split(' ')
    dic1[data[0]] = data[1]
print("\n NOW YOUR DICTIONARY IS : " , dic1)
key_value(dic1)


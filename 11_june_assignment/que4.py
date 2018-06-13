# QUESTION 4: SEPARATE DIFFERENT DATA TYPE IN DIFFERENT LIST
def separate(lis):
    integer_list = []
    float_list = []
    string_list = []
    for i in lis:
        if type(i) == int:
            integer_list.append(i)
        elif type(i) == str:
            string_list.append(i)
        else:
            float_list.append(i)
    print("\nLIST OF INTEGER  : ", integer_list)
    print("\nLIST OF STRING   : ", string_list)
    print("\nLIST OF FLOAT    : ", float_list)

lis1 = [1,2,3,"vishal","joshi",9.8,8.5]
separate(lis1)
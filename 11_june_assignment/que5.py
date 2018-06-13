# QUESTION 5: LIST OF EVEN AND ODD NO
even = []
odd = []
for i in range(1,101):
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(" LIST OF EVEN NO  : " , even)
print(" LIST OF ODD NO  : " , odd)
eve_odd_list = even + odd
print(" \n LIST OF EVEN AND ODD NO\n", eve_odd_list)

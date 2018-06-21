# QUESTION 1: EXCEPTION
a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print(" ERROR  NAME :  ZeroDivisonError  :- DIVISION BY ZERO")
# QUESTION 2 : PERFECT NO
def perfect(n):  #FUNCTION FOR CALCULATING PERFECT NUMBER
    sum = 0
    for j in range(1 , n):
        if n % j == 0:
            sum += j
    if sum == n:
        print(n)
print("\n PERFECT NUMBERS  BETWEEN 1 TO 1000 ARE:\n")
for i in range(1  , 1000):
    perfect(i)    #PASSING NUMBER AS ARGUMENT TO FUNCTION



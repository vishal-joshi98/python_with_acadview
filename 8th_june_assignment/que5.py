#question 6: discount on purchase
def dis(cost):
    discount = 0.10 * cost
    if cost > 1000:
        price = cost - discount
        print("\n AFTER DISCOUNT TOTAL COST =\n", price)
    else:
        print(" \n NO DISCOUNT IF PURCHASE IS LESS THAN 1000")

unit = int(input("ENTER THE UNIT \n"))
# 1 UNIT=100
cost1 = unit * 100
print("\n   TOTAL PRICE = ",cost1)
dis(cost1)
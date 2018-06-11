def prize(points):
    if points >= 1 and points <= 50:
        print("  SORRY ! NO PRIZE THIS TIME")
    elif points >= 51 and  points <= 150:
        print(" CONGRATULATION ! YOU WON A WOODEN DOG")
    elif points >= 151 and points <=180:
        print("CONGRATULATION ! YOU WON A BOOK");
    else:
        print("CONGRATULATION ! YOU WON A CHOCOLATE")

p=int(input(" ENTER THE POINTS"))
if p>=0 and p<=200:
    prize(p)
else:
    print("\n POINTS SHOULD BE POSITIVE AND LESS THAN OR EQUAL TO 200")
# GCD USING MATH PACKAGE
import math   # importing math package for gcd
def gcd1(var1,var2):  # FUNCTION FOR CALCULATING GCD OF NUMBER
    gc = math.gcd(var1, var2)    # MATH FUNCTION FOR GCD
    print(" GCD OF ", var1, var2, "= ", gc)

a = int(input("\n ENTER FIRST NUMBER "))
b = int(input("\n ENTER SECOND NUMBER"))
gcd1(a, b)    # FUNCTION gcd1 CALLING
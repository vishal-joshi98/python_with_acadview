import sys
# try block for import error
try:
    import exception as exc
except Exception as e:
    print("ImportError:",e)


lis= [1,2]  # List to show index error
#INDEX ERROR
try:
    print(lis[3])   # IndexError
except IndexError:
    print("\nHere  IndexError is Handeled")

# VALUE ERRROR
try:
    print(int('vishal'))     # valueError
except ValueError:
    print(" \n HERE ValuError IS HANDELED")
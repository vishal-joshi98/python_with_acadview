# input 10 integer and print on screen
def display(integers):
    i = 0
    while i < len(integers):
        print(integers[i])
        i += 1
inputs = input("ENTER THE 10 INTEGERS :\n").strip().split()
no = list(map(int  , inputs))
display(no)
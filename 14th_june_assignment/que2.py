# QUESTION 2: STUDENT CLASS AND THEIR DETAILS
class student:
    def __init__(self, name, roll):
        self.n = name
        self.r = roll
    def display(self):
        print("\t", self.n, " \t\t", self.r)
       # print("\n  ROLL NO OF STUDENT: ", self.r)

s = int(input("\n ENTER THE TOTAL NO OF STUDENT"))
obj = [ ]
for i in range(s):
    obj.append(i)

for i in range(s):
    name = input("\n ENTER THE NAME OF STUDENT :")
    roll = int(input("\n ENTER THE ROLL NO OF STUDENT"))
    obj[i] = student(name, roll)
print(" \n DETAILS OF STUDENT :\n")
print("\n     NAME        ROLL NO")
for i in range(s):
    obj[i].display()

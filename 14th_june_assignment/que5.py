#QUESTION 5: EXPENDITURE AND SAVING
class expenditure:
    def __init__(self, expen, sav):
        self.exp = expen
        self.sa = sav
    def display(self):
        print("\n EXPENDITURE : ", self.exp)
        print("\n SAVINGS  :", self.sa)
    def salary(self):
        self.sal = self.sa + self.exp
    def sal_dis(self):
        print("\nTOTAL SALARY : ", self.sal)

e = float(input("\n ENTER THE EXPENDITURE"))
s = float(input("\n ENTER THE SAVINGS"))
obj = expenditure(e, s)
obj.display()
obj.salary()
obj.sal_dis()
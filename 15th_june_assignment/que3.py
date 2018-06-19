# QUESTION 3: CREATING COP CLASS AND ANOTHER CLASS MISSION WHICH EXTENDS COP CLASS
class Cop:
    def __init__(self, name, age, w_experince, designation):
        """
        INTIALIZATION
        :param name:
        :param age:
        :param w_experince:
        :param designation:
        :return:
        """
        self.c_name = name
        self.c_age = age
        self.c_w_exp = w_experince
        self.desig = designation

    def display(self):
        """
        DISPALY FUNCTION .ITS DISPLAY DETAILS OF COPS

        :return:
        """
        print("NAME:", self.c_name, "\t\t", "AGE : ", self.c_age, "\t\t", "EXPERINCE : ",  self.c_w_exp, "\t\t", "DESIGNATION : ",  self.desig)

    def update(self, name, age, w_experince, designation):
        """
        UPDATE METHOD TO UPDATE THE DETAILS OF COP
        :param name:
        :param age:
        :param w_experince:
        :param designation:
        :return:
        """
        self.c_name = name
        self.c_age = age
        self.c_w_exp = w_experince
        self.desig = designation

class Mission(Cop):   # class Mission extends cop class

    def add_mission_detail(self):
        """
        METHOD WHICH CHECK THE DETAIL OF  COP AND SELECT FOR MISSION
        MISSION SELECTION CRITERIA   1> AGE SHOULD BE GRETER THAN 26  (AGE>26)
        2> WORK EXPERIENCE MINIMUM 6YRS     EXPERIANCE>6

        :return:
        """
        if self.c_age > '26':
            print("\n\n\t", self.c_name, "  SELECTED IN MISSION")
        else :
            pass


total_cop = int(input("\n ENTER THE TOTAL NO OF COPS"))    # INPUT FOR TOTAL NO OF COP
object_cop_lis = [ ]      # CREATING LIST FOR STORING OBJECT LIST WHICH ARE COP

for i in range(total_cop):
    """
    for loop which creating object in terms of list
    """
    object_cop_lis.append(i)

for k in range(total_cop):
    """
    TAKING USER INPUT FOR COP DETAIL IN TERM OF LIST
    """
    lis = list(input("\n ENTER THE NAME OF COP  , AGE , WORK EXPERIANCE AND DESIGNATION ").strip().split(" "))

    object_cop_lis[k] = Cop(lis[0], lis[1], lis[2], lis[3])    # creating object and passing details
    object_cop_lis[k] = Mission(lis[0], lis[1], lis[2], lis[3])
print("\n \t\t\t COPS DETAILS")
for dis in range(total_cop):
    """
        THIS FOR LOOP DISPLAYING THE DETAILS OF COP
    """
    object_cop_lis[dis].display()

update_det = input("\n IF YOU WANT TO UPDATE THE DETAILS OF COP THEN PRESS Y OTHERWISE N")

if update_det == "y" or update_det == "Y":
    total = int(input("\n HOW MANY COPS DETAILS YOU WANT TO UPDTAE "))
    for i in range(total):  # INPUT OF UPDATE VALUE
        n = int(input("\n ENTER THE COP NO WHOM YOU WANT TO UPDATE DETAILS"))
        lis = list(input(" ENTER THE COP NAME AGE WORK EXPERIANCE AND DESIGNATION ").strip().split(" "))
        object_cop_lis[n - 1].update(lis[0], lis[1], lis[2], lis[3])  # UPDATING COPS DETAILS
    # DISPLAYING COPS DETAILS AFTER UPDATE
    print("\n\n \tAFTER UPDATING THE COPS DETAIL")
    print("\n\t\t  COPS DETAILS")

    for i in range(total_cop):
        object_cop_lis[i].display()
else:
    pass

for i in range(total_cop):
    """
    for loop to check the details of cop for selection in mission
    """
    #object_cop_lis[i]  = Mission()
    object_cop_lis[i].add_mission_detail()


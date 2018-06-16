# QUESTION 4 : CREATING CLASS FOR MOVIE DETAILS
class MovieDetails:
    def __init__(self, name, artistname, release_y, rating):  # INTILIZING MOVIE DETAILS
        self.m_name = name
        self.a_name = artistname
        self.r_year = release_y
        self.rat = rating

    # DISPLAYING MOVIES DETAAILS

    def display(self, i):
        print("\n", i+1, "\t\t", self.m_name, "\t\t\t\t", self.a_name, "\t\t\t\t", self.r_year, "\t\t\t", self.rat)


    # UPDATING MOVIES DETAILS

    def update(self, name, artistname, release_y, rating):
        self.m_name = name
        self.a_name = artistname
        self.r_year = release_y
        self.rat = rating


# INTIALIZING LIST FOR TOTAL MOVIE
f = [ ]

# INPUT TOTAL NO OF MOVIES
m = int(input("\n ENTER THE TOTAL NO OF MOVIE"))

# CREATING LIST OF TOTAL NO OF MOVIES
for i in range(m):
    f.append(i)

# TAKING INPUT FROM USER OF MOVIES DETAILS
for i in range(m):
    lis = list(input(" ENTER THE MOVIE NAME ARTIST NAME RELEASE YEAR  AND RATING OF MOVIE ").strip().split(" "))

# CREATING OBJECT OF MOVIEDETAILS CLASS AND PASSING DETAILS
    f[i] = MovieDetails(lis[0], lis[1], lis[2], lis[3])

# PRINTING DETAILS OF MOVIES
print("\t\t  MOVIE DETAILS")
print("S.NO\tNAME\t\t\tARTIST NAME\t\t\tRELEASE YEAR\t\tRATING")
for i in range(m):
    f[i].display(i)

# TALKING INPUT FOR UPDATING MOVIE DETAILS
o = (input("\n IF YOU WANT TO UPDATE THE MOVIE DETAIL THEN PRESS Y OTHERWISE PRESS N"))
if o == 'y' or o == "Y":
    t = int(input("HOW MANY MOVIES DETAILS YOU WANT TO UPDATE : "))
    for i in range(t):       # INPUT OF UPDATE VALUE
        n =int(input("\n ENTER THE MOVIE NO WHOM YOU WANT TO CHANGE THE DETAILS"))
        lis = list(input(" ENTER THE MOVIE NAME ARTIST NAME RELEASE YEAR  AND RATING OF MOVIE ").strip().split(" "))
        f[n-1].update(lis[0], lis[1], lis[2], lis[3])  # UPDATING MOVIES DETAILS

# DISPLAYING MOVIE DETAILS AFTER UPDATE
print("\n\n \tAFTER UPDATING THE MOVIE DETAIL")
print("\n\t\t  MOVIE DETAILS")
print("S.NO\tNAME\t\t\tARTIST NAME\t\t\tRELEASE YEAR\t\tRATING")
for i in range(m):
    f[i].display(i)
else:
    exit()

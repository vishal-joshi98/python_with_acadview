# QUESTION 5: WRITING 10 RANDOM NUMBER IN FILE AND SORT NUMBER AND STORE IN ANOTHER FILE
import random      # importing random number to generate random number
def Random_No(fname1, fname2, n):
    """
    Function to generate  random number  and store in file and then sort
    :param f: File name to store random no
    :param n: total no of random to generate
    :return:
    """
    f1 = open(fname1, "w")  #opening file to write
    for ran in range(n):
        f1.write(str(random.random())+"\n")      # writing random number in file

    f1.close()

    f = open(fname1, "r")
    lines = f.read().splitlines()

    sorted_lines = sorted(map(str, lines))    # SORTING RANDOM NUMBER

    file_to_save_to = open(fname2, "w")
    for line in sorted_lines:                   # WRITING SORTED RANDOM NUMBER IN SECOND FILE
        file_to_save_to.write((line)+"  ,")
    file_to_save_to.close()

    print("\n \n\t\t AFTER SORT RANDOM NUMBER   \n FILE :\n")
    with open(fname2) as f:
        for line in f:
            print(line)



file1 = input("\n ENTER THE FILE NAME IN WHICH YOU WANT TO STORE RANDOM NUMBER")
file2 = input("\n ENTER THE FILE IN WHICH YOU WANT TO STORE SORTED RANDOM NUMBER")
no_rand = int(input("\n ENTER THE NO OF RANDOM TO BE GENEARTE"))

try:
    Random_No(file1, file2, no_rand)
except:
    print(" \n FILE ERROR!........")


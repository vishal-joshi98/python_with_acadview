# QUESTION 3: COPY CONTENT OF ONE FILE TO ANOTHER FILE
def ContentCopy(fname1, fname2):
    """
    function copy the content from one file to another file
    :param fname1:  file 1 from where we copy content
    :param fname2:  file 2 in which we copy content
    :return:
    """
    f2 = open(fname2, "w")
    with open(fname1) as f1:
        for line in f1:         # for loop for copy the content of one file to another
            f2.write(line)       # writing content of file 1 into another

    f2.close()      # closing second file

    print("\n AFTER COPY THE CONTENT OF ONE FILE TO ANOTHER \n \t CONTENTS OF BOTH FILE\n:")
    print("\n\t FILE 1 CONTENT :\n")
    with open(fname1) as f1:
        for line in f1:
            print(line)


    print("\n \t FILE 2 CONTENT :\n")
    with open(fname2) as f2:
        for line1 in f2:
            print(line1)

file1 = input("\n ENTER THE FIRST FILE NAME FROM WHERE YOU WANT TO COPY THE CONTENT")

file2 = input(("\n ENTER THE SECOND FILE NAME IN WHICH YOU WANT TO COPY"))

try:
    ContentCopy(file1, file2)
except:
    print("FILE ERROR !......")
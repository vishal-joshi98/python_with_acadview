# QUESTION 1: READING LAST N LINE
def LastNLine(fname, n):
    """
    READING LAST N LINES
    :param f: FILE NAME
    :param n: NO OF LINE TO READ
    :return:
    """
    with open(fname) as file:
        print('Last', n, 'lines from', fname)
        for line in(file.readlines()[-n:]):     # reading last n lines
            print(line, end=' ')

name = input("\n ENTER THE FILE NAME")
n = int(input("ENTER NO OF LAST LINE"))
try:
    LastNLine(name, n)
except:
    print(" FILE ERROR !...")
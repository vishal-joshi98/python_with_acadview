# QUESTION 2: FREQUENCY OF WORD IN  FILE

def WordFreq(fname):
    """
    FUNCTION COUNT THE FREQUENCY OF WORD
    :param f: FILE NAME
    :return:
    """
    Wordcount = { }     # dictionary to store the frequency of word
    with open(fname) as file:
        for word in file.read().split():
            if word not in Wordcount:
                Wordcount[word] = 1
            else:
                Wordcount[word] += 1
    for k, v in Wordcount.items():
        print(k, " : ", v)




FileName = input("\n ENTER THE FILE NAME")    # input for file name
try:
    WordFreq(FileName)     # function calling
except:
    print("File Error !.....")
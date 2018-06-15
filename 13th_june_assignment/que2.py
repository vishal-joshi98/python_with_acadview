import time  # import time module for time formatted
# QUESTION 2: FORMATTED TIME
def formatted():  # FUNCTION FOR PRINT FORMATTED TIME
    print(time.gmtime())   # print current formatted time
    print("\n",time.time())           # print time in second
    print("\n",time.gmtime(time.time()))  #convert seonds into present time

formatted()
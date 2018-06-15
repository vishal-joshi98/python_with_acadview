import time   # import time module
# QUESTION 3: EXTRACTING MONTH FROM TIME
s1 = time.gmtime(time.time())
print("\n CURRENT TIME: ", s1)
s2 = s1.tm_mon    # MONTH FROM TIME
print("MONTH EXTRACTED FROM TIME =: ", s2)

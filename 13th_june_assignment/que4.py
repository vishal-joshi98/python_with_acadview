import time   # import time module
# QUESTION 3: EXTRACTING DAY FROM TIME
s1 = time.gmtime(time.time())
print("\n CURRENT TIME: ", s1)
s2 = s1.tm_mday    # MONTH FROM TIME
print("DAY EXTRACTED FROM TIME =: ", s2)

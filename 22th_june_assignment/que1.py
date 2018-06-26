# QUESTION 1: EXTRACT USERID DOMAIN AND SUFFIX FROM  EMAIL ADDRESS"
import re
email_1 = re.match(r'(......)@(........).(...)', 'zuck26@facebook.com')

email_2 = re.match(r'(......)@(......).(...)', 'page33@google.com')

email_3 = re.match(r'(......)@(......).(...)', 'jeff42@amazon.com')

print(" OUTPUT  : \n\t")
print(email_1.groups())

print(email_2.groups())

print(email_3.groups())


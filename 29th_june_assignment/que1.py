#QUESTION 1: CREATING DATAFRAME AND STORING DATA OF ME AND MY FRIEND
import pandas as pd

data = {'Name':['vishal', 'vivek'], 'Age':[28,23], 'Mail':['joshivishal506@gmail.com', 'vvekjoshi@live.com'], 'Phone No':[8847235763, 9872139933]}
df = pd.DataFrame(data, index= [1,2])     # CREATING DATA FRAME OF NAME MAIL AGE AND PHONE NO
#print(df.shape)

print(df)
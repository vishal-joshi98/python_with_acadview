# QUESTION 3: SPLITING
import re
text = "A, very very; irregular_sentence"

print("\n\tOUTPUT : ")
print(re.sub(r'[_,;]', ' ', text))
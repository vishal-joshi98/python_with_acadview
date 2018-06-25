#QUESTION 4: COMBINING EACH LINE FROM ONE FILE WITH THE CORRESPONDING LINE IN SECOND FILE

with open("file1.txt") as f1, open("file2.txt") as f2:
	for line1, line2 in zip(f1,f2):
		print(line1+line2)



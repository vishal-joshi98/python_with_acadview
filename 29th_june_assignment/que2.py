#
import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/Shreyas3108/Weather/master/weather.csv')    # READING DATA AND CONVERTING IN DATAFRAME

print("\n\tDATAFRAME  : ",df)
# 1:   FIRST FIVE ROW

five_row = df.head(5)

print("\n\n\t FIRST FIVE ROW OF DATA FRAME : ")

print(five_row)

# 2: FIRST 10 ROWS OF DATA FRAME

Ten_row = df.head(10)

print("\n\t FIRST TEN ROW OF DATA FRAME : ")

print(Ten_row)

# c and e :BASIC STATISTICS OF DATA FRAME   AND ON 2ND COLUMN MinTemp
print("\n\t\t BASIC STATISTICS OF DATA FRAME")
# SUM OF COLUMN MIN TEMPERATUE
sum = df['MinTemp'].sum(skipna = True)
print("\n\t\t SUM OF COLUMN MinTemp OF DATAFRAME  :  ",sum)


#ARITHMATIC MEAN OF COLUMN VALUES
#ARITHMATIC MEAN OF MinTemp COLUMN OF DATAFRAME
mean = df['MinTemp'].mean()

print("\n\t\t MEAN OF COLUMN MinTemp   :  ", mean)




# SUMMARY STATISTICS
describe_f = df['MinTemp'].describe()

print("\n\t\t SUMMARY STATISTICS   : \n", describe_f)


# COUNTING THE NUMBER OF VALUES IN COLUMN

print("\n\t TOTAL NUMBER OF VALUES  : ", df['MinTemp'].count())

# MAXIMUM AND MINIMUM VALUE FROM A COLUMN OF A DATAFRAME
print("\n\t\t MAXIMUM VALUE  : ", df['MinTemp'].max())

print("\n\t\t MINIMUM VALUE  : ", df['MinTemp'].min())



# MEDIAN OF COLUMN
print("\n\t\t MEDIAN VALUE  : ", df['MinTemp'].median())


# MODE OF COLUMN
print("\n\t\t MODE VALUE  : ", df['MinTemp'].mode())

#d:  LAST FIVE ROWS
print("\n\tLAST FIVE ROWS OF DATAFRAME  : ",df.tail(5))



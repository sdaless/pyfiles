#Sara D'Alessandro
#November 2, 2018
#Count which cars got the most parking tickets

import pandas as pd

csvFile = input('Enter CSV file name: ')
column = input('Name attribute: ')

tickets = pd.read_csv(csvFile)

print("The 10 worst offenders are:")
print(tickets[column].value_counts()[:10]) 

#Sara D'Alessandro
#November 7, 2018
#This program does things with collisions.

import pandas as pd

csvFile = input("Enter CSV file name: ")

factors = pd.read_csv(csvFile)

print("Top three contributing factors for collisions: ")
print(factors["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])



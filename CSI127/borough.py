#Sara D'Alessandro
#October 22, 2018
#This program asks the user for the borough, an output file, and then displays the fraction of the population. 

import matplotlib.pyplot as plt
import pandas as pd

bor = input("Enter borough name: ")
newimg = input("Enter output file name: ")

pop = pd.read_csv('nycHistPop.csv',skiprows=5)

pop['Fraction'] = pop[bor]/pop['Total']

pop.plot(x = 'Year', y = 'Fraction')

fig = plt.gcf()
fig.savefig(newimg)

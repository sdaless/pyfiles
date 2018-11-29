#Sara D'Alessandro
#October 24, 2018
#This program makes a plot of the fraction of the total population that are children over time.

import matplotlib.pyplot as plt
import pandas as pd

data = input("Enter input file name: ")
newimg = input("Enter output file name: ")

pop = pd.read_csv(data)
pop['Fraction Children'] = pop['Total Children in Shelter']/pop['Total Individuals in Shelter']
pop.plot(x = 'Date of Census', y = 'Fraction Children')

fig = plt.gcf()
fig.savefig(newimg)

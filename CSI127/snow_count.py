#Sara D'Alessandro
#A program that asks the user for the name of a png file and print the number of pixels that are nearly white.
#October 9th, 2018

import matplotlib.pyplot as plt
import numpy as np

snowFile = input("Please enter the name of a file: ")

ca = plt.imread(snowFile)   
countSnow = 0            
t = 0.75                

for i in range(ca.shape[0]):
     for j in range(ca.shape[1]):
          if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
               countSnow = countSnow + 1

print("Snow count is", countSnow)

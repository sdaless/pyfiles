#Sara D'Alessandro
#October 24, 2018
#This program asks the user for the name of an image and an output file. It then saves the lower left quarter of the image.

import matplotlib.pyplot as plt
import numpy as np

inF = input("Enter file name: ")
out = input("Enter output file: ")

img = plt.imread(inF) 

height = img.shape[0] 
width = img.shape[1] 

newimg = img[height//2:, :width//2] 

plt.imsave(out, newimg) 

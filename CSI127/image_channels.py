#Sara D'Alessandro
#A program that changes the color of turtle
#September 26th, 2018

#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np


img = plt.imread(input("Enter the name of an input file with extension: "))   
newimg = input("Enter the name of an output file with extension: ")
plt.imshow(img)		          
plt.show()                         

img2 = img.copy()        
img2[:,:,1] = 0              
img2[:,:,0] = 0          

plt.imshow(img2)         
plt.show()               

plt.imsave(newimg, img2)  

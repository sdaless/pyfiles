# Name:  Sara D'Alessandro
# Date:  October 19, 2018
# Takes elevation data of NYC and displays using the default color map


#Import the libraries for arrays and displaying images:
import numpy as np
import matplotlib.pyplot as plt

#Read in the data to an array, called elevations:
elevations = np.loadtxt('elevationsNYC.txt')

#Take the shape (dimensions) of the elevations
#  and add another dimension to hold the 3 color channels:
mapShape = elevations.shape + (3,)

#Create a blank image that's all zeros:
topoMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        
        if elevations[row,col] <= 0:
            #Below sea level
           topoMap[row,col,2] = 0.25     #Set the blue channel to 100%
           
        elif elevations[row,col] % 10 == 0:
            #Below the storm surge of Hurricane Sandy (flooding likely)
           topoMap[row,col,0] = 0     #Set the red channel to 100%
           
        else:
            #Above the 6 foot storm surge and didn't flood
            topoMap[row,col,1] = 0.5   #Set the green channel to 100%
            topoMap[row,col,2] = 0.5
            topoMap[row,col] = 0.5

#Save the image:
plt.imsave('topo.png', topoMap)

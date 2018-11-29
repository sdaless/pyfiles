# Examples of Image-manipulation and filters

# Use this command from the Windows command prompt to install opencv3...
# conda install -c menpo opencv3

import cv2
import numpy as np
from matplotlib import pyplot as plt


# Simple function to read in a picture file and display it

def simple_display():
	""" some initial trials... read and show images """

	# Reading and color-converting an image to RGB
	raw_image = cv2.imread('monalisa.jpg',cv2.IMREAD_COLOR) 

	# convert an OpenCV image (BGR) to an "ordinary" image (RGB) 
	image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2RGB)

	plt.xticks([]), plt.yticks([])  # to hide axis labels
	plt.imshow(image)    
	plt.show()
	input("Hit enter to continue...")





def transform( image ):
    """ an example of a pixel-by-pixel filter 
        input: an r, g, b image
        output: a transformed r, g, b image
    """
    new_image = image.copy()
    num_rows, num_cols, num_chans = new_image.shape
    for row in range(num_rows):
        for col in range(num_cols):
            r, g, b = image[row,col]

            # Red filter
            new_image[row,col] = [255, g, b]

            # Green filter
            #new_image[row,col] = [r, 255, b]

            # Blue filter
            #new_image[row,col] = [r, g, 255]

            # Greyscale filter (averages the r, g, b values)
            #grey = ((r+g+b)/3)
            #new_image[row,col] = [grey, grey, grey]

            # Greyscale filter with Luminosity (weights the r, g, b values for human eye perception)
            #grey =((r*0.3)+(g*0.59)+(b*0.11))/3
            #new_image[row,col] = [grey, grey, grey]

    return new_image

#
# try that filter!
#
def color_filter():
    """ try out a filter! """
    raw_image = cv2.imread('flag.jpg',cv2.IMREAD_COLOR)
    flag = cv2.cvtColor(raw_image, cv2.COLOR_BGR2RGB)
    new_image = transform( flag )
    plt.imshow(new_image)
    plt.show() 




# Here are some inverted color filters...

def invert():

    raw_image = cv2.imread('spam.png',cv2.IMREAD_COLOR)
    spam = cv2.cvtColor(raw_image, cv2.COLOR_BGR2RGB)
    
    new_image = raw_image.copy()
    num_rows, num_cols, num_chans = new_image.shape
    for row in range(num_rows):
        for col in range(num_cols):
            r, g, b = raw_image[row,col]

            # RGB -> BRG
            new_image[row,col] = [b, r, g]

            # RGB -> 255-G
            #new_image[row,col] = [r, 255-g, b]

            # RGB -> 255-(all values)
            #new_image[row,col] = [255-r, 255-g, 255-b]

            # RGB -> 255-G (as the r value)
            #new_image[row,col] = [255-g, b, r]

    plt.imshow(new_image)
    plt.show()


simple_display()
#color_filter()
#invert()
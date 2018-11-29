#Name:  Sara D'Alessandro
#Date: September 23, 2018
#This program implements psuedocode to draw a block spiral.

import turtle

todd  = turtle.Turtle()

for i in range(10, 260, 10):
    todd.forward(i + 1)
    todd.left(90)

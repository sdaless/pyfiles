#Sara D'Alessandro
#A program that demonstrates shades of blue
#September 26th, 2018

import turtle				

turtle.colormode(255)	    
tess = turtle.Turtle()		
tess.shape("turtle")	    
tess.backward(100)			

for i in range(0,255,10):
     tess.forward(10)		
     tess.pensize(i)		
     tess.color(0,0,i)

#Name: Sara D'Alessandro
#November 16, 2018
#This program makes turtles do the squiggle.

import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(100):
  trey.forward(10)
  a = random.randrange(360)
  trey.right(a)

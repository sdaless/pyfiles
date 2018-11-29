#Sara D'Alessandro
#A program that changes the color of turtle
#September 26th, 2018

import turtle

tut = turtle.Turtle()
tut.shape("turtle")

hex = input("Enter a hex string starting with '#' sign: ")

tut.color(hex)

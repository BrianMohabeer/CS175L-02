#Brian Mohabeer
#CS175L
#Turtle Graphics Stop Sign

import math
import turtle
import random

#Named Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATED_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

s = LENGTH
x = s/math.sqrt(2)
diameter = s + (2 * x)

turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
diameter = s + (2 * x)

turtle.color('black')
turtle.pensize(3)
turtle.penup()
turtle.setpos(-10, diameter/2)
turtle.pendown()
turtle.fillcolor('red')
turtle.begin_fill()
for x in range(NUM_SIDES):
    turtle.forward(LENGTH)
    turtle.right(ANGLE)
turtle.end_fill()
turtle.penup()
turtle.setpos(TEXT_X, TEXT_Y)
turtle.color('white')
turtle.pendown()
turtle.write("STOP", font=("Arial",26,"bold"))
turtle.hideturtle()

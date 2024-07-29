from turtle import *
import turtle
from random import *
t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(1.0, 1.0)
width=int(window_width())
height=int(window_height())
#100 stars, black background
#random star size and location
bgcolor("black")
t.speed(40)
def draw_star(width,height):
  t.penup()
  t.goto(randrange(round(-width/2),round(width /2)), randrange(round(-height/2),round(height/2)))
  t.pendown()
  t.color("white")
  t.begin_fill()
  t.circle(randrange(1,10))
  t.end_fill()




for x in range(100):
  draw_star(width,height)
  x=x+1
  












screen.mainloop()
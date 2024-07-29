from turtle import *
import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(1.0, 1.0)

def move_and_turn(t,angle):
  t.forward(50)
  t.right(angle)

for x in range(12):
  move_and_turn(t,30)












screen.mainloop()
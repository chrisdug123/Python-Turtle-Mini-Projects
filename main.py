



from turtle import *
import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(1.0, 1.0)


def move_and_turn(turtle,distance, angle):
  turtle.forward(distance)
  turtle.right(angle)

move_and_turn(t,100, 45)
move_and_turn(t,50,90)

screen.mainloop()
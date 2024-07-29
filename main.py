from turtle import *
import turtle
from random import *
t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(1.0, 1.0)
width=int(window_width())
height=int(window_height())
#Create a turtle that can move in 4 directions
#Have an end goal
#Have visual feedback when we reach the goal
t.speed(0)
move_distance=20

bgcolor("#D2691E")

t.penup()
t.goto(100,200)
t.pendown()
t.color("blue")
t.begin_fill()
t.goto(300,200)
t.goto(300,-200)
t.goto(100,-200)
t.goto(100,200)
t.end_fill()

t.penup()
t.goto(-200,0)
t.shape("turtle")
t.color("green")

def move_up():
  t.setheading(90)
  t.forward(move_distance)
  check_goal()

def move_down():
  t.setheading(270)
  t.forward(move_distance)
  check_goal()
  
def move_left():
  t.setheading(180)
  t.forward(move_distance)
  check_goal()

def move_right():
  t.setheading(0)
  t.forward(move_distance)
  check_goal()
  
def check_goal():
  if t.xcor() > 100:
    t.hideturtle()
    t.color("white")
    t.write("You WIN !")
    onkey(None, "Up")
    onkey(None, "Down")
    onkey(None, "Left")
    onkey(None, "Right")
    

onkey(move_up, "Up")
onkey(move_down, "Down")
onkey(move_left, "Left")
onkey(move_right, "Right")
listen()





screen.mainloop()
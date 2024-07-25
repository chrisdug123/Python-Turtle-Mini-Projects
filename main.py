



from turtle import *
import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(1.0, 1.0)


diameter = 40
pop_diameter = 100

def draw_balloon(t):
  t.color("red")
  t.dot(diameter)


def inflate_balloon():
  global diameter
  global t
  diameter = diameter + 10
  draw_balloon(t)
  if diameter >= pop_diameter:
    t.clear()
    diameter = 40
    t.write("POP!")
  
draw_balloon(t)
onkey(inflate_balloon, "Up")
listen()
screen.mainloop()
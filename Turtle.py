import turtle
import time
import random

# nmn=turtle.Turtle()
# nmn.shape('turtle')
# nmn.color('red')
# nmn.pensize(20)

# time.sleep(3)

turtle.Turtle()
colors=["red", "blue", "green", "yellow", "black"]

def up():
	turtle.setheading(90)
	turtle.forward(100)
def down():
	turtle.setheading(270)
	turtle.forward(100)
def left():
	turtle.setheading(180)
	turtle.forward(100)
def right():
	turtle.setheading(0)
	turtle.forward(100)
def leftclick(x,y):
	turtle.color(random.choice(colors))
def rightclick(x,y):
	turtle.stamp()

turtle.listen()

turtle.onkey(up,'Up')
turtle.onkey(down,'Down')
turtle.onkey(left,'Left')
turtle.onkey(right,'Right')
turtle.onscreenclick(leftclick,1)
turtle.onscreenclick(rightclick,3)

turtle.mainloop()
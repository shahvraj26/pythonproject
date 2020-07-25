import turtle
import threading
import time

turtle.shape("turtle")
turtle.color("red")
turtle.color("red")
screen = turtle.Screen()
screen.bgcolor("blue")



move_speed = 5
turn_angle = 15

def forward():
    turtle.forward(move_speed)
    
def backward():
    turtle.backward(move_speed)

def left():
    turtle.left(turn_angle)

def right():
    turtle.right(turn_angle)


screen.onkey(forward,"Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

def PetersFunc():
    PetersVar = True
    while True:
        if PetersVar == False:
            PetersVar = True
            screen.onkey(turtle.pendown(), "Space")
            screen.listen()
        elif PetersVar == True:
            screen.onkey(turtle.penup(), "Space")
            PetersVar = False
            screen.listen()
        else:
            print('What the %s%s%s%s?!?!?!')
            end()

PetersThread = threading.Thread(target=PetersFunc)

screen.listen()

screen.exitonclick()

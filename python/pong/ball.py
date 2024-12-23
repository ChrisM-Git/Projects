from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.shapesize(1,1)
        self.penup()
        #creat a move variable so when ball hits wall we can change the direction
        self.xmove = 10
        self.ymove = 10
        self.movespeed = 0.07

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce(self):
        """ creates a variable for the y axis so we can change the direction of ball ewhen
        it hits a wall  the multiply by -1 provides a negative value and reverses direction
        of the ball
        """
        self.ymove *= -1
    def paddlebounce(self):
        self.xmove *= -1

    def resetball(self):
        self.goto(0,0)
        self.paddlebounce()
        self.movespeed = 0.07






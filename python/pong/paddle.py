from turtle import Turtle
UP = 90
DOWN = 270


class Paddle(Turtle):
     def __init__(self,position):
         super().__init__()
         self.shape("square")
         self.color("white")
         self.shapesize(stretch_wid=5,stretch_len=1)
         self.penup()
         self.goto(position)




     def R_Up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)


     def R_Down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)



     def L_Up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)


     def L_Down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)


from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.rscore = 0
        self.lscore = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.rscore}", align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(f"{self.lscore}", align="center", font=("Courier", 80, "normal"))


    def lpoint(self):
        self.lscore += 1
        self.update_score()
        if self.lscore == 7:
            gameon == False
            self.write("Left Wins!", align="center", font=("Courier", 80, "normal"))


    def rpoint(self):
        self.rscore += 1
        self.update_score()
        if self.rscore == 7:
            gameon == False
            self.write("Left Wins!", align="center", font=("Courier", 80, "normal"))


    def winner(self,player):

        self.write(f"{player} Wins!", align="center", font=("Courier", 80, "normal"))


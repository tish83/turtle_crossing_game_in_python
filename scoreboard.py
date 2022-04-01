from turtle import Turtle


FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.goto(-280, -290)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)    
    
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()

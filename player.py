from turtle import Turtle

from car_manager import CarManager

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle, CarManager):
    
    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.go_to_start()
        self.goto(STARTING_POSITION)

    def move_forwards(self):
        self.sety(self.ycor() + MOVE_DISTANCE)
        
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_finish_line(self):
        if self.ycor()>=FINISH_LINE_Y:
            return True
        else: return False
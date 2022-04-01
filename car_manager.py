from random import randint
import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,5)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.goto(300, randint(-200, 300))
            self.all_cars.append(new_car)

    def cars_move(self):
        for car in self.all_cars:
            car.setx(car.xcor() - self.car_speed)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
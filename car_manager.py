import random
from turtle import Turtle
from player import Player
import time

COLORS = ["red", "violet", "pink", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
rand_y=(range(-240,300,20))


class CarManager(Turtle):
    def __init__(self):
        super(CarManager, self).__init__()
        self.right_cars=[]
        self.left_cars = []
        self.distance = STARTING_MOVE_DISTANCE
    def create_car(self):
        random_chance = random.randint(1,40)
        random_direction = random.randint(0,2)
        if self.distance<5:
            if random_chance ==1 :
                new_car =Turtle()
                new_car.hideturtle()
                new_car.shape("square")
                new_car.color(random.choice(COLORS))
                new_car.shapesize(1, 2)
                new_car.penup()
                if random_direction == 0:
                    new_car.setposition(300, random.choice(rand_y))
                    new_car.showturtle()
                    self.right_cars.append(new_car)
                elif random_direction ==1:
                    new_car.setposition(-300, random.choice(rand_y))
                    new_car.showturtle()
                    self.left_cars.append(new_car)
        elif self.distance<15:
            if random_chance<10:
                new_car = Turtle()
                new_car.hideturtle()
                new_car.shape("square")
                new_car.color(random.choice(COLORS))
                new_car.shapesize(1, 2)
                new_car.penup()
                if random_direction == 0:
                    new_car.setposition(300, random.choice(rand_y))
                    new_car.showturtle()
                    self.right_cars.append(new_car)
                elif random_direction ==1:
                    new_car.setposition(-300, random.choice(rand_y))
                    new_car.showturtle()
                    self.left_cars.append(new_car)
        else:
            if random_chance<20:
                new_car = Turtle()
                new_car.hideturtle()
                new_car.shape("square")
                new_car.color(random.choice(COLORS))
                new_car.shapesize(1, 2)
                new_car.penup()
                if random_direction == 0:
                    new_car.setposition(300, random.choice(rand_y))
                    new_car.showturtle()
                    self.right_cars.append(new_car)
                elif random_direction ==1:
                    new_car.setposition(-300, random.choice(rand_y))
                    new_car.showturtle()
                    self.left_cars.append(new_car)



    def random_move_cars(self):
        for car in self.right_cars:
            car.backward(self.distance)
        for car in self.left_cars:
            car.forward(self.distance)


    def increase_cars_speed(self):
        self.distance+=MOVE_INCREMENT

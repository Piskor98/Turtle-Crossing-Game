import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import playsound
#creating screen object
screen = Screen()

#creating a player object
player=Player()


car_manager = CarManager()

#creating a scoreboard
scoreboard = Scoreboard()


#screen setup
screen.listen()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.onkeypress( key = "w", fun = player.player_move )

#Main loop
game_is_on = True

while game_is_on:

    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.random_move_cars()

    if player.ycor()==280:
        player.level_counter()
        player.finish()
        car_manager.increase_cars_speed()
        scoreboard.increase_level()

    #Detect collision
    for car in car_manager.right_cars:
        if car.distance(player)<20:
            scoreboard.losing()
            game_is_on = False



if game_is_on ==False:
    playsound.playsound("losing.wav")

screen.exitonclick()
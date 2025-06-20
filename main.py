from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor('black')
screen.title("Snake Game Ultimate!")
screen.tracer(0)

scoreboard = ScoreBoard()
scoreboard.game_start()


def run_game():
    global is_game_running
    if is_game_running: return

    is_game_running = True
    scoreboard.refresh()
    snake = Snake()
    food = Food()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")


    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.07)
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.increase_score()
            snake.extend_snake()

        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False
            scoreboard.reset()
            for seg in snake.segments:
                seg.goto(1000,1000)
            food.goto(1000,1000)
            scoreboard.game_over()

        for segment in snake.segments[1::]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.reset()
                for seg in snake.segments:
                    seg.goto(1000, 1000)
                food.goto(1000, 1000)
                scoreboard.game_over()



    is_game_running = False

screen.listen()
is_game_running = False
screen.onkey(run_game, "space")
screen.exitonclick()
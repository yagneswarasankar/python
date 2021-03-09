from turtle import Screen
import time
from src.Python100DaysChallenge.Day20_SnakeGame_Part1.snake import Snake
from src.Python100DaysChallenge.Day20_SnakeGame_Part1.Food import Food
from src.Python100DaysChallenge.Day20_SnakeGame_Part1.score import Score


my_screen= Screen()
my_screen.setup(height=600,width=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)

#To do :Create Snakebody
snake = Snake()
food  = Food()
score = Score()


my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.left,"Left")
my_screen.onkey(snake.right,"Right")

game_on = True

while game_on:
  my_screen.update()
  time.sleep(0.1)
  snake.move()
 #Detect the collission with Food.
  if snake.head.distance(food) < 15:
   snake.extend()
   food.refresh()
   score.calculate_score()

 #Detect the head collision with wall
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
   game_on = False
   score.game_over()


  for segment in snake.segments[1:]:
   # if segment == snake.head:
   #   pass
   if snake.head.distance(segment) < 10:
     game_on = False
     score.game_over()
snake.segments
my_screen.exitonclick()
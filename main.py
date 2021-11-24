#TODO: Build paddles and get them to move up and down 
#TODO: Build ball and get it to move 
#TODO: Build scores 
#TODO: Get the screen with the dotted line and reflect in the top outline 
#TODO: Get the score to work 


#TODO : Create the screen:
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time 

screen = Screen() 
screen.tracer(0)
ball=Ball()
scoreboard = Scoreboard()

screen.bgcolor('black')
screen.setup(width=800, height = 600)
screen.title('Pong Game')

rpaddle = Paddle((350,0))
lpaddle = Paddle((-350,0))
screen.update()
screen.tracer(1)
screen.listen()
screen.onkeypress(rpaddle.up,"Up") #here you don't put brackets as you are using a function as a parameter. 
screen.onkeypress(rpaddle.down,"Down")
screen.onkeypress(lpaddle.up,"w") #here you don't put brackets as you are using a function as a parameter. 
screen.onkeypress(lpaddle.down,"s")

screen.update()
#screen.tracer(1)
game_is_on = True 
setting = 0.1
while game_is_on: 
    screen.update()
    time.sleep(setting)
    ball.move_ball()

    #detect collision with wall, if there is one then bounce 
    if ball.ycor() > 270 or ball.ycor() <-270: 
        ball.bouncewall() 

    #detect collision with right paddel 
    if (ball.distance(rpaddle)< 40 and 332<=ball.xcor()<=360 ) or (ball.distance(lpaddle)< 40 and -332 > ball.xcor() > -360 ): 
        setting = setting * 0.7
        ball.bouncepad()
    
    #detect a miss on right side 
    if ball.xcor() > 380: 
        setting = 0.1
        ball.resetballleft()
        scoreboard.l_score+= 1
        scoreboard.updatescoreboard()
        

    #detect a miss on the left side
    if ball.xcor() < -380: 
        setting = 0.1
        ball.resetballright()
        scoreboard.r_score += 1
        scoreboard.updatescoreboard()
        

screen.exitonclick()

from turtle import Turtle, heading 
import random 
import time 

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.headingin = 45


    def create_ball(self): 
        self.penup()
        self.shape('circle')
        self.color('white')
        
    def move_ball(self): 
        self.setheading(self.headingin)
        self.forward(20)
         
    def bouncewall(self): 
        self.headingin = 360- self.headingin 
        self.setheading(self.headingin)

    def bouncepad(self):
        self.headingin =  360 - self.headingin + 180 
        self.setheading(self.headingin)

    def resetballleft(self): 
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
        self.headingin=(random.randint(110,160))

    def resetballright(self): 
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
        self.headingin=(random.randint(30,60))

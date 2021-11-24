from turtle import Turtle

class Paddle(Turtle): 
    def __init__(self,position): #now we are inside the paddle class, tap into methods and attributes using self key word. 
        super().__init__() #this initiates a turtle object and assigns it to the variable self 
        self.create_paddle(position) 

    def create_paddle(self,position): 
        self.penup() 
        self.setpos(position)
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=4, stretch_len=1)

    def up(self):
        new_y = self.ycor() + 20  #use self to get the object
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
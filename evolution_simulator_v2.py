import turtle
import random

wn_main =  turtle.Screen()
wn_main.bgcolor('pink')
wn_main.title('Main')
wn_main.setup(700,700)
wn_main.tracer(0)

class Window(turtle.Turtle):
   def __init__(self):
            turtle.Turtle.__init__(self)
            self.penup()
            self.speed(0)
            self.pen(pensize=10)
            self.left(90)
            self.hideturtle()
            self.color("gold")

class Pen(turtle.Turtle):
   def __init__(self):
            turtle.Turtle.__init__(self)
            self.speed(0)
            self.color('black')
            self.hideturtle()

class Ball(turtle.Turtle):
   def __init__(self):
            turtle.Turtle.__init__(self)        
            self.shape('circle')
            self.setheading(random.randint(0,360))
            self.color(random.choice(("green", "blue", "red", "purple")))
            self.pensize(2)
            self.shapesize(stretch_wid=0.5, stretch_len=0.5)
            self.speed(0)

def make_window(x,y,size):
    window = Window()
    window.goto(x,y)
    window.pendown()
    a = range(4)
    for n in a:
      window.forward(size)
      window.right(90)

balls = []
def make_balls(number_balls):
   i = 0
   while i < number_balls:
      ball = Ball()
      balls.append(ball)
      
      i += 1

make_balls(50)

pen = Pen()

make_window(-300, -300, 600)

global x
x=0.1

global y
y=0

global z
z=20

while True:
    wn_main.update()
    
    for ball in balls:
        x-=0.0001
        ball.forward(1.5)
        ball.right(x)
 
    y += 1
    if y>5:
        z=random.randint(10,50)
        pen.clear()
        pen.write("gefelicteerd spielor!", align='center', font=('Arial', z,'normal'))
        pen.right(10)
        y=0
        

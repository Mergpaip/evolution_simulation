import turtle
import random

wn_main =  turtle.Screen()
wn_main.bgcolor('black')
wn_main.title('Main')
wn_main.setup(1300,800)
wn_main.tracer(0)

count = 0

data_time = 10

number_balls = 30
number_food = 10

round_time = 20
food_energy = 500

ball_energy = 500
ball_speed = 1
ball_vision = 50
reproduction_energy = 1000
reproduction_cost = 500

mutation_speed = 0.5
mutation_vision = 10

class Ball(turtle.Turtle):
   def __init__(self):
            turtle.Turtle.__init__(self)
            
            a = random.randint(-340, 340)
            b = random.choice((-340, 340))

            random_x = random.choice((a, b))
            
            if random_x == a:
                random_y = b
                self.right(-90)
            else:
                random_y = a
            
            self.goto(random_x, random_y)
                       
            self.shape('arrow')
            self.color(random.choice(("green", "blue", "red", "purple", "white", "light blue")))
            self.shapesize(stretch_wid=0.5, stretch_len=1)
            self.penup()
            self.speed(0)
            self.dead_count = 0
            
            self.energy = ball_energy
            self.vision = ball_vision
            self.speed = ball_speed
                
   def destroy(self):
            self.color("dim grey")
            stats_speed.remove(self.speed)
            stats_vision.remove(self.vision)
            
            dead_balls.append(self)
            balls.remove(self)

dead_balls = []
            
class Food(turtle.Turtle):
    def __init__(self):
            turtle.Turtle.__init__(self)
            random_x = random.randint(-340, 340)
            random_y = random.randint(-340, 340)
            self.goto(random_x, random_y)
            self.shape('square')
            self.color('gold')
            self.shapesize(stretch_wid=0.5, stretch_len=0.5)
            self.penup()
            self.speed(0)
            self.energy = food_energy
                
    def destroy(self):
            self.goto(2000,2000)
            self.hideturtle()
            foods.remove(self)
          
class Graph(turtle.Turtle):
   def __init__(self):
            turtle.Turtle.__init__(self)
            self.penup()
            self.goto(400, 0)
            self.speed(0)
            self.pen(pensize=3)
            self.shapesize(stretch_wid=0.5, stretch_len=0.5)
            self.left(90)

class Window(turtle.Turtle):
   def __init__(self):
            turtle.Turtle.__init__(self)
            self.penup()
            self.speed(0)
            self.pen(pensize=3)
            self.shapesize(stretch_wid=0.5, stretch_len=0.5)
            self.left(90)

class Pen(turtle.Turtle):
   def __init__(self):
            turtle.Turtle.__init__(self)
            self.penup()
            self.speed(0)
            self.color("white")
            self.hideturtle()

pen_population = Pen()
pen_population.goto(500,315)

pen_speed = Pen()
pen_speed.goto(500,65)

pen_vision = Pen()
pen_vision.goto(500,-185)
          
def move():
  if not foods:
    for ball in balls:
      random_angle = random.randint(-10, 10)
      ball.right(random_angle)
          
      ball.forward(ball.speed)
      
      ball.energy -= 1
 
  else:
    for food in foods:
      for ball in balls:
        if ball.distance(food) < ball.vision:
            ball.setheading(ball.towards(food.xcor(), food.ycor()))
        else:
            random_angle = random.randint(-10, 10)
            ball.right(random_angle)
            
        ball.forward(ball.speed)
      
        ball.energy -= 1

def check_collission_wall():
    for ball in balls:
        if ball.ycor() > 340:
            ball.sety(340)
            ball.setheading(ball.towards(0,0))
            
        if ball.ycor() < -340:
            ball.sety(-340)
            ball.setheading(ball.towards(0,0))
            
        if ball.xcor() < -340:
            ball.setx(-340)
            ball.setheading(ball.towards(0,0))
        
        if ball.xcor() > 340:
            ball.setx(340)
            ball.setheading(ball.towards(0,0)) 

def check_collission_food():
  for food in foods:
     for ball in balls:
        if ball.distance(food) < 10:
          ball.energy += food.energy
          food.destroy()

def check_round():
    global count
    count += 1
    if count > round_time:
      make_food(number_food)
      
      count = 0
      
def check_reproduction():
   for parent in balls:
         if parent.energy > reproduction_energy:

                  child = Ball()
                  balls.append(child)
                  child.speed = parent.speed + random.uniform(-mutation_speed, mutation_speed)
                  child.vision = parent.vision + random.randint(-mutation_vision, mutation_vision)
                  
                  stats_speed.append(child.speed)
                  stats_vision.append(child.vision)
                  
                  parent.energy -= reproduction_cost

def check_energy():
  for ball in balls:
    if ball.energy < 0:
      ball.destroy()
      
def remove_dead_balls():
  for dead_ball in dead_balls:
      dead_ball.dead_count += 1
      if dead_ball.dead_count > 50:
              dead_ball.goto(2000,2000)
              dead_ball.hideturtle()
              dead_balls.remove(dead_ball)
              
stats_speed = []
stats_vision = []

def show_stats():
  if len(stats_speed) > 0:  
      population_size = str(len(balls)) 
      average_speed = str(round((sum(stats_speed))/(len(stats_speed)),2))
      average_vision = str(round((sum(stats_vision))/(len(stats_vision))))

      pen_population.clear()
      pen_population.write("population:{}".format(population_size), align='center', font=('Courier', 18, 'normal'))
      
      pen_speed.clear()
      pen_speed.write("speed:{}".format(average_speed), align='center', font=('Courier', 18, 'normal'))
      
      pen_vision.clear()
      pen_vision.write("vision:{}".format(average_vision), align='center', font=('Courier', 18, 'normal'))
      
balls = []
def make_balls(number_balls):
   i = 0
   while i < number_balls:
      ball = Ball()
      balls.append(ball)
      
      i += 1

make_balls(number_balls)

foods = []

def make_food(number_food):
   i = 0
   while i < number_food:
      food = Food()
      foods.append(food)
      
      i += 1
      
make_food(number_food)

for ball in balls:
    stats_speed.append(ball.speed)
    stats_vision.append(ball.vision)

show_stats()

def make_window(x,y,size):
    window = Window()
    window.hideturtle()
    window.color("white")
    window.goto(x,y)
    window.pendown()
    window.forward(size)
    window.right(90)
    window.forward(size)
    window.right(90)
    window.forward(size)
    window.right(90)
    window.forward(size)
    window.right(90)

make_window(400, 150, 200)
make_window(400, -100, 200)
make_window(400, -350, 200)
make_window(-350,-350, 700)

x = 400
graph_population_size = Graph()
graph_population_size.color("red")
graph_population_size.shape('square')

graph_average_speed = Graph()
graph_average_speed.color("blue")
graph_average_speed.shape('triangle')

graph_average_vision = Graph()
graph_average_vision.color("green")
graph_average_vision.shape('circle')

count_graph = 0
def make_graph():
    global x
    global count_graph
    
    count_graph += 1
    
    if count_graph == 5:
      x += 1
      
      population_size = (len(balls)+50) 
      average_speed = ((round((sum(stats_speed))/(len(stats_speed)),2))-2)
      average_vision = ((round((sum(stats_vision))/(len(stats_vision))))-200)  
      
      graph_population_size.goto(x, population_size*3)
      graph_population_size.pendown()
      graph_average_speed.goto(x, average_speed*60)
      graph_average_speed.pendown()
      graph_average_vision.goto(x, average_vision*2)
      graph_average_vision.pendown()
      
      count_graph = 0
     
while True:
    wn_main.update()
    check_collission_food()
    check_collission_wall()
    check_reproduction()
    check_energy()
    check_round()
    remove_dead_balls()
    show_stats()
    move()
    make_graph()

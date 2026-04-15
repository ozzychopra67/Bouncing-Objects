
from turtle import*
import random 

# generates a random color
def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

# Creates the rectangular game boundary
def playing_area():
    turt = Turtle()
    turt.speed(0)
    turt.color("white")
    turt.penup()
    turt.goto(250,250)
    turt.pendown()
    turt.begin_fill()
    turt.goto(250,-250)
    turt.goto(-250,-250)
    turt.goto(-250,250)
    turt.goto(250,250)
    turt.end_fill()
    hideturtle()



  

# Function 1: Movement using turtle heading (forward + setheading)
def move_with_heading(turt):
    turt.forward(5)
    if turt.xcor() > 240 or turt.xcor() < -240:
        turt.setheading(180 - turt.heading())
        turt.forward(10)
    if turt.ycor() > 240 or turt.ycor() < -240:
        turt.setheading(-turt.heading())
        turt.forward(10)

        
   

# Function 2: Movement using delta x / delta y (coordinate-based movement)
def move_with_deltas(t, deltax, deltay):
    newx = t.xcor() + deltax
    newy = t.ycor() + deltay

    if newx > 240 or newx < -240:
        newx = t.xcor()
        deltax *= -1 

    if newy > 240 or newy < -240:
        newy = t.ycor() 
        deltay *= -1 
    
    t.goto(newx,newy)

    return deltax, deltay








bg = Screen()
bg.setup(520,520)
bg.bgcolor("black")

playing_area()

t = Turtle()
t.color(generate_color())
t.speed(0)
t.shape("circle")
deltax = random.randint(-2,2)
deltay = random.randint(-2,2)

alive = True 
while alive:
    deltax, deltay = move_with_deltas(t, deltax, deltay)





bg.exitonclick()
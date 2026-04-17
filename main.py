
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
def move_with_heading(turt, turtle_babies):
    turt.forward(5)
    if turt.xcor() > 240 or turt.xcor() < -240:
        turt.setheading(180 - turt.heading())
        turt.forward(10)
        turtle_babies.append(breeding_turtle())
    if turt.ycor() > 240 or turt.ycor() < -240:
        turt.setheading(-turt.heading())
        turt.forward(10)
        turtle_babies.append(breeding_turtle())
    return turtle_babies
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

def breeding_turtle():
    t = Turtle()
    t.color(generate_color())
    t.speed(0)
    t.shape("circle")
    t.setheading(random.randint(0,360))
    turtle_babies.append(t)
    return t

def create_player():
    global player 
    player = Turtle()
    player.speed(0)
    player.color("blue")
    player.shape("turtle")

def up():
    global player 
    player.setheading(90)
    player.sety(player.ycor() + 10)

def down():
    global player 
    player.setheading(0)
    player.sety(player.ycor() - 10)

def left():
    global player 
    player.left(10)
   

def right():
    global player 
    player.right(10)





bg = Screen()
bg.setup(520,520)
bg.bgcolor("black")
bg.listen()
bg.onkey(create_player, "space")
bg.onkeypress(up, "Up")
bg.onkeypress(down, "Down")
bg.onkeypress(left, "Left")
bg.onkeypress(right, "Right")


playing_area()

player = None



t = Turtle()
t.color(generate_color())
t.speed(0)
t.shape("circle")
t.setheading(random.randint(0,360))
deltax = random.randint(-2,2)
deltay = random.randint(-2,2)

turtle_babies = [t]


alive = True 
while alive:
    if player: 
        move_with_heading(player,turtle_babies)
    for obj in turtle_babies:
        turtle_babies = move_with_heading(obj,turtle_babies)
        if player != None and player.distance(obj) < 20: 
            obj.hideturtle()
            turtle_babies.remove(obj)





bg.exitonclick()
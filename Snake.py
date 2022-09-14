import turtle
import time
import random

a = turtle.Screen()
a.setup(width=500, height=500)
a.bgcolor("light sky blue")
a.tracer(0)
head = turtle.Turtle()
head.shape("square")
head.color("sea green")
head.penup()
head.goto(10, 20)
head.direction = "stop"
food = turtle.Turtle()
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(10, 60)
tail = []


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


def upkey():
    head.direction = "up"


def rightkey():
    head.direction = "right"


def downkey():
    head.direction = "down"


def leftkey():
    head.direction = "left"


a.listen()
a.onkey(upkey, "Up")
a.onkey(rightkey, "Right")
a.onkey(downkey, "Down")
a.onkey(leftkey, "Left")

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.goto(0, 200)
pen.write("Score=0, Highest score=0", align="center", font=("Times New Roman", 24, "normal"))
Score = 0
Highest_score = 0
while True:
    a.update()
    time.sleep(0.1)
    if head.xcor() < -250 or head.xcor() > 250:
        head.direction = "stop"
        head.home()
        for t in tail:
            t.hideturtle()
        tail = []
        Score = 0
        pen.clear()
        pen.write("Score={}, Highest score={}".format(Score, Highest_score), align="center",
                  font=("Times New Roman", 24, "normal"))

    if head.ycor() < -250 or head.ycor() > 250:
        head.direction = "stop"
        head.home()
        for t in tail:
            t.hideturtle()
        tail = []
        Score = 0
        pen.clear()
        pen.write("Score={}, Highest score={}".format(Score, Highest_score), align="center",
                  font=("Times New Roman", 24, "normal"))
    if food.distance(head) < 30:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)
        t = turtle.Turtle()
        t.shape("square")
        t.color("lawn green")
        t.penup()
        tail.append(t)
        Score = Score + 10
        if Highest_score < Score:
            Highest_score = Score
        pen.clear()
        pen.write("Score={}, Highest score={}".format(Score, Highest_score), align="center",
                  font=("Times New Roman", 24, "normal"))

    for i in range(len(tail) - 1, 0, -1):
        if i == 0:
            x = head.xcor()
            y = head.ycor()
            tail[i].goto(x, y)
        x = tail[i - 1].xcor()
        y = tail[i - 1].ycor()
        tail[i].goto(x, y)
    if len(tail) > 0:
        x = head.xcor()
        y = head.ycor()
        tail[0].goto(x, y)

    move()
    for y in tail:
        if y.distance(head) < 10:
            head.direction = "stop"
            head.home()
            for t in tail:
                t.hideturtle()
            tail = []
            Score = 0
            pen.clear()
            pen.write("Score={}, Highest score={}".format(Score, Highest_score), align="center",
                      font=("Times New Roman", 24, "normal"))
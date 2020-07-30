# Bouncy Royale v0.1 By Aurick Wong

import turtle
import os

# Variables
sc = turtle.Screen()
rp = turtle.Turtle() 
lp = turtle.Turtle()
ba = turtle.Turtle()
pen = turtle.Turtle()
ba.dx = 0.4
ba.dy = 0.4
p1sc = 0
p2sc = 0

# Window Configuration
sc.title("Bouncy Royale v0.1")
sc.setup(width = 1500, height = 800)
sc.bgcolor("black")
sc.tracer(0)

# Ball
ba.shape("circle")
ba.color("orange")
ba.goto(0, 0)
ba.speed(0)
ba.penup()

# rp - right Paddle
rp.speed(0)
rp.shape("square")
rp.color("blue")
rp.shapesize(stretch_wid=6 ,stretch_len=1)
rp.penup()
rp.goto(700, 0)

# lp Left Paddle
lp.speed(0)
lp.shape("square")
lp.color("red")
lp.shapesize(stretch_wid=6 ,stretch_len=1)
lp.penup()
lp.goto(-700, 0)

# Pen - score board
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Aliment", 24, "normal"))

# Functions
def rp_up():
    y = rp.ycor()
    y += 20
    rp.sety(y)
def lp_up():
    y = lp.ycor()
    y += 20
    lp.sety(y)
def rp_down():
    y = rp.ycor()
    y -= 20
    rp.sety(y)
def lp_down():
    y = lp.ycor()
    y -= 20
    lp.sety(y)

# keybinding
sc.listen()
sc.onkeypress(lp_up, "w")
sc.onkeypress(lp_down, "s")
sc.onkeypress(rp_up, "Up")
sc.onkeypress(rp_down, "Down")

# Game Core
while True:
    sc.update()
    
    # Ball movement
    ba.setx(ba.xcor() + ba.dx)
    ba.sety(ba.ycor() + ba.dy)
    
    # Top and bottom
    if ba.ycor() > 390:
        ba.sety(390)
        ba.dy *= -1
    
    elif ba.ycor() < -390:
        ba.sety(-390)
        ba.dy *= -1

    # Paddle and ball collisions
    if ba.xcor() < -680 and ba.ycor() < lp.ycor() + 50 and ba.ycor() > lp.ycor() - 50:
        ba.dx *= -1 
       
    elif ba.xcor() > 680 and ba.ycor() < rp.ycor() + 50 and ba.ycor() > rp.ycor() - 50:
        ba.dx *= -1
    
    # Left and right
    if ba.xcor() > 750:
        pen.clear()
        p1sc += 1
        pen.write("Player A: {}  Player B: {}".format(p1sc, p2sc), align="center", font=("Aliment", 24, "normal"))
        ba.dx *= -1
        ba.goto(0, 0)
    
    elif ba.xcor() < -750:
        p2sc += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(p1sc, p2sc), align="center", font=("Aliment", 24, "normal"))
        ba.goto(0, 0)
        ba.dx *= -1

   

    
#from turtle import *
import turtle
from random import randint

window = turtle.Screen()
window.title("Ping Pong")
window.setup(width=1.0, height=1.0)
window.bgcolor("black")
window.tracer(2)



border = turtle.Turtle()
border.speed(0)
border.color("green")
border.begin_fill()
border.goto(-500, 300)
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()

border.goto(0, 300)
border.color("white")
border.setheading(270)
for i in range(25):
	if i % 2 == 0:
		border.forward(24)
	else:
		border.up()
		border.forward(24)
		border.down()
border.hideturtle()

rocket_a = turtle.Turtle()
rocket_a.color("white")
rocket_a.shape("square")
rocket_a.shapesize(stretch_len=1, stretch_wid=5)
rocket_a.penup();
rocket_a.goto(-450, 0)

def move_up():
	y = rocket_a.ycor() + 10
	if y > 250:
		y = 250
	rocket_a.sety(y)

def move_down():
	y = rocket_a.ycor() - 10
	if y < -250:
		y = -250
	rocket_a.sety(y) 

rocket_b = turtle.Turtle()
rocket_b.color("white")
rocket_b.shape("square")
rocket_b.shapesize(stretch_len=1, stretch_wid=5)
rocket_b.penup();
rocket_b.goto(450, 0)

def move_up_b():
	y = rocket_b.ycor() + 10
	if y > 250:
		y = 250
	rocket_b.sety(y)

def move_down_b():
	y = rocket_b.ycor() - 10
	if y < -250:
		y = -250
	rocket_b.sety(y)

ball = turtle.Turtle()
ball.shape("circle")
ball.dx = 3
ball.dy = -3
ball.speed(0)
ball.color("red")
ball.penup()
 
window.listen()
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_up_b, "Up")
window.onkeypress(move_down_b, "Down")

while True:
	window.update()

	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	if ball.ycor() >= 290:
		ball.dy = -ball.dy

	if ball.ycor() <= -290:
		ball.dy = -ball.dy

	if ball.xcor() >= 490:
		ball.goto(0, randint(-150, 150))

	if ball.xcor() <= -490:
		ball.goto(0, randint(-150, 150))
		

	if ball.ycor() >= rocket_b.ycor() - 50 and ball.ycor() <= rocket_b.ycor() + 50 \
		and ball.xcor() >= rocket_b.xcor() - 5 and ball.xcor() <= rocket_b.xcor() + 5:
		ball.dx = -ball.dx

	if ball.ycor() >= rocket_a.ycor() - 50 and ball.ycor() <= rocket_a.ycor() + 50 \
		and ball.xcor() >= rocket_a.xcor() - 5 and ball.xcor() <= rocket_a.xcor() + 5:
		ball.dx = -ball.dx
 
window.mainloop()














































# import os
# import turtle as t
# playerAscore = 0
# playerBscore = 0

# window = t.Screen()
# window.title("The Ping Game")
# window.bgcolor("lightgreen")
# window.setup(width = 800,height = 600)
# window.tracer(8,25)

# #Left Paddle
# leftpaddle = t.Turtle()
# leftpaddle.speed()
# leftpaddle.shape("square")
# leftpaddle.color("white")
# leftpaddle.shapesize(stretch_wid = 5, stretch_len = 1)
# leftpaddle.penup()
# leftpaddle.goto(-350, 0)

# #Right Paddle
# rightpaddle = t.Turtle()
# rightpaddle.speed()
# rightpaddle.shape("square")
# rightpaddle.color("white")
# rightpaddle.shapesize(stretch_wid = 5, stretch_len = 1)
# rightpaddle.penup()
# rightpaddle.goto(350, 0)

# #Ball
# ball = t.Turtle()
# ball.speed(0)
# ball.shape("circle")
# ball.color("yellow")
# ball.penup()
# ball.goto(5, 5)
# ballxdirection = 0.2
# ballydirection = 0.2

# #Score Card
# pen = t.Turtle()
# pen.speed(0)
# pen.color("blue")
# pen.penup()
# pen.hideturtle()
# pen.goto(0, 260)
# pen.write("score", align = "center", font = ('Arial', 24, 'normal'))

# #Moving Left Paddle
# def leftpaddleup():
# 	y = leftpaddle.ycor()
# 	y = y + 90
# 	leftpaddle.sety(y)

# def leftpaddledown():
# 	y = leftpaddle.ycor()
# 	y = y + 90
# 	leftpaddle.sety(y)

# #Moving Right Paddle
# def rightpaddleup():
# 	y = rightpaddle.ycor()
# 	y = y + 90
# 	rightpaddle.sety(y)

# def rightpaddledown():
# 	y = rightpaddle.ycor()
# 	y = y + 90
# 	rightpaddle.sety(y)

# #Assign Key to Play
# window.listen()
# window.onkeypress(leftpaddleup, 'w')
# window.onkeypress(leftpaddledown, 's')
# window.onkeypress(rightpaddleup, 'Up')
# window.onkeypress(rightpaddledown, 'Down')

# while True:
# 	window.update()

# 	#move the ball
# 	ball.setx(ball.xcor() + ballxdirection)
# 	ball.sety(ball.ycor() + ballydirection)

# 	#border set up
# 	if ball.ycor() > 290:
# 		ball.sety(290)
# 		ballydirection = ballydirection * -1
# 	if ball.ycor() < -290:
# 		ball.sety(-290)
# 		ballydirection = ballydirection * -1

# 	if ball.xcor() > 390:
# 		ball.goto(0,0)
# 		ball_dx = ball_dx * -1
# 		player_a_score = player_a_score + 1
# 		pen.clear()
# 		pen.write("Player A: {}						Player B: {} ".format(player_a_score, player_b_score), align = "center", font = ('Monaco', 24, "normal"))
# 		os.system("afplay wallhit.wav&")

# 	if(ball.xcor()) < -390: # Left width paddle Border
# 		ball.goto(0,0)
# 		ball_dx = ball_dx * -1
# 		player_b_score = player_b_score + 1
# 		pen.clear()
# 		pen.write("Player A: {}                    Player B: {} ".format(player_a_score, player_b_score), align="center",font=('Monaco', 24, "normal"))
# 		os.system("afplay wallhit.wav&")

# 	if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
# 		ball.setx(340)
# 		ball_dx = ball_dx * -1
# 		os.system("afplay paddle.wav&")
		
# 	if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
# 		ball.setx(-340)
# 		ball_dx = ball_dx * -1
# 		os.system("afplay paddle.wav&")
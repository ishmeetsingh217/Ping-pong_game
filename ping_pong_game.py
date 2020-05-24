import turtle
import os

window = turtle.Screen()
window.title("Ping Pong")  # Add tile for the window
window.bgcolor("black")   # Give the background color to the screen
window.setup(width=800, height=600)  # Adjust the size of the screen
window.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
# set the speed for the paddle to maximum else everything will be slow
paddle_a.speed(0)
# gives paddle a shape, we can use square or circle or any other build in shape
paddle_a.shape("square")
paddle_a.color("white")
# Adjust the size of the paddle
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
# Adjust the coordinates for the padle to be on left side of screen
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
# set the speed for the paddle to maximum else everything will be slow
paddle_b.speed(0)
# gives paddle a shape, we can use square or circle or any other build in shape
paddle_b.shape("square")
paddle_b.color("white")
# Adjust the size of the paddle
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
# Adjust the coordinates for the padle to be on left side of screen
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
# set the speed for the paddle to maximum else everything will be slow
ball.speed(0)
# gives paddle a shape, we can use square or circle or any other build in shape
ball.shape("square")
ball.color("white")
ball.penup()
# Adjust the coordinates for the padle to be on left side of screen
ball.goto(0, 0)
ball.dx = 2  # every time the ball moves it moves by 2px
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()  # lines will not be drawn
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center",
          font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()  # returns the y coordinate
    y += 20              # Change the location for paddle
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()  # returns the y coordinate
    y -= 20              # Change the location for paddle
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()  # returns the y coordinate
    y += 20              # Change the location for paddle
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()  # returns the y coordinate
    y -= 20              # Change the location for paddle
    paddle_b.sety(y)


# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")  # perform the function when key is pressed
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    window.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b),
                  align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b),
                  align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

import turtle

# Window
wd = turtle.Screen()
wd.title("PONG GAME")
wd.bgcolor("blue")
wd.setup(width=800, height=600)
wd.tracer(0)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball_x = 0.5
ball_y = 0.5

# Paddle_A
paddle_A = turtle.Turtle()
paddle_A.shape("square")
paddle_A.color("black")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350, 0)

# Paddle_B
paddle_B = turtle.Turtle()
paddle_B.shape("square")
paddle_B.color("black")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(350, 0)

# score
sboard = turtle.Turtle()
sboard.shape("square")
sboard.color("red")
sboard.penup()
sboard.hideturtle()
sboard.goto(0, 260)
sboard.write(
    "Player 1: 0         Player 2: 0", align="center", font=("Bold", 24, "normal")
)

score_a = 0
score_b = 0


# Functions
def paddle_A_up():
    y = paddle_A.ycor()
    y += 30
    paddle_A.sety(y)


def paddle_A_down():
    y = paddle_A.ycor()
    y -= 30
    paddle_A.sety(y)


def paddle_B_up():
    y = paddle_B.ycor()
    y += 30
    paddle_B.sety(y)


def paddle_B_down():
    y = paddle_B.ycor()
    y -= 30
    paddle_B.sety(y)


def menu():
    import SI.py

    SI.py.game_intro()


# Keyboard Bindings
wd.listen()
wd.onkeypress(paddle_A_up, "w")
wd.onkeypress(paddle_A_down, "s")
wd.onkeypress(paddle_B_up, "Up")
wd.onkeypress(paddle_B_down, "Down")


def game():
    global score_a
    global score_b
    global ball
    global ball_y
    global ball_x
    global sboard
    global menu
    run = True
    while run:
        wd.update()

        wd.listen()
        if wd.onkeypress(menu, "Escape"):
            run = False

        # BAll movement
        ball.setx(ball.xcor() + ball_x)
        ball.sety(ball.ycor() + ball_y)

        # Border
        if ball.ycor() > 290:
            ball.sety(290)
            ball_y *= -1
        elif ball.ycor() < -290:
            ball.sety(-290)
            ball_y *= -1

        # score
        if ball.xcor() > 350:
            score_a += 1
            sboard.clear()
            sboard.write(
                "Player 1: {}       Player 2: {}".format(score_a, score_b),
                align="center",
                font=("Bold", 24, "normal"),
            )
            ball.goto(0, 0)
            ball_x *= -1
        elif ball.xcor() < -350:
            score_b += 1
            sboard.clear()
            sboard.write(
                "Player 1: {}       Player 2: {}".format(score_a, score_b),
                align="center",
                font=("Bold", 24, "normal"),
            )
            ball.goto(0, 0)
            ball_x *= -1

        # Collision with bars
        if (
            ball.xcor() < -340
            and ball.ycor() < paddle_A.ycor() + 50
            and ball.ycor() > paddle_A.ycor() - 50
        ):
            ball_x *= -1
        elif (
            ball.xcor() > 340
            and ball.ycor() < paddle_B.ycor() + 50
            and ball.ycor() > paddle_B.ycor() - 50
        ):
            ball_x *= -1


game()

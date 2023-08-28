import random
import time
import turtle

# Set up the screen
window = turtle.Screen()
window.title("Block Breaker Game")
window.bgcolor("black")
window.setup(width=800, height=600)

# window.tracer(0)

# Create the paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=10)
paddle.penup()
paddle.goto(0, -250)

# Create the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

colors = ['orange', 'red', 'purple', 'skyblue', 'turquoise', 'green']

# Create blocks
blocks = []
for _ in range(100):
    block = turtle.Turtle()
    block.penup()
    block.speed(0)
    block.shape("square")
    block.color(random.choice(colors))
    block.shapesize(stretch_len=4)
    # block.penup()
    blocks.append(block)

# Position blocks
# for i, block in enumerate(blocks):
#     x = -180 + i * 80
#     y = 200
#     block.goto(x, y)

for i in range(10):
    for j in range(10):
        x = -360 + j * 80
        y = 290 - i * 20
        blocks[i*10 + j].goto(x, y)


# Move the paddle
def move_paddle_left():
    x = paddle.xcor()
    x -= 20
    if x < -350:
        x = -350
    paddle.setx(x)


def move_paddle_right():
    x = paddle.xcor()
    x += 20
    if x > 350:
        x = 350
    paddle.setx(x)


# Keyboard bindings
window.listen()
window.onkeypress(move_paddle_left, "Left")
window.onkeypress(move_paddle_right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    spd = 1
    time.sleep(0.1//spd)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball and wall collisions
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Ball and paddle collision
    if ball.ycor() < -240 and -100 < ball.xcor() - paddle.xcor() < 100:
        ball.sety(-240)
        ball.dy *= -1

    # Ball misses the paddle and game is lost
    if ball.ycor() < -260:
        ball.goto(0, 0)
        loss = turtle.Turtle()
        loss.penup()
        loss.goto(0, 0)
        loss.color('white')
        loss.pendown()
        loss.write("You Lost", align="center", font=("Courier", 80, "normal"))
        game_is_on = False

    # Ball and block collision
    for block in blocks:
        if (block.ycor() + 20 > ball.ycor() > block.ycor() - 20) and (block.xcor() + 40 > ball.xcor() > block.xcor() - 40):
            blocks.remove(block)
            block.hideturtle()
            ball.dy *= -1

    if len(blocks) == 0:
        ball.goto(0, 0)
        ball.dy *= -1
        end = turtle.Turtle()
        end.penup()
        end.goto(0, 0)
        end.color('white')
        end.pendown()
        end.write("You Won", align="center", font=("Courier", 80, "normal"))
        game_is_on = False

    spd += 1

# Close the game window on click
window.exitonclick()
# window.bye()

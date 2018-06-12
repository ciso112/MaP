import my_turtle
import math

turtle = my_turtle.Turtle()
turtle.turtle(900, 900, 400, 400)


def star(turtle, n, d):
    for i in range(n):
        # turtle.canvas.show()
        turtle.forward(d)
        if n % 2 == 1:
            turtle.left(180 - 180 / n)
        elif n % 4 == 0:
            turtle.left(180 - 360 / n)
        else:
            turtle.left(180 - 720 / n)


def plant(turtle, depth, length):
    if depth > 0:
        turtle.forward(length)
        turtle.left(45)
        plant(turtle, depth - 1, length / 2)
        turtle.right(90)
        plant(turtle, depth - 1, length / 2)
        turtle.left(45)
        turtle.forward(-length)


def koch_curve(turtle, depth, length):
    if depth == 0:
        turtle.forward(length)
    else:
        koch_curve(turtle, depth - 1, length / 2)
        turtle.left(60)
        koch_curve(turtle, depth - 1, length / 2)
        turtle.right(120)
        koch_curve(turtle, depth - 1, length / 2)
        turtle.left(60)
        koch_curve(turtle, depth - 1, length / 2)


def koch_snowflake(depth, length):
    for i in range(3):
        koch_curve(turtle, depth, length)
        turtle.right(120)


def squares(turtle, n, d, ratio):
    for i in range(n):
        turtle.polygon(4, d)
        turtle.forward(d * (1 - ratio))
        turtle.left(math.atan((1 - ratio) / ratio) * 180 / math.pi)
        d = math.sqrt(math.pow(d * ratio, 2) + math.pow(d * (1 - ratio), 2))


# move constant not correct, relative distance is getting smaller
def triangles(turtle, n, d):
    for i in range(n):
        move = d / math.sqrt(3) / n
        turtle.polygon(3, d)
        turtle.left(30)
        turtle.pen_up()
        turtle.forward(move)
        turtle.pen_down()
        turtle.right(30)
        d = d - (d / n)
        # print d


def polygon_flower(turtle, n, d):
    for i in range(n):
        turtle.polygon(n, d)
        turtle.left(360 / n)


def sierp_triangle(turtle, depth, d):
    turtle.draw_part(depth, d)
    turtle.right(120)
    turtle.forward(d)
    for i in range(3):
        turtle.left(120)
        turtle.forward(d * 2)


def draw_part(turtle, depth, d):
    if depth <= 0:
        return
    for i in range(3):
        turtle.forward(d / 2)
        turtle.insert_part(depth, d)
        turtle.forward(d / 2)
        turtle.right(120)


def insert_part(turtle, depth, d):
    turtle.left(120)
    turtle.draw_part(depth - 1, d / 2)
    turtle.right(120)



turtle.canvas.show()
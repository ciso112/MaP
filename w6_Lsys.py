import my_turtle

turtle = my_turtle.Turtle()
turtle.turtle(900, 900, 400, 400)

# ### C L-systems ###

def iterate(axiom, num, initator):

    def translate(current, axiom):

        result = ''
        consts = {'+', '-', '[', ']'}
        for c in current:
            if c in consts:
                result += c
                continue
            if c == 'F':
                result += axiom
        return result

    result = initator
    for i in range(0, num):
        result = translate(result, axiom)
    return result

# a - angle; l - length
def draw(axiom, a, l):

    turtle.left(90)

    for i in range(len(axiom)):
        c = axiom[i]

        if c == 'F':
            turtle.forward(l)

        elif c == 'f':
            turtle.pen_up()
            turtle.forward(l)
            turtle.pen_down()

        elif c == '+':
            turtle.left(a)

        elif c == '-':
            turtle.right(a)

        elif c == '[':
            turtle.push()

        elif c == ']':
            heading, position = turtle.stack.pop()
            turtle.pen_up()
            turtle.go_to(position[0], position[1])
            turtle.set_angle(heading)
            turtle.pen_down()


axiom = "F[-F]F[+F]F"
axiom = iterate(axiom, 3, "F")
draw(axiom, 60, 10)
turtle.canvas.show()


from PIL import Image, ImageDraw
import itertools
import math

width = 600
height = width
canvas = Image.new('RGBA', (width, height), "white")
draw = ImageDraw.Draw(canvas)



# ### D GCD Visualization ###

# steps for subtraction method
stepssub = 0

# steps for mod method
steps = 0

# recursive function - steps variable set to zero at the first call (by a user)
def gcdmod(a, b, user):
    global steps
    if user:
        steps = 0
    steps += 1

    if b == 0:
        return a
    else:
        return gcdmod(b, a % b, False)


def gcdsub(a, b, user):
    global stepssub
    if user:
        stepssub = 0
    stepssub += 1

    if a == b:
        return a
    if a > b:
        return gcdsub(a - b, b, False)
    else:
        return gcdsub(a, b - a, False)

# gcd ratio between numbers
def ratio():
    for i in range(1, width):
        for j in range(1, height):
            draw.point((i, height - j), fill=(gcdsub(i, j, False) * 255 / min(i, j), 125, 255))

# searching for gcd with subtraction method - more steps
def subst():
    for i in range(1, width):
        for j in range(1, height):
            gcdsub(i, j, True)
            # print stepssub
            draw.point((i, height - j), fill=(0, stepssub, 255))

# searching for gcd with modulo method - fewer steps
def modulo():
    for i in range(1, width):
        for j in range(1, height):
            gcdmod(i, j, True)
            # print steps
            draw.point((i, height - j), fill=(0, 125 - steps, 55))


# canvas.show()













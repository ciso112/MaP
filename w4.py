from PIL import Image, ImageDraw
import math

width = 600
height = 600
canvas = Image.new('RGBA', (width, height), "white")
draw = ImageDraw.Draw(canvas)

#  a, b - starting position, r - radius
def circle(a, b, r, filled):
    if filled:
        # iterate over points of canvas
        for i in range(width):
            for j in range(height):
                if math.pow(j-a, 2) + math.pow(i-b, 2) < math.pow(r, 2):
                    draw.point((i, j), fill='red')
    else:
        i = 0.0
        while i < math.pi * 2:
            x = a + math.cos(i) * r
            y = b + math.sin(i) * r
            draw.point((x, y), fill='red')
            i += 1 / r

#  a, b - starting position, r - radius
def spiral(a, b, r, e, spins):
    bound = spins * math.pi * 2
    i = 0.0
    while i < bound:
        x = math.cos(i) * r * (i / bound) + a
        y = math.sin(i) * r * (i / bound) + b
        #constant in a B color component set experimentally for nicest visual
        color = (int(x), int(y), int(i * 3))
        draw.point((x, y), fill=color)
        i += e


def triangle(a):
    x = (0, a, a / 2)
    y = (0, 0, math.sqrt(3) / 2 * a)
    tr_height = math.sqrt(3) / 2 * a

#  a, b - starting position, r1, r2 - radius
def ellipse(a, b, r1, r2, rotation):

    for i in range(width):
        for j in range(height):
            if math.pow((j-a) * math.cos(rotation) - (i-b) * math.sin(rotation), 2) / r1 \
                    + math.pow((j-a) * math.sin(rotation) + (i-b) * math.cos(rotation), 2) / r2 \
                    <= 1:
                draw.point((i, j), fill='red')

# n - ribbs density, r - radius
def ribbed_circle(n, r):
    for i in range(2 * r):
        for j in range(2 * r):
            if math.sqrt((j - r) * (j - r) + (i - r) * (i - r)) <= r and (j % n == 0 or i % n == 0):
                draw.point((i, j), fill='black')


# circle(150, 150, 100.0, True)
# spiral(200, 200, 150, 0.01, 8)
# ellipse(200, 200, 200, 400, 0.5)
# ribbed_circle(15, 75)

canvas.show()

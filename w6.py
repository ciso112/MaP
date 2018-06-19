from PIL import Image, ImageDraw
from random import choice

width = 300
height = 300
canvas = Image.new('RGBA', (width, height), "white")
draw = ImageDraw.Draw(canvas)

# ### A Chaos game ###

def midpoint(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def chaos(corners, start_point, steps=10000):

    prev_point = start_point
    for _ in range(steps):
        # Select the next guider to move closer to
        corner = choice(corners)
        new_point = midpoint(prev_point, corner)
        # print new_point
        draw.point(new_point, fill='black')
        prev_point = new_point

start_point = (150.0, 150.0)
# corners = [(100.0, 100.0),
#            (200.0, 100.0),
#            (200.0, 200.0),
#            (100.0, 200.0)]
corners = [(100.0, 100.0),
           (200.0, 100.0),
           (150.0, 250.0)]
chaos(corners, start_point)
canvas.show()


# ### B Feigenbaum ###

def feigenbaum_diagram():
    xa = 2.9
    xb = 4.0
    maxit = 1000

    for i in range(width):
        r = xa + (xb - xa) * i / (width - 1)
        x = 0.5
        for j in range(maxit):
            x = r * x * (1 - x)
            if j > maxit / 2:
                draw.point((i, int(x * height)), fill='blue')
    canvas.show()

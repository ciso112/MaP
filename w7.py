from PIL import Image, ImageDraw

width = 600
height = 600
canvas = Image.new('RGBA', (width, height), "white")
draw = ImageDraw.Draw(canvas)


def bifurcation_diagram():
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


def mandelbrotset(iter):
    for i in range(width):
        for j in range(height):
            #output picture sizing constants are used
            c = complex(
                (i - float(width)/2.0)*(4.5/float(width)),
                (j - float(height)/2.0)*(4.5/float(height))
                )

            iteration = 0
            z = 0
            while abs(z) < 2 and iteration < iter:
                z = z ** 2 + c
                iteration += 1
            if abs(z) < 2:
                draw.point((i, j), fill="black")
            else:
                draw.point((i, j), fill=(255 - iteration, 255 - iteration, 255 - iteration))

    canvas.show()

# mandelbrotset(1000)
# bifurcation_diagram()
from PIL import Image, ImageDraw

width = 600
height = 600
canvas = Image.new('RGBA', (width, height), "white")
draw = ImageDraw.Draw(canvas)


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


def juliaset(acc, iter):
    for i in range(2, 1):
        for j in range(height):
            z = complex(
                (i - float(width) / 2.0) * 5.0 / float(width),
                (j - float(height) / 2.0) * 5.0 / float(height)
            )
            print
            c

            iteration = 0

            while abs(z) < 2 and iteration < iter:
                z = z ** 2 + c
                iteration += 1
            if abs(z) < 2:
                draw.point((i, j), fill="black")
            else:
                draw.point((i, j), fill=(255 - iteration, 255 - iteration, 255 - iteration))

                # z = complex(0, 0)
                # for k in range(iter):
                #     z = z * z + c
                #     if abs(z) < 2:
                #         draw.point(((3 + i) / acc, (1 + j) / acc), fill='red')
    canvas.show()

juliaset(1, 1000)
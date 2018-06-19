from PIL import Image, ImageDraw
import math
import random

width = 600
height = 600
canvas = Image.new('RGBA', (width, height), "white")
draw = ImageDraw.Draw(canvas)

# ### A Lines intersections ###

x_coord = []
y_coord = []


def random_number(min, max):
    return random.randint(min, max)


def random_points(min, max, n):
    points = []
    for i in range(n):
        point = random_number(min, max)
        points.append(point)
    return points


def generate_lines(n, length):
    # generate N random points of length between 0 to width, resp. height
    x1 = random_points(0, width, n)
    y1 = random_points(0, height, n)

    x2 = -1
    y2 = -1

    for i in range(n):
        # randomly generate remaining points to have all line coordinates
        while x2 < 0 or x2 > width or y2 < 0 or y2 > height:
            angle = random_number(0, 360)
            x2 = x1[i] + math.sin(angle) * length
            y2 = x1[i] + math.cos(angle) * length
        # append x coordinates of start and end
        x_coord.append(x1[i])
        x_coord.append(int(x2))
        # append y coordinates of start and end
        y_coord.append(y1[i])
        y_coord.append(int(y2))
        # line(start: x1, y1; end: x2, y2)
        draw.line((x1[i], y1[i], x2, y2), fill=120)
        x2 = -1
    print x_coord
    print y_coord


def find_intersections():
    print len(x_coord) - 2
    for i in range(0, len(x_coord) - 4, 2):
        for j in range(0, len(y_coord) - 4, 2):
            print 'j: %d' %(j)
            print y_coord[2 * j + 3]
            print y_coord[2 * i]
            denominator = (x_coord[2 * i] - x_coord[2 * i + 1]) * (y_coord[2 * j] - y_coord[2 * j + 1])\
                          - (y_coord[2 * i] - y_coord[2 * i + 1]) * (x_coord[2 * j] - x_coord[2 * j + 1])
            print 'denom %d' %(denominator)
            if denominator and y_coord[2 * j + 3]:
                Px = ((x_coord[2 * i] * y_coord[2 * j + 1] - y_coord[2 * j] * x_coord[2 * i + 1])
                      * (x_coord[2 * i + 2] - x_coord[2 * i + 3]) - (x_coord[2 * i] - x_coord[2 * i + 1])
                      * (x_coord[2 * i + 2] * y_coord[2 * j + 3] - y_coord[2 * j + 2] * x_coord[2 * i + 3]))\
                     / denominator
                Py = ((x_coord[2 * i] * y_coord[2 * j + 1] - y_coord[2 * i] * x_coord[2 * i + 1])
                      * (y_coord[2 * j + 2] - y_coord[2 * j + 3]) - (y_coord[2 * i] - y_coord[2 * i + 1])
                      * (x_coord[2 * j + 2] * y_coord[2 * j + 3] - y_coord[2 * j + 2] * x_coord[2 * j + 3]))\
                     / denominator
                print 'Px = %d' %(Px)
                # print Py
            else:
                Px = Py = 0

            if (Px >= min(x_coord[2 * i], x_coord[2 * i + 1])) and (Px <= max(x_coord[2 * i], x_coord[2 * i + 1])) and \
                (Py >= min(y_coord[2 * i], y_coord[2 * i + 1])) and (Py <= max(y_coord[2 * i], y_coord[2 * i + 1])) and \
                (Px >= min(x_coord[2 * j], x_coord[2 * j + 1])) and (Px <= max(x_coord[2 * j], x_coord[2 * j + 1])) and \
                (Py >= min(y_coord[2 * j], y_coord[2 * j + 1])) and (Py <= max(y_coord[2 * j], y_coord[2 * j + 1])):
                draw.ellipse((Px,Px + 5, Py, Py + 10), fill='red')



generate_lines(20, 80)
find_intersections()
canvas.show()

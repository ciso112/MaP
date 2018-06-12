from PIL import Image, ImageDraw
import math
import random

width = 600
height = 600
canvas = Image.new('RGBA', (width, height), "white")
draw = ImageDraw.Draw(canvas)
x = []
y = []


def random_number(min, max):
    return random.randint(min, max)


def random_points(min, max, n):
    points = []
    for i in range(n):
        point = random_number(min, max)
        points.append(point)
    return points


def generate_lines(n, length):
    x1 = random_points(0, width, n)
    y1 = random_points(0, height, n)
    x2 = -1
    y2 = -1

    for i in range(n):
        while x2 < 0 or x2 > width or y2 < 0 or y2 > height:
            angle = random_number(0, 360)
            x2 = x1[i] + math.sin(angle * math.pi / 180) * length
            y2 = x1[i] + math.cos(angle * math.pi / 180) * length
        x.append(x1[i])
        x.append(x2)
        y.append(y1[i])
        y.append(y2)
        draw.line((x1[i], y1[i], x2, y2), fill=120)
        x2 = -1


def find_intersections():

    for i in x[:len(x) / 2]:
        for j in y[:len(y) / 2]:
            denominator = (x[i] - x[i + 1]) * (y[j] - y[2 * j + 1]) - (y[2 * i] - y[2 * i + 1]) \
                * (x[2 * j] - x[2 * j + 1])
            Px = ((x[2 * i] * y[2 * i + 1] - y[2 * i] * x[2 * i + 1]) * (x[2 * j] - x[2 * j + 1]) \
                - (x[2 * i] - x[2 * i + 1]) * (x[2 * j] * y[2 * j + 1] - y[2 * j] * x[2 * j + 1])) / denominator
            Py = ((x[2 * i] * y[2 * i + 1] - y[2 * i] * x[2 * i + 1]) * (y[2 * j] - y[2 * j + 1]) \
                  - (y[2 * i] - y[2 * i + 1]) * (x[2 * j] * y[2 * j + 1] - y[2 * j] * x[2 * j + 1])) / denominator

            if (Px >= math.Min(x[2 * i], x[2 * i + 1])) and (Px <= math.Max(x[2 * i], x[2 * i + 1])) and \
                (Py >= math.Min(y[2 * i], y[2 * i + 1])) and (Py <= math.Max(y[2 * i], y[2 * i + 1])) and \
                (Px >= math.Min(x[2 * j], x[2 * j + 1])) and (Px <= math.Max(x[2 * j], x[2 * j + 1])) and \
                (Py >= math.Min(y[2 * j], y[2 * j + 1])) and (Py <= math.Max(y[2 * j], y[2 * j + 1])):
                draw.circle(Px, Py, 2)

        # for i in x[:]:
        #     for j in y[:]:
        #         denominator = (x[i] - x[i + 1]) * (y[j] - y[2 * j + 1]) - (y[2 * i] - y[2 * i + 1]) \
        #                                                                   * (x[2 * j] - x[2 * j + 1])
        #         Px = ((x[2 * i] * y[2 * i + 1] - y[2 * i] * x[2 * i + 1]) * (x[2 * j] - x[2 * j + 1]) \
        #               - (x[2 * i] - x[2 * i + 1]) * (
        #               x[2 * j] * y[2 * j + 1] - y[2 * j] * x[2 * j + 1])) / denominator
        #         Py = ((x[2 * i] * y[2 * i + 1] - y[2 * i] * x[2 * i + 1]) * (y[2 * j] - y[2 * j + 1]) \
        #               - (y[2 * i] - y[2 * i + 1]) * (
        #               x[2 * j] * y[2 * j + 1] - y[2 * j] * x[2 * j + 1])) / denominator
        #
        #         if (Px >= math.Min(x[2 * i], x[2 * i + 1])) and (Px <= math.Max(x[2 * i], x[2 * i + 1])) and \
        #                 (Py >= math.Min(y[2 * i], y[2 * i + 1])) and (
        #             Py <= math.Max(y[2 * i], y[2 * i + 1])) and \
        #                 (Px >= math.Min(x[2 * j], x[2 * j + 1])) and (
        #             Px <= math.Max(x[2 * j], x[2 * j + 1])) and \
        #                 (Py >= math.Min(y[2 * j], y[2 * j + 1])) and (Py <= math.Max(y[2 * j], y[2 * j + 1])):
        #             draw.circle(Px, Py, 2)


generate_lines(20, 80)
find_intersections()
canvas.show()

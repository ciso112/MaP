from PIL import Image, ImageDraw
import math


class Turtle:
    x = 0
    y = 0
    angle = 0
    pen = True

    width = None
    height = None
    canvas = None
    draw = None

    stack = []

    def turtle(self, width, height, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.angle = 0
        self.stack = []

        self.width = width
        self.height = height
        self.canvas = Image.new('RGBA', (width, height), "white")
        self.draw = ImageDraw.Draw(self.canvas)

    def pen_up(self):
        self.pen = False

    def pen_down(self):
        self.pen = True

    def push(self):
        self.stack.append((self.angle, self.position()))

    def pop(self):
        return self.stack.pop()

    def go_to(self, x, y):
        self.x = x
        self.y = y

    def position(self):
        return self.x, self.y

    def set_angle(self, angle):
        self.angle = angle

    def angle(self):
        return self.angle

    def forward(self, distance):
        orig_x = self.x
        orig_y = self.y
        self.x += math.cos(self.angle * math.pi / 180) * distance
        self.y += math.sin(self.angle * math.pi / 180) * distance
        if self.pen:
            self.draw.line((orig_x, orig_y, self.x, self.y), fill=255)

    def left(self, angle):
        self.angle = (self.angle - angle) % 360

    def right(self, angle):
        self.angle = (self.angle + angle) % 360

    def polygon(self, n, d):
        for i in range(n):
            self.forward(d)
            self.left(360 / n)

from PIL import Image, ImageDraw
import math

width = 600
height = 600
canvas = Image.new('RGBA', (width, height), "white")
draw = ImageDraw.Draw(canvas)

# ### 2D Transformations ###

orig = [[200, 300, 300, 200],
    [200, 200, 300, 300]]

class Transformations:

    # x - matrix, type - type of transformation, c - coeficient
    def transform(self, orig, type, coef):
        if type == 'resize':
            change = [[coef, 0], [0, coef]]
        elif type == 'reflexion':
            change = [[- 1, 0], [0, 1]]
        elif type == 'rotate':
            angle = (coef / 180.0) * math.pi
            change = [[math.cos(angle), - math.sin(angle)], [math.sin(angle), math.cos(angle)]]
        elif type == 'sheer':
            change = [[1, coef], [0, 1]]
        else:
            print 'Not a valid transformation'
            # break

        trans = [[0 for _ in range(len(orig[0]))] for _ in range(len(change))]
        for i in range(len(change)):
            for j in range(len(orig[0])):
                for k in range(len(change)):
                    # if i == j == 0 or (i == 1 and j == 0) :
                    #     c[i][j] = x[i][j]
                    # else:
                    trans[i][j] += change[i][k] * orig[k][j]

        return trans

    @staticmethod
    def draw_square(orig):
        j = 0
        while j < len(orig[0]) - 1:
            draw.line((orig[0][j], orig[1][j], orig[0][j + 1], orig[1][j + 1]), fill='red')
            j += 1
        draw.line((orig[0][j], orig[1][j], orig[0][0], orig[1][0]), fill='red')


trans = Transformations()

for i in range(10):
    orig = trans.transform(orig, 'resize', 0.8)
    orig = trans.transform(orig, 'rotate', 10)
    orig = trans.transform(orig, 'sheer', 0.2)
    trans.draw_square(orig)

canvas.show()

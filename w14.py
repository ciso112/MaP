from random import shuffle

# Generate maze using DFS ###

def make_maze(w = 12, h = 6):
    # make walls everywhere, remember visited locations
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1
        # neighbours' positions
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        # shuffle so we get random order order before looping
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            # delete wall, continue on a new location;  max functions eliminate negative indexes
            if xx == x: hor[max(y, yy)][x] = "+  "
            if yy == y: ver[y][max(x, xx)] = "   "
            walk(xx, yy)

    walk(0, 0)

    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s

print(make_maze())
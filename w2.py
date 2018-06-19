import math
import random


#  ### A Combinations, variations, permutations ###

my_list = ['A', 'B', 'C', 'D']


def permutations(my_list):
    if len(my_list) == 1:
        return [my_list]

    res = []
    for prmt in permutations(my_list[1:]):
        for i in range(len(my_list)):
            res.append(prmt[:i] + my_list[0:1] + prmt[i:])
    print(res)
    return res

def comb_number(n, k):

    if k == 0 or k == n:
        return 1
    else:
        return comb_number(n-1, k-1) + comb_number(n-1, k)

def choose_iter(elements, length):
    for i in range(len(elements)):
        if length == 1:
            yield (elements[i],)
        else:
            for next in choose_iter(elements[i+1:len(elements)], length-1):
                print(elements[i], next)
                yield (elements[i],) + next


def choose(l, k):
    return list(choose_iter(l, k))


# ### B Pascal's triangle ###

def pascal(n):
    if n==0:
        return [1]
    else:
        N = pascal(n-1)
        return [1] + [N[i] + N[i+1] for i in range(n-1)] + [1]


def pascal_triangle(n):
    for i in range(n):
        print pascal(i)

pascal_triangle(10)


# ### C Computation of Pi ###

def gregory(start):
    sum = 0
    i = 0
    down = 1.0
    up = 1.0
    while i < 1000:
        sum += up / down
        down += 2
        up = - up
        i += 1
        print sum
    return 4 * sum

print gregory(4)

def archimedes():
    a = 2 * math.sqrt(3)
    b = 3
    i = 0
    while i < 1000:
        a = 2 * a * b / (a + b)
        b = math.sqrt(a * b)
        i += 1
    return a

# print archimedes()

def monte_carlo():
    count_inside = 0
    i = 0
    while i < 1000:
        x, y = random.random(), random.random()
        if x * x + y * y < 1:
            count_inside += 1
        i += 1
    print 4.0 * count_inside / i

# monte_carlo()

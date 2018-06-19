import random
from collections import Counter

# ### A - Monty Hal ###

def monty(change):

    doors = [i for i in range(3)]
    car = random.choice(doors)
    choice = random.choice(doors)

    open_door = random.choice([i for i in doors if i not in [choice, car]])

    # change == 1 represents change your original door
    if change == 1:
        choice = [i for i in doors if i not in [choice, open_door]][0]

    # change == 2 represents randomly change/don't change door
    if change == 2:
        choice = [random.choice([i for i in doors if i not in [open_door]])][0]
        print random.choice([i for i in doors if i not in [car]]), choice, car

    # print random.choice([i for i in doors if i not in [car]])
    if choice == car:
        return True
    else:
        return False

def run_monty():
    #don't change, change, randomly
    wins = [0, 0, 0]
    runs = 1000
    for i in range(runs):
        if monty(0):
            wins[0] += 1
        if monty(1):
            wins[1] += 1
        if monty(2):
            wins[2] += 1
    print wins

    print "If a person CHANGES door, he wins %d %% of the time." % (float(wins[1])/runs*100)
    print "If a person does NOT CHANGE, he wins %d %% of the time." % (float(wins[0])/runs*100)
    print "If a person changes door RANDOMLY, he wins %d%% of the time." % (float(wins[2])/runs*100)

# run_monty()

# ### B Files analysis ###

#count symbols' occurrences
def analyze_files():
    for x in range(1,7):
        file_name = "random%d.txt" % x
        print file_name
        with open(file_name, "r") as f:
            content = f.read()
        result = Counter(content)
        print result


# ### C - Central Limit Theorem ###

weighted = (1, 2, 3, 4, 5, 6)
inverted = (6, 5, 4, 3, 2, 1)
normal = (1, 1, 1, 1, 1, 1)

def roll(die):
    number = random.uniform(0, sum(die))
    current = 0
    # bias takes 1., 2.,.. element from weighs list, iterate till current is smaller than number
    for i, bias in enumerate(die):
        current += bias
        if number <= current:
            return i + 1

def rolls(die, n, choose):
    results = []
    for _ in range(n):
        if choose:
            die = random.choice([weighted, inverted])
        results.append(roll(die))
    average =sum(results) / float(len(results))
    return average

# print rolls(normal, 10, True)

def clt(die, n, k, choose):
    averages = []
    for i in range(k):
        averages.append(rolls(die, n, choose))
    return averages

res =  Counter(clt('', 100, 500, True))
# print res
print sorted(res.items())



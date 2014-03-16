import random

def monty(num_doors = 3, p = 1):
    assert(num_doors >=3) , "num_doors must be >= 3"
    assert(p <= num_doors - 2), "p must be <= num_doors - 2"

    doors = []
    for _ in range(num_doors):
        doors.append(0)

    #put a prize randomly in one of the doors
    prize = random.randint(0, num_doors - 1)
    doors[prize] = 1
    original = random.randint(0, num_doors - 1)

    #monty reveals p goats
    goats = []
    for _ in range(p):
        goat = random.randint(0, num_doors - 1)
        while(goat == prize or goat == original or goat in goats):
            goat = random.randint(0, num_doors - 1)
        goats.append(goat)

    #you pick a door that is neither a goat door nor your original door
    answer = random.randint(0, num_doors - 1)
    while(answer in goats or answer == original):
        answer = random.randint(0, num_doors - 1)

    return doors[answer]

def monty_count(n, num_doors = 3, p = 1):
    count = 0
    for _ in range(n):
        count += monty(num_doors, p)
    count = float(count)
    return (count / n)
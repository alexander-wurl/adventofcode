#!/usr/bin/env python

def isInDict(value, memory) -> int:
    found = 0
    m = list(memory.items())
    for e in m[:-1]:
        if (value == e[1]):
            found = e[0]
    return found

def part1():

    memory = {1: 14, 2: 3, 3: 1, 4: 0, 5: 9, 6: 5}

    currentTurn = list(memory)[-1] + 1

    while (currentTurn <= 2020):

        lastValue = memory.get(currentTurn - 1)

        index = isInDict(lastValue, memory)

        if (index > 0):
            numberSpoken = (currentTurn - 1) - index
        else:
            numberSpoken = 0
    
        memory.update({currentTurn:numberSpoken})

        currentTurn += 1

    print("2020th number spoken: {}".format(numberSpoken))

# main
part1()
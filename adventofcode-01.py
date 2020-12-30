#!/usr/bin/env python3

import helper

def part1():
    data = helper.getData("01")

    solution = 0

    for e in data:
        for j in data:
            value = int(e) + int(j)
            if (value == 2020):
                #print(str(e) + " + " + str(j) + " = 2020!")
                solution = int(e) * int(j)
                #print(str(e) + " * " + str(j) + " = " + str(value) + "!")

    print(solution)

# main
part1()
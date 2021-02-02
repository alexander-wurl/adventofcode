#!/usr/bin/env python3

import os

def part1():

    questions = ""
    solution = 0

    file = open(os.path.dirname(__file__) + "/input-06.txt")

    for line in file:

        if (line != '\n'):
            questions = questions + line
        else:
            tlist = list("abcdefghijklmnopqrstuvwxyz")
            
            for e in questions:
                if (e in tlist):
                    tlist.remove(e)
            
            questions = ""

            v = 26 - len(tlist)
            solution += v

    print(solution)

# main

part1()
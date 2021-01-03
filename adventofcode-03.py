#!/usr/bin/env python3

import helper

def part1():
    file = helper.getData("03")

    start = 0
    trees = 0

    for line in file:
        if (start > 30):
            start = start - 31

        if (line[start] == '#'):
            trees += 1
            #print(line[0:start] + 'X' + line[start+1:31])
        #else:
            #print(line[0:start] + 'O' + line[start+1:31])

        start = start + 3

    print(trees)

# main
part1()

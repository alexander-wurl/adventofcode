#!/usr/bin/env python

import random

import helper

# print cubes, visible view can be expanded given margin parameter greater 0
def PrintCubes(cubes, margin = 0) -> int:

    # sort for x, y and z
    cubes.sort(key = lambda x: (x[0], x[1], x[2]))

    # set min and max +- tolerance
    max_x = max(cubes)[0] + margin
    min_x = min(cubes)[0] - margin
    max_y = max(cubes)[1] + margin
    min_y = min(cubes)[1] - margin
    max_z = max(cubes)[2] + margin
    min_z = min(cubes)[2] - margin

    count = 0

    for z in range(min_z, max_z + 1):
        print("z = {}".format(z))

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if ( (x, y, z, "#") in cubes):
                    print("#", end="")
                    count += 1
                else:
                    print(".", end="")

            print("")

    print("Number of active cubes is {}".count)
    return count


def SetActivity(data, x, y, z) -> (int, int, int, str):

    cube_is_active = False

    # get current element neighbours
    active_neighbours = []

    # set activity for current element
    if ((x, y, z, "#") in data):
        cube_is_active = True

    # look for active neighbours
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                if (((i, j, k, "#") in data) and ((i != x) or (j != y) or (k != z))):
                    active_neighbours.append((i, j, k, "#"))

    # count active neighbours
    count = len(active_neighbours)

    # if sum is 2 or 3 and cube(x, y) is active ...
    if (((count == 2) or (count == 3)) and (cube_is_active)):
        return (x, y, z, "#")
    elif ((count == 3) and (not cube_is_active)):
        return (x, y, z, "#")
    else:
        return (x, y, z, ".")

# main

def part1() -> int:
    ret = 0
    data = helper.getData("17")

    # set vars
    cubes = []
    l = len(data[0])
    start = -int((l - 1) / 2)
    end = -start

    margin = 6

    # init coordinates with '.' (extend du to lookup in neighbourhood)
    for z in range(start - margin, end + margin + 1):
        [cubes.append((x, y, z, ".")) for x in range(start - margin, end + margin + 1) for y in range(start - margin, end + margin + 1)]

    y = start

    for e in data:

        x = start

        for ee in e:

            # remove old data
            cubes.remove( (x, y, 0, ".") )

            # add data from file
            cubes.append( (x, y, 0, ee) )
            x += 1

        # next line/data (y increases)
        y += 1

    # six cycles
    for cycle in range(1, 7):
        print("### cyle: {} ###".format(cycle))
        cubes_new = []

        for cube in cubes:
            cube_new = SetActivity(cubes, cube[0], cube[1], cube[2])
            cubes_new.append(cube_new)

        cubes = cubes_new.copy()

        ret = PrintCubes(cubes_new, 1)
    
    return ret

# main

print( "Solution for part 1: {}".format(part1()) )

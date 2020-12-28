import helper

def moveNorth(position, value, direction):
    position["north"] += int(value)
    print( "moving {} north ... new position now is ({}, {}, {}, {})".format(value, position["east"], position["west"], position["north"], position["south"]) )
    return (position, direction)

def moveSouth(position, value, direction):
    position["north"] -= int(value)
    print( "moving {} south ... new position now is ({}, {}, {}, {})".format(value, position["east"], position["west"], position["north"], position["south"]) )
    return (position, direction)

def moveEast(position, value, direction):
    position["east"] += int(value)
    print( "moving {} east ... new position now is ({}, {}, {}, {})".format(value, position["east"], position["west"], position["north"], position["south"]) )
    return (position, direction)

def moveWest(position, value, direction):
    position["east"] -= int(value)
    print( "moving {} west ... new position now is ({}, {}, {}, {})".format(value, position["east"], position["west"], position["north"], position["south"]) )
    return (position, direction)

def moveForward(position, value, direction):

    moveToDirection = {
        "east": moveEast,
        "west": moveWest,
        "south": moveSouth,
        "north": moveNorth
    }
    
    moveToDirection[direction](position, int(value), direction)
    return (position, direction)


def changeEastLeft(degrees):

    newDirection = {
        0: "east",
        90: "north",
        180: "west",
        270: "south"
    }

    ret = newDirection[int(degrees)]
    return ret

def changeWestLeft(degrees):

    newDirection = {
        0: "west",
        90: "south",
        180: "east",
        270: "north"
    }

    return newDirection[int(degrees)]

def changeNorthLeft(degrees):

    newDirection = {
        0: "north",
        90: "west",
        180: "south",
        270: "east"
    }

    return newDirection[int(degrees)]

def changeSouthLeft(degrees):

    newDirection = {
        0: "south",
        90: "east",
        180: "north",
        270: "west"
    }

    return newDirection[int(degrees)]


def changeEastRight(degrees):

    newDirection = {
        0: "east",
        90: "south",
        180: "west",
        270: "north"
    }

    return newDirection[int(degrees)]

def changeWestRight(degrees):

    newDirection = {
        0: "west",
        90: "north",
        180: "east",
        270: "south"
    }

    return newDirection[int(degrees)]

def changeNorthRight(degrees):

    newDirection = {
        0: "north",
        90: "east",
        180: "south",
        270: "west"
    }

    return newDirection[int(degrees)]

def changeSouthRight(degrees):

    newDirection = {
        0: "south",
        90: "west",
        180: "north",
        270: "east"
    }

    return newDirection[int(degrees)]

def turnLeft(position, degrees, direction):

    changeDirection = {
        "east": changeEastLeft,
        "north": changeNorthLeft,
        "south": changeSouthLeft,
        "west": changeWestLeft
    }
    
    newdirection = changeDirection[direction](degrees)
    print("new direction is {}".format(newdirection))

    return (position, newdirection)

def turnRight(position, degrees, direction):

    changeDirection = {
        "east": changeEastRight,
        "north": changeNorthRight,
        "south": changeSouthRight,
        "west": changeWestRight
    }
    
    newdirection = changeDirection[direction](degrees)
    print("new direction is {}".format(newdirection))

    return (position, newdirection)


actions = {
    "N": moveNorth,
    "S": moveSouth,
    "E": moveEast,
    "W": moveWest,
    "L": turnLeft,
    "R": turnRight,
    "F": moveForward
}

# main




# current position
position = {"east": 0, "west": 0, "north": 0, "south": 0}

# current direction
direction = "east"

# load data
data = helper.getData("12")

for e in data:
    action = e[0]
    value = e[1:]

    (position, direction) = actions[action](position, value, direction)

e = position["east"]
n = position["north"]

distance = abs(int(position["east"])) + abs(int(position["north"]) )

print("solution: {}".format(distance))


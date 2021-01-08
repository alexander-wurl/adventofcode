#!/usr/bin/env python

import helper

def getValidTickets(tickets: list, notes: list):

    validTickets = []
    invalidvalue = -1

    for ticket in tickets:

        valid = True
        invalidvalue = -1

        for value in ticket:
            
            if (valid == False):
                break

            val = {}

            for note in notes:

                check = checkValidity(value, note)

                val[str(note)] = check

            #print(val)
            
            if (True in val.values()):
                valid = True
            else:
                valid = False
                invalidvalue = value
                #print("Mismatch")
                break

        if (valid):
            validTickets.append(ticket)
        #else:
        #    print("Value {} in ticket {} not valid!".format(invalidvalue, ticket))

    return validTickets

# check single value (for one note)
def checkValidity(value: int, note: list) -> bool:
    valid = False

    if (((value >= note[0]) and (value <= note[1])) or ((value >= note[2]) and (value <= note[3]))):
        valid = True

    return valid

# check multiple values (for one note), one mismatch means column is not valid for given note
def checkValidities(values: list, note: list) -> bool:
    valid = True

    for i in values:
        if not (((i >= note[0]) and (i <= note[1])) or ((i >= note[2]) and (i <= note[3]))):
            valid = False

    return valid

def part1():

    data = helper.getData("16")

    notes = []
    tickets = []

    # read notes
    for e in data[0:20]:
        temp = e.split(":")[1].replace("or", "-").replace(" ", "").split("-")
        notes.append(list([int(value) for value in temp]))

    # read tickets
    for e in data[26:]:
        temp = e.split(",")
        tickets.append(list([int(value) for value in temp]))


    validity = {}

    # scanning error rate
    ser = 0

    # all tickets
    for ticket in tickets:

        # all values
        for value in ticket:

            # all notes
            for note in notes:
                validity[str(note)] = checkValidity(value, note)

            # check validity
            if not True in validity.values():
                ser += value
     
            validity.clear

    print("Solution for part 1 is: {}.".format(ser))

def part2():

    data = helper.getData("16")

    notes = []
    tickets = []

    # notes = [
    #     [0, 1, 4, 19],
    #     [0, 5, 8, 19],
    #     [0, 13, 16, 19]
    # ]

    # tickets = [
    #     [3, 9, 18],
    #     [15, 1, 5],
    #     [5, 14, 9]
    # ]

    #read notes
    for e in data[0:20]:
       temp = e.split(":")[1].replace("or", "-").replace(" ", "").split("-")
       notes.append(list([int(value) for value in temp]))

    #read tickets
    for e in data[25:]:
       temp = e.split(",")
       tickets.append(list([int(value) for value in temp]))

    validTickets = getValidTickets(tickets, notes)
    
    # now process valid tickets
    for note in notes:

        for columnIndex in range(0, len(validTickets[0])):

            column = [t[columnIndex] for t in validTickets]

            if (checkValidities(column, note)):
                print("Note {}: matches with column {}".format(note, columnIndex))

# main

part1()

part2() # solution found by manual elimination, algorithm still to do

solution = 157*113*53*101*167*191
print("solution for part 2 is: {}".format(solution))
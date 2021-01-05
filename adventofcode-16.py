#!/usr/bin/env python

import helper

def checkValidity(value: int, note: list) -> bool:
    valid = False

    if (((value >= note[0]) and (value <= note[1])) or ((value >= note[2]) and (value <= note[3]))):
        valid = True

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
                validity.update({str(note): checkValidity(value, note)})

            # check validity
            if not True in validity.values():
                ser += value
                #print("Value {} in ticket is not valid! Scanning error rate now is: {}.".format(value, ser))

            validity.clear

    print("Solution for part 1 is: {}.".format(ser))

# main
part1()

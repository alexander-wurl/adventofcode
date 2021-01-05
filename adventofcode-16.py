#!/usr/bin/env python

import helper

def checkValidity(value: int, note: list) -> bool:
    valid = False

    if (((value >= note[0]) and (value <= note[1])) or ((value >= note[2]) and (value <= note[3]))):
        valid = True

    return valid

def checkSimilarity(value: int, note: list) -> bool:
    error = 0

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
     
            validity.clear

    print("Solution for part 1 is: {}.".format(ser))

def part2():

    data = helper.getData("16")

    notes = []
    tickets = []
    
    validTickets = []

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
    for e in data[26:]:
       temp = e.split(",")
       tickets.append(list([int(value) for value in temp]))

    validity = {}

    # all tickets
    for ticket in tickets:

        # all values
        for value in ticket:

            # all notes
            for note in notes:
                validity.update({str(note): checkValidity(value, note)})

        # check validity
        if not False in validity.values():
            validTickets.append(ticket)

        validity.clear


    # now process valid tickets
    noteNumber = 0
    columnNumber = 0
    
    notesO = notes.copy()
    noteLen = len(notesO)

    # columns
    for columnNumber in range(0, len(validTickets[0])):
        
        for note in notes:

            matchingNotes = True

            for ticket in validTickets:

                if (not checkValidity(ticket[columnNumber], note)):
                    matchingNotes = False
                    
            
            if (matchingNotes):
                print("column number {} matches with note {}".format(columnNumber, note))
        



# main

part1()

#part2() # still not working :(

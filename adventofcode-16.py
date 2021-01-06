#!/usr/bin/env python

import helper

def getValidTickets(tickets: list, notes: list):

    validTickets = []

    for ticket in tickets:

        valid = True

        for value in ticket:

            for note in notes:

                check = checkValidity(value, note)

            if (not check):
                valid = False
                break
        
        if (valid):
            validTickets.append(ticket)

    return validTickets

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
     
            validity.clear

    print("Solution for part 1 is: {}.".format(ser))

def checkNotesInColumn(notes:list, columnValues:list):

    match = True
    notesIndex = -1

    for i in range(0, len(notes)):

        for e in columnValues:
            if (not checkValidity(e, notes[i])):
                match = False

        if match:
            #print("Match: {}, {}".format(i, notes[i]))
            notesIndex = i
            break

    return notesIndex

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
    for e in data[26:]:
       temp = e.split(",")
       tickets.append(list([int(value) for value in temp]))

    validTickets = getValidTickets(tickets, notes)
    
    # now process valid tickets

    # every column


    for columnIndex in range(0, 19):

        column = [c[columnIndex] for c in tickets]

        index = checkNotesInColumn(notes, column)

        if (index >= 0):
            print("Match: {}".format)

    

# main

#part1()

part2() # still not working :(

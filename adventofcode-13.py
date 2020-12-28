#!/usr/bin/env python3

import helper

def getBusIds(data):
    return data.replace(",x", "").split(",")

def printTimeTable(time, info):
    print(time + "\t", end = "")
    for e in info:
        print(e + "\t", end = "")
    print("")

# data
data = helper.getData("13")

# estimated time of (my) arrival at bus stop
eta = data[0]

# relevant bus ids
ids = getBusIds(data[1])

# optional: print first line of bus schedules
#printTimeTable("time", ids)

# cast eta and set max waiting using highest bus id
i = int(eta)
max_wating_time = i + int(max(ids))

# initial values for 
waiting_time = 9999
bus_id = 0

while (i <= max_wating_time):

    bus_stops = []

    for e in ids:
        if ((i % int(e)) == 0):
            bus_stops.append("D")
            t = i - int(eta)
            if (waiting_time > t):
                waiting_time = t
                bus_id = int(e)
        else:
            bus_stops.append("-")

    # optional: print time table
    #printTimeTable(str(i), bus_stops)

    i += 1

print("solution: {}".format(bus_id * waiting_time))




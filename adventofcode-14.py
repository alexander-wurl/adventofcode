#!/usr/bin/env python

import helper

def getSumOfValuesInDictionary(dict):
    v = (dict.values())
    s = sum(v)
    return s

def part1():

    data = helper.getData("14")

    mask = ""
    memory = {}

    for e in data:

        # get mask ...
        if (e[0:7] == "mask = "):
            mask = e[7:]
        else:
            # ... or adress and value
            pos = e.find("] = ")
            adress = e[4:pos]
            value = e[pos+4:]

            # convert value to binary, remove prefix
            bvalue = str(bin(int(value)))[2:]

            # fill leading gap with zeros
            while (len(bvalue) < 36):
                bvalue = "0" + str(bvalue)

            # use mask to define binary value
            for (i, b) in enumerate(mask):
                if (b == "0"):
                    bvalue = bvalue[0:i] + "0" + bvalue[i+1:]
                elif (b == "1"):
                    bvalue = bvalue[0:i] + "1" + bvalue[i+1:]
                pass

            # binary value to int
            value = int(bvalue, 2)

            # update value if already exists otherwise add
            if (adress in memory):
                memory[adress] = value
            else:
                memory.update({adress:value})

    print(getSumOfValuesInDictionary(memory))

# main
part1()
from itertools import combinations
import helper

def isValidNumber(preamble, number):
    for e in combinations(preamble, 2):

        #print(str(e[0]) + " + " + str(e[1]) + " = " + str(number))
        sum = int(e[0]) + int(e[1])

        if (e[0] != e[1]) and (sum == int(number)):
            return True
    return False
    

data = helper.getData("09")

# preamble length
f = 25

# current index
i = f

# e is current element
for e in data[f:]:

    # build preamble from previous numbers
    start = i-f
    stop = i
    preamble = data[start:stop]

    # check for valid numbers in preamble 
    if (isValidNumber(preamble, e) == False):
        print(e + " is  not valid!")

    i += 1

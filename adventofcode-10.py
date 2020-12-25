import helper

def recTest(voltage, d1, d2, d3):
    # find elements in list which are 1, 2, or 3 lower 
    # then use each of them for recursive call

    global diff1
    global diff2
    global diff3

    if (voltage <= max):

        for e in data:
            if (e - voltage == 1):
                # diff = 1
                diff1.append("1|" + str(e) + "|" + str(voltage))
                print("1|" + str(e) + "|" + str(voltage))
                recTest(e, d1+1, d2, d3)
            elif (e - voltage == 2):
                # diff = 2
                diff2.append("2|" + str(e) + "|" + str(voltage))
                print("2|" + str(e) + "|" + str(voltage))
                recTest(e, d1, d2+1, d3)
            elif (e - voltage == 3):
                # diff = 3
                diff3.append("3|" + str(e) + "|" + str(voltage))
                print("3|" + str(e) + "|" + str(voltage))
                recTest(e, d1, d2, d3+1)
    else:
        pass

temp = helper.getData("10")

# to int
data = [int(e) for e in temp]

max = max(data) + 3

diff1 = []
diff2 = []
diff3 = []

recTest(0, 0, 0, 0)

diff1 = list(set(diff1))
diff2 = list(set(diff2))
diff3 = list(set(diff3))

print("diff1: " + str(len(diff1)))
print("diff2: " + str(len(diff2)))
print("diff3: " + str(len(diff3)))

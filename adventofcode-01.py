import helper

data = helper.getData("01")

for e in data:
    for j in data:
        value = int(e) + int(j)
        if (value == 2020):
            print(str(e) + " + " + str(j) + " = 2020!")
            value = int(e) * int(j)
            print(str(e) + " * " + str(j) + " = " + str(value) + "!")

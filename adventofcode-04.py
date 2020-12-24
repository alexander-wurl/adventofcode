import os

file = open(os.path.dirname(__file__) + "/input-04.txt")
validIds = 0

refList = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
tarList = []

for line in file:

    if (line == "\n"):

        # space found - check tarList's elements in refList
        valid = 0
        n = 0

        for el in tarList:
            if el in refList:
                valid = 1
                n += 1

        if (valid == 1) and (n >= 7):
            validIds += 1

        tarList = []

    pos1 = 0
    pos2 = line.find(':')

    while (pos2 > 0):
        tarList.append(line[pos1:pos2])

        # skip spaces
        pos1 = pos2+1

        while ((line[pos1:pos1+1] != ' ') and (line[pos1:pos1+1] != '')):
            pos1 += 1

        # consider space char
        pos1 += 1

        pos2 = line.find(':', pos1)

print("validIds: " + str(validIds))

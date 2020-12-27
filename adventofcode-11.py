import helper

def neighbours(data, x, y, lx, ly):
    # max 8 neighbours
    ret = []

    if (x > 0 and y > 0):
        ret.append( data[x-1][y-1] )
    if (x > 0):
        ret.append( data[x-1][y] )
    if (x > 0 and y < ly):
        ret.append( data[x-1][y+1] )

    if (y > 0):
        ret.append( data[x][y-1] )
    if (y < ly):
        ret.append( data[x][y+1] )

    if (x < lx and y > 0):
        ret.append( data[x+1][y-1] )
    if (x < lx):
        ret.append( data[x+1][y] )
    if (x < lx and y < ly):
        ret.append( data[x+1][y+1] )

    return ret

def changeSeats(data):

    x = 0
    y = 0
    lx = len(data) - 1
    ly = len(data[0]) - 1

    newdata = data.copy()
    change = False

    for e in data:
        for j in e:

            n = neighbours(data, x, y, lx, ly)

            if ( (data[x][y] == 'L') and (str(n).count('#') == 0) ):
                newdata[x] = newdata[x][0:y] + "#" + newdata[x][y+1:]
                change = True
            if ( (data[x][y] == '#') and (str(n).count('#') >= 4) ):
                newdata[x] = newdata[x][0:y] + "L" + newdata[x][y+1:]
                change = True

            y += 1
        y = 0
        x += 1

    for e in newdata:
        print(e)

    return change, newdata

# main

olddata = helper.getData("11")
finaldata = []

for i in range(100):
    (c, newdata) = changeSeats(olddata)
    if c == False:
        finaldata = olddata
        break
    else:
        olddata = newdata.copy()
    print("")

c = 0
for e in finaldata:
    for j in e:
        if (j == '#'):
            c += 1

print(c)    


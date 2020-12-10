questions = ""
solution = 0

file = open("input-06.txt")

for line in file:

    if (line != '\n'):
        questions = questions + line
    else:
        tlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        for e in questions:
            if (e in tlist):
                tlist.remove(e)
        
        questions = ""

        v = 26 - len(tlist)
        solution += v

        print("final solution: " + str(solution))

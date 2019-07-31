# Marti157
print "THREE IN A ROW"

table = {}
for i in range(1, 4):
    table[i] = {}
for i in range(1, 4):
    for e in range(1, 4):
        table[i][e] = " "

def checkScore(table, how, x, y, t):

    # Vertical cases
    if how == 1:
        casesx = [x, x, x]
        casesy = [y - 1, y, y + 1]

    # Horizontal cases
    elif how == 2:
        casesx = [x - 1, x, x + 1]
        casesy = [y, y, y]

    # Diagonal cases (top right to bottom left)
    elif how == 3:
        casesx = [x + 1, x, x - 1]
        casesy = [y - 1, y, y + 1]

    # Diagonal cases (top left to bottom right)
    else:
        casesx = [x - 1, x, x + 1]
        casesy = [y - 1, y, y + 1]

    counter = 0
    for i in range(3):
        try:
            if table[casesx[i]][casesy[i]] == t:
                counter += 1
        except:
            continue

    if counter == 3:
        printTable(table)
        print "\n{} IS THE WINNER.".format(t)
        exit()

def printTable(table):
    print "\n    1   2   3"
    for i in range(1, 4):
        print "{} |".format(i),
        for e in range(1, 4):
            print "{} |".format(table[e][i]),
        print
    print

t = "X"
try:
    while True:
        printTable(table)

        coordinates = raw_input("{}: ENTER COORDINATES (x y): ".format(t)).split(" ")
        x = int(coordinates[0])
        y = int(coordinates[1])

        if table[x][y] != " ":
            print "ALREADY WRITTEN TO THESE COORDINATES.\n"
            continue

        table[x][y] = t

        for y in range(1, 4):
            for x in range(1, 4):
                if table[x][y] == t:
                    checkScore(table, 1, x, y, t)
                    checkScore(table, 2, x, y, t)
                    checkScore(table, 3, x, y, t)
                    checkScore(table, 4, x, y, t)

        t = "X" if t != "X" else "O"

except KeyboardInterrupt:
    print
    exit()

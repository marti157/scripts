"""Area calculator
By Marti157
Use any units, they all have the same output"""

import time

def Play():
    selectionValidList = {'1','2','3','4'}
    print "Select a figure from the list by inputting"
    print "the assigned number!"
    print "\n"
    print "[1] Square"
    print "[2] Rectangle"
    print "[3] Triangle"
    print "[4] Circle"
    print "\n"
    print "More to come soon!"
    print "\n"
    choice = raw_input()
    choice = str(choice)
    if choice in selectionValidList:
        if choice == '1':
            print "\n"
            print "\n"
            print "\n"
            print "You have chosen Square!"
            time.sleep(1)
            print "\n"
            print "Plase input the length of"
            print "ANY side of the square:"
            print "\n"
            mesurament1 = raw_input()
            print "\n"
            answer = int(mesurament1) * int(mesurament1)
            time.sleep(1)
            print "\n"
            print "The total area of your square"
            print "is:"
            print "\n"
            print answer
            Start()
        elif choice == '2':
            print "\n"
            print "\n"
            print "\n"
            print "You have chosen Recangle!"
            time.sleep(1)
            print "\n"
            print "Plase input the length of"
            print "one of the LONG sides of your"
            print "rectangle:"
            print "\n"
            mesurament1 = raw_input()
            print "\n"
            print "Ok. Please input the length"
            print "of one of the SHORT sides of"
            print "your rectangle:"
            print "\n"
            mesurament2 = raw_input()
            answer = int(mesurament1) * int(mesurament2)
            time.sleep(1)
            print "\n"
            print "The total area of your rectangle"
            print "is:"
            print "\n"
            print answer
            Start()
        elif choice == '3':
            print "\n"
            print "\n"
            print "\n"
            print "You have chosen Triangle!"
            time.sleep(1)
            print "\n"
            print "Plase input the length of the"
            print "BASE of your triangle:"
            print "\n"
            mesurament1 = raw_input()
            print "\n"
            print "Ok. Please input the HEIGHT"
            print "of your triangle:"
            print "\n"
            mesurament2 = raw_input()
            answer = int(mesurament1) * int(mesurament2) / 2
            time.sleep(1)
            print "\n"
            print "The total area of your triangle"
            print "is:"
            print "\n"
            print answer
            Start()
        else:
            print "\n"
            print "\n"
            print "\n"
            print "You have chosen Circle!"
            time.sleep(1)
            print "\n"
            print "Plase input the RADIUS of your"
            print "circle:"
            print "\n"
            mesurament1 = raw_input()
            answer = int(mesurament1) * int(mesurament1) * 3.14159265359
            time.sleep(1)
            print "\n"
            print "The total area of your circle"
            print "is:"
            print "\n"
            print answer
            Start()
    else:
        print "\n"
        print "Error: no valid number was selected."
        print "\n"
        time.sleep(1.5)
        print "\n"
        print "\n"
        print "\n"
        Play()

def Start():
    print "\n"
    time.sleep(0.5)
    print "To start again, press any key"
    print "\n"
    raw_input()
    Play()

print "\n"
print "                            Area Calculator"
print "                             Use any units"
print "\n"
time.sleep(1)
Play()

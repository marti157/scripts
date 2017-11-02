"""Square mesuraments calculator
By Marti157
Gives Side, Area, Diagonal and Perimeter of a square"""

import math
import time

def start():
	choice = 1
	print "\n###########################################\n#                                         #\n#         Square Sizes Calculator         #\n# From Side, Diagonal, Perimeter or Area! #\n#                                         #\n###########################################\n"
	time.sleep(2)
	print "What length to use?\n\n [1] Square Side\n [2] Square Area\n [3] Square Diagonal\n [4] Square Perimeter\n\n: (Insert number)\n"
	choice = raw_input("> ")
	if choice == "1":
		useSide()
	elif choice == "2":
		useArea()
	elif choice == "3":
		useDiagonal()
	elif choice == "4":
		usePerimeter()							
	else:
		print "\nInvalid choice."
		time.sleep(1)
		start()
def useSide():
	print "\n\nWhat is your square\'s side length?\n"
	side = raw_input("> ")
	try:
		float(side)
		intside = int(side)
		side = float(side)
		if side > 999999999:
			print "\nWoah! That\'s quite big!"
			time.sleep(1)
			useSide()
		else:
			print "\nOkay, " + str(intside) + "\n"
			time.sleep(2)
			area = side ** 2
			diagonal = (side ** 2) + (side ** 2)
			diagonal = math.sqrt(diagonal)
			perimeter = side * 4
			print "\nCalculations complete."
			time.sleep(1)
			print "\n: Square\'s area = " + str(area) + "\n: Square\'s diagonal = " + str(diagonal) + "\n: Square's perimeter = " + str(perimeter) + "\n\nPress any key to continue..."
			raw_input()
			start()
	except ValueError:
		print "The side\'s length is invalid."
def useArea():
	print "\n\nWhat is your square's area?\n"
	area = raw_input("> ")
	try:
		float(area)
		intarea = int(area)
		area = float(area)
		if area > 9999999:
			print "\nWoah! That\'s quite big!"
			time.sleep(1)
			useSide()
		else:
			print "\nOkay, " + str(intarea) + "\n"
			time.sleep(2)
			side = math.sqrt(area)
			diagonal = (side ** 2) + (side ** 2)
			diagonal = math.sqrt(diagonal)
			perimeter = side * 4
			print "\nCalculations complete."
			time.sleep(1)
			print "\n: Square\'s side = " + str(side) + "\n: Square\'s diagonal = " + str(diagonal) + "\n: Square's perimeter = " + str(perimeter) + "\n\nPress any key to continue..."
			raw_input()
			start()
	except ValueError:
		print "The area\'s length is invalid."
		useArea()
def useDiagonal():
	print "\n\nWhat is your square\'s diagonal length?\n"
	diagonal = raw_input("> ")
	try:
		float(diagonal)
		intdiagonal = int(diagonal)
		diagonal = float(diagonal)
		if diagonal > 99999999:
			print "\nWoah! That\'s quite big!"
			time.sleep(1)
			useSide()
		else:
			print "\nOkay, " + str(intdiagonal) + "\n"
			time.sleep(2)
			side = diagonal / math.sqrt(2)
			perimeter = side * 4
			area = side ** 2
			print "\nCalculations complete."
			time.sleep(1)
			print "\n: Square\'s side = " + str(side) + "\n: Square\'s area = " + str(area) + "\n: Square's perimeter = " + str(perimeter) + "\n\nPress any key to continue..."
			raw_input()
			start()
	except ValueError:
		print "The diagonal\'s length is invalid."
def usePerimeter():
	print "\n\nWhat is your square\'s perimeter length?\n"
	perimeter = raw_input("> ")
	try:
		float(perimeter)
		intperimeter = int(perimeter)
		perimeter = float(perimeter)
		if Perimeter > 99999999:
			print "\nWoah! That\'s quite big!"
			time.sleep(1)
			useSide()
		else:
			print "\nOkay, " + str(intperimeter) + "\n"
			time.sleep(2)
			side = perimeter / 4
			area = side ** 2
			diagonal = side * math.sqrt(2)
			print "\nCalculations complete."
			time.sleep(1)
			print "\n: Square\'s side = " + str(side) + "\n: Square\'s area = " + str(area) + "\n: Square's diagonal = " + str(diagonal) + "\n\nPress any key to continue..."
			raw_input()
			start()
	except ValueError:
		print "The perimeter\'s length is invalid."
try:
	start()
except KeyboardInterrupt:
	print "\n\nSee ya..."
"""A better version of the last one I made.
By Marti157"""

import random

print "\nGuess the number I\'m thinking!\n(It's a number from 1 to 9):\n"
guess = raw_input()
checkList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number = random.randrange(1, 10)
try:
	guess = int(guess)
	if guess in checkList:
		if number == guess:
			print "\nYou got it first try! Nice!\n"
			exit()
		else:
			if number > guess:
				print "\nThe number I'm thinking is bigger!\nTry again!\n"
				guess = raw_input()
				if guess == number:
					print "\nThe number was bigger than"
				elif guess > number:
					print "\nThe number was bigger than " + str(guess) + "!\nI was thinking of " + str(number) + "!\n"
				else:
					print "\nThe number was bigger than " + str(guess) + "!\nI was thinking of " + str(number) + "!\n"
				exit()
			else:
				print "\nThe number I'm thinking is smaller!\nTry again!\n"
				guess = raw_input()
				guess = int(guess)
				if guess == number:
					print "\nThe number was bigger than"
				elif guess > number:
					print "\nThe number was bigger than " + str(guess) + "!\nI was thinking of " + str(number) + "!\n"
				else:
					print "\nThe number was bigger than " + str(guess) + "!\nI was thinking of " + str(number) + "!\n"	
				exit()
	else:
		print "\nThis is not a number between 1 and 9!"
		exit()
except ValueError:
	print "\nThis is not a number!"
	exit()

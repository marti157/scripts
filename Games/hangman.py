"""Good enough hangman
By Marti157"""

from random import randint
print "\nHangman :)\n"
try:
	def play():
		guesses = 15
		words = ["word", "hello", "house", "tree", "nice", "dog", "good", "air", "cat", "baby", "food", "car", "center", "face", "idea", "man", "open", "poor", "rich", "short", "vote", "zebra"]
		word = words[randint(0, len(words) - 1)]
		wordIndex = []
		for i in word:
			wordIndex.append(i)
		example = []
		for i in range(len(word)):
			example.append(" _")
		index = 0
		while guesses > 0:
			print "\nAvailable Guesses: " + str(guesses) + "\n"
			print example
			print ''.join(example)
			guess = raw_input("\nYour Guess (letter or word): ").lower()
			guesses -= 1
			if guess == word:
				print "Nice!"
				print "You win!"
				print "\nPress enter to play again..."
				raw_input()
				play()
			else:
				if len(guess) == 1:
					if guess in word:
						for i in wordIndex:
							if i == guess:
								example[index] = " " + guess
							index += 1
						print "Nice!"
						if " _" not in example:
							print "You win!"
							print "\nPress enter to play again..."
							raw_input()
							play()
					else:
						print "Nope."
				else:
					print "Nope."
			index = 0
		print "\nOut of guesses!"
		print "The word was \"" + word + "\"!"
		print "\nPress enter to play again..."
		raw_input()
		play()
	play()
except KeyboardInterrupt:
	print "\nSee Ya!..."
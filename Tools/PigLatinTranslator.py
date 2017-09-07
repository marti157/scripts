"""Simple Pig Latin translator: Pig Latin is a language game,
where you move the first letter of the word to the end and 
add "ay." So "Python" becomes "ythonpay." To run, insert your
word string in the "word" variable.
I know, this translator could be made much simpler. Do not pull
request. I just wanted to try it out with lists and other
components.
by Marti157"""

import time

word = "Test"

print "\nWelcome to the Pig Latin translator!"
print "Input a word in the script and wait for the result!"
print "Your word is: \"" + word + "\""
word = word.lower()
firstLetter = word[0]
time.sleep(3)
wordLen = len(word)
word = word[1:]
if any(char.isdigit() for char in word) or word == "" or wordLen > 50:
	print "\nThe word is invalid. Quitting..."
	exit()
else:
	wordCcionary = [word]
	wordCcionary.insert(2, firstLetter)
	wordCcionary.append("ay")
	word = "".join(wordCcionary)
	print "\nDone! Pig Latinned word is: \"" + word + "\""

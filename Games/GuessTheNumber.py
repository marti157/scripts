"""The simplest guess-the-number game
you can find :)
By Marti157"""

import random

print "Guess the number that i'm thinking!"
print "(0-10)"
print "\n"
guess = input("Guess: ")
int(guess)
numb = random.randrange(0, 10)
if guess == numb:
    print "Congratulations, you got it right!"
else:
    print "Wrong, it was", numb
print "\n"

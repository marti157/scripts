"""Simple caesar encrypter and decrypter with bruteforce
By Marti157"""

import sys

def error():
	print "Usage: " + sys.argv[0] + " [option] or \"message\""
	print "Try \"-h\" or \"--help\" option examples."
	exit()

def help():
	print "Usage: " + sys.argv[0] + " [option] or \"message\"\nExamples:"
	print sys.argv[0] + " Hello\n" + sys.argv[0] + " \"My name is Robert\""
	exit()

def start():
	msg = sys.argv[1]
	alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	result = []
	for e in range(26):
		for i in msg:
			if i in alphabet:
				num = alphabet.index(i)
				result.append(alphabet[num + e])
			else:
				result.append(i)
		print ''.join(result)
		result = []

try:
	if len(sys.argv) == 2:
		if sys.argv[1][0] == "-":
			if sys.argv[1] == "-h":
				help()
			elif sys.argv[1] == "--help":
				help()
			else:
				error()
		else:
			start()
	else:
		error()
except IndexError:
	help()
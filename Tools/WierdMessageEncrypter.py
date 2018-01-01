import sys
import random
import crypt

alf = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y"]
try:
	msg = sys.argv[1]
	print "Your message: " + msg
	msglist = [x for x in msg if x in alf]
	random.shuffle(msglist)
	asciisum = 0
	for i in msglist:
		asciisum = asciisum + ord(i)
	msglist.insert(random.randint(1, len(msg) - 1), asciisum)
	msglist[0] = chr(ord(msglist[0]) - 1)
	msglist[len(msg)] = chr(ord(msglist[len(msg)]) - 1)
	salt = []
	for i in range(12):
		salt.append(alf[random.randint(0, len(alf))])
	salt.insert(0, "$")
	finalmsg = []
	for i in salt:
		finalmsg.append(str(i))
	for i in msglist:
		finalmsg.append(str(i))
	print "\nEncrypted message: " + ''.join(finalmsg)
except IndexError:
	print "Usage: " + sys.argv[0] + " <message>"

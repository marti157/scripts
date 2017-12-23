"""Simple but efficient prime number finder.
By Marti157"""

import time

try:
	option = raw_input("\n[1] Full Speed\n[2] Moderate\n\n(Insert Number): ")
	print "\nStarting Prime Finder... (Exit using ctrl + c)"
	time.sleep(1)
	if option == "1":
		print "\n1\n2"
		num = 3
		llist = []
		may = False
		while True:
			for i in range(int(num)):
				llist.append(i)
			llist.remove(0)
			llist.remove(1)
			for i in llist:
				if num % i == 0:
					may = True
			if may == False:
				print num
			num += 1
			may = False
	elif option == "2":
		print "\n1"
		time.sleep(1)
		print "2"
		time.sleep(1)
		num = 3
		llist = []
		may = False
		while True:
			for i in range(int(num)):
				llist.append(i)
			llist.remove(0)
			llist.remove(1)
			for i in llist:
				if num % i == 0:
					may = True
			if may == False:
				print num
				time.sleep(1)
			num += 1
			may = False
	else:
		print "\nInvalid Option. Quitting..."
		exit()
except KeyboardInterrupt:
	print "\nGoodbye..."
	exit()
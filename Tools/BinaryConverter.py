#Convert Decimal or ASCII to binary without using the function bin()
#By Marti157
def main():
	x = raw_input("Choose option:\n[1] Base 10 to Base 2\n[2] Text to Base 2\n: ")
	if x == "1":
		try:
			n = int(raw_input("Enter a number in Base 10: "))
			get2(n)
			end()
		except ValueError:
			print "Invalid number."
			end()
	elif x == "2":
		try:
			n = raw_input("Enter text: ")
			int(n)
			print "Invalid text."
			end()
		except ValueError:
			for i in n:
				get2(ord(i))
			end()
	else:
		print "Invalid option."
		end()
def get2(x):
	curr = x
	result = []
	while curr > 0:
		if curr % 2 == 0:
			result.append("0")
		else:
			result.append("1")
		curr = curr / 2
	result.append("0" * (8 - len(result)))
	result.reverse()
	print ''.join(result),
def end():
	print "\nPress enter to continue..."
	raw_input()
	main()
try:
	main()
except KeyboardInterrupt:
	print "\nQuitting..."
	exit()
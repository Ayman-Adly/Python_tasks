import os
from time import sleep
os.system('cls')
#right arrow
print(" "*12)
for k in range(1,12):
	for n in range(0,32):
		if n < 27:
			if k != 6:
				print(" ", end = "")
			else:
				if n < 16:
					print(" ", end = "")
				if n >= 16:
					print("*", end = "")

	if k <= 6:
		print("*"*k, end = "")
	else:
		print("*"*(12-k), end = "")
	print("")
		
sleep(1)
os.system('cls')

#down arrow
for k in range(1,17):
	if k <11:
		print(" "*16, end = "")
		print("*", end = "")
	else:
		print(" "*(2*k-16), end = "")
		print("* "*(11-2*(k-11)), end = "")
	print("")
		
sleep(1)
os.system('cls')

#left arrow
print(" "*12)
for k in range(1,12):
	if k < 6:
		print(" "*(6-k), end = "")
		print("*"*k, end = "")
	elif k == 6:
		print("*"*17, end = "")
	else:
		print(" "*(k-6), end = "")
		print("*"*(12-k), end = "")
	print("")

sleep(1)
os.system('cls')

#Up arrow
for k in range(1,17):
	if k <= 6:
		print(" "*(16-2*k), end = "")
		print("* "*(2*(k)-1), end = "")
		
	else:
		print(" "*14, end = "")
		print("*", end = "")
	print("")
		
sleep(1)
os.system('cls')

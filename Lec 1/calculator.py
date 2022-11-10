import math
print("Please choose the mood of operation: ")
print("----------------------------------------------------------")
print("For scientific choose s and for programmer choose p")
print("----------------------------------------------------------")
mood = input("The desired mood: ")
print("----------------------------------------------------------")
if mood == 's' or mood == 'S':
	print("For addition choose: 1\nFor subtraction choose: 2\nFor multiplication choose: 3\nFor division choose: 4\nFor exponent choose: 5\nFor absolute value choose: 6\nFor inverse choose: 7\nFor square choose: 8\nFor root choose: 9\nFor power choose: 10\nFor factorial choose: 11\nFor modulus choose: 12")
	print("----------------------------------------------------------")
	choice = int(input("Your choice: "))
	print("----------------------------------------------------------")
	if choice == 1:
		print("Addition")
		no_1 = float(input("Please input the first no: "))
		no_2 = float(input("Please input the Second no: "))
		print("Your result = "+str(no_1+no_2))
	elif choice == 2:
		print("Subtraction")
		no_1 = float(input("Please input the first no: "))
		no_2 = float(input("Please input the Second no: "))
		print("Your result = "+str(no_1-no_2))
	elif choice == 3:
		print("Multiply")
		no_1 = float(input("Please input the first no: "))
		no_2 = float(input("Please input the Second no: "))
		print("Your result = "+str(no_1*no_2))
	elif choice == 4:
		print("Divide")
		no_1 = float(input("Please input the first no: "))
		no_2 = float(input("Please input the Second no: "))
		if no_2 != 0:
			print("Your result = "+str(no_1/no_2))
		else:
			print("You can not divide by zero")
	elif choice == 5:
		print("Exponent")
		no_1 = float(input("Please input no: "))
		print("Your result = "+str(math.exp(no_1)))
	elif choice == 6:
		print("Absolute")
		no_1 = float(input("Please input no: "))
		print("Your result = "+str(abs(no_1)))
	elif choice == 7:
		print("Inverse")
		no_1 = float(input("Please input no: "))
		if no_1 != 0:
			print("Your result = "+str(1/no_1))
		else:
			print("You can not divide by zero")
	elif choice == 8:
		print("Square")
		no_1 = float(input("Please input no: "))
		print("Your result = "+str(no_1**2))
	elif choice == 9:
		print("Square root")
		no_1 = float(input("Please input no: "))
		print("Your result = "+str(no_1**0.5))
	elif choice == 10:
		print("Power")
		no_1 = float(input("Please input the first no: "))
		no_2 = float(input("Please input the Second no: "))
		print("Your result = "+str(no_1**no_2))
	elif choice == 11:
		print("Factorial")
		no_1 = int(input("Please input no: "))
		result = 1
		for i in range(1,no_1+1,1):
			result *=i
		print("Your result = "+str(result))
	elif choice == 12:
		print("Modulus")
		no_1 = float(input("Please input the first no: "))
		no_2 = float(input("Please input the Second no: "))
		print("Your result = "+str(no_1%no_2))
	else:
		print("Your choice is out of range.")
	
elif mood == 'p' or mood == 'P':
	print("The following conversions are available: ")
	print("----------------------------------------------------------")
	print("For Hex write: h\nFor Dec write: d\nFor Oct write: o\nFor Bin write: b")
	print("----------------------------------------------------------")
	in_type = input("The value you will input type: ")
	value = input("The Value: ")
	out_type = input("The type you want to cast: ")
	if in_type == 'h' or in_type == 'H':
		inside = hex(value)
		if out_type == 'd' or out_type == 'D':
			print("Your result: "+str(int(inside)))
		elif out_type == 'o' or out_type == 'O':
			print("Your result: "+str(oct(inside)))
		elif out_type == 'b' or out_type == 'B':
			print("Your result: "+str(bin(inside)))
		else:
			print("The type you want as an output is not available.")
	elif in_type == 'd' or in_type == 'D':
		inside = int(value)
		if out_type == 'h' or out_type == 'H':
			print("Your result: "+str(hex(inside)))
		elif out_type == 'o' or out_type == 'O':
			print("Your result: "+str(oct(inside)))
		elif out_type == 'b' or out_type == 'B':
			print("Your result: "+str(bin(inside)))
		else:
			print("The type you want as an output is not available.")
	elif in_type == 'o' or in_type == 'O':
		inside = oct(value)
		if out_type == 'd' or out_type == 'D':
			print("Your result: "+str(int(inside)))
		elif out_type == 'h' or out_type == 'H':
			print("Your result: "+str(hex(inside)))
		elif out_type == 'b' or out_type == 'B':
			print("Your result: "+str(bin(inside)))
		else:
			print("The type you want as an output is not available.")
	elif in_type == 'b' or in_type == 'B':
		inside = bin(value)
		if out_type == 'd' or out_type == 'D':
			print("Your result: "+str(int(inside)))
		elif out_type == 'o' or out_type == 'O':
			print("Your result: "+str(oct(inside)))
		elif out_type == 'h' or out_type == 'H':
			print("Your result: "+str(hex(inside)))
		else:
			print("The type you want as an output is not available.")
	else:
		print("The input Type is not available.")
else:
	print("The desired mood is not available")
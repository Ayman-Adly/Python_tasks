print("--System for grocerry shop--")
print("#Welcome to ITI Shop")
stock = []
counter = 0
while True:
	print("-----------------------------------")
	mode = int(input("Select Mode For customer press 1 , for owner press 2 , to exist press 0  : "))
	print("-----------------------------------")
	cus_list = []
	cus_counter = 0
	if mode == 1:
		print("Customer mode")
		while True:
			print("-----------------------------------")
			print("To show our products press 1\nTo Buy from our products press 2\nto print the bill press 3\nto exist press 0")
			print("-----------------------------------")
			cus_s = int(input("Choose one option from the previous list: "))
			print("-----------------------------------")
			if cus_s == 1:
				print("Show products")
				print("-----------------------------------")
				for n in range(0,counter,1):
					print(str(stock[n][0])+"- "+stock[n][1]+" has: "+str(stock[n][3])+"each costs: "+str(stock[n][2]))
				print("-----------------------------------")
			elif cus_s == 2:
				print("Buy products")
				print("-----------------------------------")
				index = int(input("Please write the index of the product you want to buy: "))
				cus_list.append(stock[index])
				quan = int(input("Enter the quantity you want to buy: "))
				q_old = stock[index][3]
				if quan == q_old:
					srock.remove(stock[index])
				elif q_old > quan:
					stock[index][3] = q_old - quan
					cus_list[cus_counter][3] = quan
				else:
					print("This amunt is not available in stock")
				cus_counter +=1
			elif cus_s == 3:
				print("Print your bill")
				print("-----------------------------------")
				for n in range(0,cus_counter,1):
					print(str(cus_list[n][0])+"- "+cus_list[n][1]+" has: "+str(cus_list[n][3])+"each costs: "+str(cus_list[n][2]))
				print("-----------------------------------")
			elif cus_s == 0:
				print("Thank you for your time.")
				break
			else:
				print("No such command is available")
	elif mode == 2:
		print("ITI owner mode")
		while True:
			print("-----------------------------------")
			print("Add new products --- press 1\nShow Products --- press 2\nAdd Cost --- press 3\nChange cost --- press 4\nto exist --- press 0")
			print("-----------------------------------")
			owner_s = int(input("Choose one option from the previous list: "))
			print("-----------------------------------")
			if owner_s == 1:
				print("Add new product")
				print("-----------------------------------")
				new_list = [0,0,0,0] #[prod.number,name,cost,quantity]
				new_list[1] = input("Please enter the name of this product: ")
				new_list[3] = int(input("Please enter the quantity of this product in stock: "))
				new_list[0] = counter
				stock.append(new_list)
				counter +=1
				print("-----------------------------------")
			elif owner_s == 2:
				print("Show products")
				print("-----------------------------------")
				for n in range(0,counter,1):
					print(str(stock[n][0])+"- "+stock[n][1]+" has: "+str(stock[n][3])+"each costs: "+str(stock[n][2]))
				print("-----------------------------------")
			elif owner_s == 3:
				print("Add cost")
				print("-----------------------------------")
				index = int(input("Please enter the index of the product you want to add cost to: "))
				cost = int(input("Please enter the desired cost: "))
				stock[index][2] = cost
				print("-----------------------------------")
			elif owner_s == 4:
				print("Change cost")
				print("-----------------------------------")
				index = int(input("Please enter the index of the product you want to change cost to: "))
				cost = int(input("Please enter the desired cost: "))
				stock[index][2] = cost
				print("-----------------------------------")
			elif owner_s == 0:
				print("Thank you for your time.")
				break
			else:
				print("No such command is available")
	elif mode == 0:
		print("Thank you for your time.")
		break
	else:
		print("No such command is available")
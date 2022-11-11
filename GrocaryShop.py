'''Welcome to my project 
	this is a Grocary shop data base application
	this application helps the owner to manage his shop
	and also helps the customer to buy products from this shop 
	depending on two modes:
	Mode 1--->is for customer usage
	Mode 2--->is for owner mangment
	The user can show and buy items from the shop and also can print his bill
	The owner can add a new item or show the existed ones or change a cost of an existed item
'''
	
#the shop products' intial data base
Item= 	  ["apple","banana","cherry"]
Cost= 	  [ 0.5   ,   2    ,    3   ]
Quantity= [ 40    ,   30   ,    70  ]

while True:
	print("For Customer Mode Press 1 ")
	print("For Owner Mode Press 2 ")
	print("To Exit Press 0 ")
	
	Mode= int (input()) #Selec the mode for customer or owner

	Total_Cost=0 #variable to save the total cost if the user want to print his bill
	
	while Mode != 0: #checking the exit statues
#***********************************************************************************************#
#**************************               Customer Mode               **************************#
#***********************************************************************************************#
		if Mode == 1: 
			print("--------------------------------------")
			print("           WELCOME CUSTOMER           ")
			print("--------------------------------------")
			print("To show our products press 1")
			print("--------------------------------------")
			print("To buy from our products press 2")
			print("--------------------------------------")
			print("To print the bill press 3")
			print("--------------------------------------")
			print("To exit press 0")
			Customer_Choice= int (input())
			print("--------------------------------------")
			#1- Customer choose to show products
			if Customer_Choice == 1:
				#Printing products , cost and quaintity 
				for n in range(len(Item)) and range(len(Cost)) and range(len(Quantity)):
					print ("Item" ,n+1,"is:",Item[n],"\nThe cost of each unit is:",Cost[n],"\nThe availabe Quantity is:",Quantity[n])
					print("--------------------------------------")
					
			#2- Customer choose to buy from the existed products	
			elif Customer_Choice == 2:
				print("Please select the item")
				Item_Choice= str (input())
				flag=0
				
				#2.1- Searching for the product in the item list
				for n in range(len(Item)):
					if Item_Choice == Item[n]:
						flag=1
						break
						
				#2.2- If the product is found the customer should enter the quantity needed
				if flag == 1:
					print("Please enter the quintity needed")
					Quantity_Choice= int (input())
					#2.2.1- Checking if the quantity enough 
					#2.2.2- Subtracting it from the quantity of the product in the shop 
					#2.2.3- then calculating the cost
					if (Quantity_Choice<=Quantity[n]):
						Quantity[n]=Quantity[n]-Quantity_Choice
						Total_Cost=Total_Cost+(Quantity_Choice*Cost[n])
						
					else:
						print("Not enough quantity")
					
				
				else:
					print("Wrong Item")
				
			#3- Customer choose to print the bill	
			elif Customer_Choice == 3:
				if Total_Cost == 0:
					print("No items selected")
				else:
					print("Your bill is:",Total_Cost)
					
			#4- Customer choose to exit
			elif Customer_Choice == 0:
				print("Thanks for Using ITI Shop")
				break
			#5- Customer enter wrong number
			else:
				print("wrong choice please select a number from 1 to 4")
#***********************************************************************************************#
#**************************                Owner Mode                 **************************#
#***********************************************************************************************#
		elif Mode == 2:
			print("--------------------------------------")
			print("            WELCOME OWNER            ")
			print("      Please Enter Your Password      ")
			Password= str (input()) #Password for admins
			if Password == "12345": #checking the password
				print("--------------------------------------")
				print("To add product press 1")
				print("--------------------------------------")
				print("To show products press 2")
				print("--------------------------------------")
				print("To change cost press 3")
				print("--------------------------------------")
				print("To exist press 0")
				Owner_Choice= int (input())
				
				#1- Owner choose to add a product
				if Owner_Choice == 1:
					#1.1- Asking the owner to add the product name
					print("Please enter the product name")
					Product_Name=str(input())
					Item.append(Product_Name)
					#1.2- Asking the owner to add the product cost
					print("Please enter the product cost")
					Product_Cost=int(input())
					Cost.append(Product_Cost)
					#1.3- Asking the owner to add the product quantity
					print("Please enter the product quantity")
					Product_Quantity=int(input())
					Quantity.append(Product_Quantity)
					print("The Product Added Successfully")
				
				#2- Owner choose to print the products
				elif Owner_Choice == 2:
					for n in range(len(Item)) and range(len(Cost)) and range(len(Quantity)):
						print ("Item" ,n+1,"is:",Item[n],"\nThe cost of each unit is:",Cost[n],"\nThe availabe Quantity is:",Quantity[n])
						print("--------------------------------------")
						
				#2- Owner choose to change a product cost 	
				elif Owner_Choice == 3:
					print("Please enter the product name that you want to change its cost")
					ProductChangedCost= str (input())
					flag1=0
					#2.1 Searching for the product
					for n in range(len(Item)):
						if ProductChangedCost == Item[n]:
							flag=1
							i=n #Saving this product index
							break
					#2.2 If the product found the owner is asked to add the new cost		
					if flag == 1:
						print("please enter the new cost")
						New_cost=int (input())
						Cost[i]=New_cost #Edit the new cost into the cost list
						print("The Cost Changed Successfully")
						
					else:
						print("Item Does Not Exist")
			
			
				elif Owner_Choice == 0:
					print("Thanks for Using ITI Shop")
					break
				
				#2- Owner entered a wrong choice 
				else :
					print("Wrong Choice please try again")
				
				
			else:
				print("Wrong Password Try again")
#***********************************************************************************************#
#**************************                Exist Mode                 **************************#
#***********************************************************************************************#	
		elif Mode == 0:
			print("Thanks for Using ITI Shop")
			break
#***********************************************************************************************#
#**************************             Wrong Mode Choice             **************************#
#***********************************************************************************************#				
		else:
			print("Wrong Choice please try again")
##################################################
# File Name				 : PasswordManager.py	 #
# Author				 : Namis Mohamed Ibrahim #
# Date of Development	 : 20th March 2022		 #
##################################################

																							# Defining font colours as variables to be used later
font1 = '\033[34m' 																			# BLUE FONT
font2 = '\033[30m'																			# BLACK FONT
font3 = '\033[31m'																			# RED FONT
font4 = '\033[36m'																			# CYAN FONT
font5 = '\033[35m'																			# MAGENTA FONT
fontB = '\033[1m'																			# BOLD FONT
fontR = '\033[0m'																			# RESET FONT

def menu():																					# Defining Menu as a Function
	print("")
	print(font1 + fontB + ('-'*5) + 'PASSWORD MANAGER MENU'+('-'*5) + fontR)				# Password Manager Menu Title
	print(font2 + "\n[1] Input New Credentials")											# Menu Option 1 = To input New credentials
	print("[2] View Stored Credentials")													# Menu Option 2 = To view stored credentials
	print("[3] Exit the Program" + fontR)													# Menu Option 3 = To exit from menu

menu()																						# Calling Menu Function
option = input(font4 + '\nPlease Select a number from the Menu Above? ' + fontR)			# Prompts User to enter a number from the Main Menu

while option !='3':																			# The following Codes are run if the user doesn't select number 3 in the Menu
	
	if option == '1':																		# Opens a series of prompts to add new credentials when menu option 1 is selected
		
		print("\n")
		website = input("Enter the name of the Website: ")									# Prompts the user to enter their website/URL and saves it under variable called website
		print("")
		username = input("Enter your username: ")											# Prompts the user to enter their username and saves it under variable called username
		print("")
		password = input("Enter your password: ")											# Prompts the user to enter their password and saves it under variable called password
		
		file = open("storedCredentials.txt", "a")											# Creates a text file called storedCredentials.txt for appending (a)
		file.write(f"{website : ^20}|{username : ^30}|{password : ^20} |:")					# Writes the entered website, username & password in the text file
		file.close()																		# closes the file

	elif option =='2':																		# Displays stored credentials in a readable format when menu option 2 is selected
		
		print()
		print(font1 + fontB + '*'*78)	
		print(f"|{'WEBSITE' : ^23}|{'USERNAME' : ^30}|{'PASSWORD' : ^20} |")				# Prints WEBSITE | USERNAME | PASSWORD in Blue bold Font & with spacing as specified
		print('*'*78 + fontR)																# Underlines the heading with * symbols
		
		file = open("storedCredentials.txt", "r")											# Opens storedCredentials text file for reading
		
		data = file.read()																	# "Data" variable reads and takes in all the text in the file
		data = data.split(":")																# "Data" variable splits the text and converts it into a list array
		data = sorted(data)																	# "Data" List is sorted alphabetically
		
		for i, val in enumerate(data):														# Prints the Data list in Alphabetical order 
    			print([i], val)		
		print('-'*78)
		file.close()

	else:
		print(font3 + "\nInvalid Option\n" + fontR)											# Prints Invalid Entry Message when any other text is entered, apart from 1, 2 & 3
		
	print()
	menu()
	option = input(font4 + "\nPlease select a number from the Menu again? " + fontR)

print(font5 + "\nThanks for using the Password Manager Program created by Namis. Goodbye! \n" + fontR) # Exits the menu when Menu option 3 is selected & displays the following message
  

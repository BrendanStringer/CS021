# Brendan L. Stringer
# CS 021
# Charge Account Validation 

# This program will ask the user to enter a charge account number and then see if it is a vailid one. 

def main(): 


	try: 

		# Get the possible charge account number
		possAccountNumber = int(input('Please enter a charge account nubmer: '))

		# Open the file of charge account numbers and read them into a list while stripping off the \n and making it an int
		validNumbers = open('charge_accounts.txt', 'r')
		validList = []
		for accountNumber in validNumbers: 
			validList.append(int(accountNumber.rstrip('\n')))

		# Search for the possAccountNumber in the validList
		if possAccountNumber not in validList: 
			print('The account number you are looking for does not exist. Please try another.')
		else: 
			print('You have entered a valid account number.')

		# Close the account number file 
		validNumbers.close()

	# Except error where a string is entered. 
	except ValueError as err: 
		print('You have entered an invalid account number.')
		print('The error message is displayed below.')
		print(err)

	except IOError as err: 
		print('The charge_accounts.txt file cannot be located.')
		print('Please verify that it exists and is named correctly')

	except Exception as err: 
		print('An unknown error has occured.')
		print(err)

main()


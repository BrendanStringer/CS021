# Brendan L. Stringer 
# CS 021 
# Telephone .py 

# This program will convert between alphebtical phone numbers and numberical phone numbers. 

# Define the main functions 
def main(): 

	# Start error handling
	try: 

		# Get the phone number from the user
		phone_number = input('Input the phone number in this format XXX-XXX-XXXX: ')

		# New number 
		new_number = []

		# Keep the first three digits the same and the first -
		new_number.append(phone_number[0])
		new_number.append(phone_number[1]) 
		new_number.append(phone_number[2])
		new_number.append(phone_number[3])  

		# Convert the phone number 
		for index in [4, 5, 6, 7, 8, 9, 10, 11]: 
			if phone_number[index].upper() == 'A' or phone_number[index].upper() == 'B' or phone_number[index].upper() == 'C':
				new_number.append('2')

			elif phone_number[index].upper() == 'D' or phone_number[index].upper() == 'E' or phone_number[index].upper() == 'F': 
				new_number.append('3')

			elif phone_number[index].upper() == 'G' or phone_number[index].upper() == 'H' or phone_number[index].upper() == 'I': 
				new_number.append('4')

			elif phone_number[index].upper() == 'J' or phone_number[index].upper() == 'K' or phone_number[index].upper() == 'L': 
				new_number.append('5')

			elif phone_number[index].upper() == 'M' or phone_number[index].upper() == 'N' or phone_number[index].upper() == 'O': 
				new_number.append('6')

			elif phone_number[index].upper() == 'P' or phone_number[index].upper() == 'Q' or phone_number[index].upper() == 'R' or phone_number[index].upper() == 'S':
				new_number.append('7')

			elif phone_number[index].upper() == 'T' or phone_number[index].upper() == 'U' or phone_number[index].upper() == 'V': 
				new_number.append('8')

			elif phone_number[index].upper() == 'W' or phone_number[index].upper() == 'X' or phone_number[index].upper() == 'Y' or phone_number[index].upper() == 'Z': 
				new_number.append('10')

			else: 
				new_number.append('-')


		# Make the list into a string
		string_list = ''.join(new_number)

		# Print the string	
		print('The number is: ', string_list)

	except IndexError as err: 
		print('The number you entered was not long enough.')

	except Exception as err: 
		print('There was an nknown error.')

main()







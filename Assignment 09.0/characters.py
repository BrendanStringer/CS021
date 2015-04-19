# Brendan L. Stringer 
# CS 021
# characters.py

# This program will parse a large text file. 

# Define the main function
def main(): 

	# Start error checking
	try:

		# Start the counters
		lowerCount = 0
		upperCount = 0
		digitCount = 0
		spaceCount = 0

		# Get the file name 
		filename = input('Please input the filename you want to parse: ')

		# Open the file. 
		searchFile = open(filename, 'r')

		for string in searchFile: 
			for char in string: 
				if char.islower(): 
					lowerCount += 1
				elif char.isupper(): 
					upperCount += 1
				elif char.isdigit(): 
					digitCount += 1
				elif char.isspace(): 
					spaceCount += 1

		print('\n')
		print('Filename: ', filename)
		print('Lower Case: ', lowerCount)
		print('Upper Case: ', upperCount)
		print('Digits : ', digitCount)
		print('Space :', spaceCount)

	except FileNotFoundError as err: 
		print('Please make sure you entered the correct file name.')

	except Exception as err: 
		print('There was an unknown error.')
		print(err)


main()

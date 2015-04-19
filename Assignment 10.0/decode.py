# Brendan L. Stringer 
# CS 021 
# decode.py 

# This program will replace any instances of a string with the specified coded character 

# Ask the user for thier input 
def getChoice():

	print('Welcome to my encryption program.')
	print('You can choose to encrypt a file or decrypt a file.')
	print('Would you like to:')
	print('1. Encrypt a file.')
	print('2. Decrypt a file.')
	choice = input('Your choice: ')

	return choice

# start the main function
def main(): 

	# Start Error Handling
	try: 

		# Start the code dictionary 
		encCode = {}
		decCode = {}

		# Open the codes files 
		codeKey = open('codes.txt', 'r')

		# Populate the codes dictionary 
		for indKey in codeKey: 

			encCode[indKey[0]] = indKey[2]
			decCode[indKey[2]] = indKey[0]

		# Get the users choice
		choice = getChoice()

		# Encrypt a file 
		if choice == '1': 

			# Get the input and output file names from the user 
			inFile = input('Enter the name of the input file. ')
			outFile = input('Enter the name of the output file. ')
			print('Writing encrypted data to', outFile)

			# Open the files
			inputFile = open(inFile, 'r')
			outputFile = open(outFile, 'w')

			# Convert the input file 
			# Index through the lines
			for line in inputFile: 

				# Start the encrypted list for each line as you index into each line
				encryptList = []

				# index through each character in the string
				for i in line: 
					
					# See if we can encrypt the charachter
					if i in encCode: 

						# Encrypt the letter
						encryptList.append(encCode[i])

					# Just pass the character through
					else: 
						encryptList.append(i)

				# Join the line which is a list into one string & Write the line to the output file
				oneString = ''.join(encryptList)
				outputFile.write(oneString)

				# Close all the files
				inputFile.close()
				outputFile.close()
				
		# Decrypt a file
		if choice == '2': 

			# Get the input file name from the user
			inFile = input('Enter the name of the input file. ')
			print('The decrypted contents of the file are: ')

			# Open the input file 
			inputFile = open(inFile, 'r')

			# Index through each line 
			for line in inputFile: 

				# Start the decrypted list
				decryptList = []

				# Index through each character 
				for i in line: 

					# Can the character be encrypted
					if i in decCode: 

						# Decrypt the letter 
						decryptList.append(decCode[i])

					else: 

						# Just pass the character through
						decryptList.append(i)

				oneString = ''.join(decyptList)
				print(oneString)

	# Error Handling
	except FileNotFoundError as err: 
		print('Please check you file name.')

	except Exception as err: 
		print('An unknown error occured.')
		print(err)

# run the main function 
main()


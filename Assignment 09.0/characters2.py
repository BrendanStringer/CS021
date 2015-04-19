# Brendan L. Stringer
# CS 021 
# Characters 2 python 

# This program will parse a string for the most common character. 

# Open the main function
def main(): 

	# Start exception handling
	try: 
		# Get the user input 
		testString = input('Enter a string: ')
		testString = testString.upper()

		# Start the variables. 
		letList = []
		countList = []
		maxList = []

		# Add all the letters in the string to a list 
		for char in testString: 
			if char not in letList: 
				if char != ' ':
					letList.append(char)

		# Check how many of 
		for letter in letList: 
			countList.append(testString.count(letter))

		# Get the max occurances 
		maxVal = max(countList)

		# Put every occurance of the max in a list of its own 
		index = 0
		while index < len(letList): 
			if countList[index] == maxVal: 
				maxList.append(letList[index])
			index += 1

		# Print the max list
		print('The most frequently occuring letter(s) are: ',maxList)

	# Add some exception handling
	except ValueError as err: 
		print('Please enter a string.')

	except Exception as err: 
		print('An unknown error occured.')
		print(err)

# Start the main function
main()	
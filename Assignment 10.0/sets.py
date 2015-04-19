# Brendan L. Stringer 
# CS 021
# sets.py 

# This will compare two programs

# Start the main program 
def main(): 

	try:

		# Get the file names from the user 
		file1 = input('Please enter the first file name: ')
		file2 = input('Please enter the second file name: ')

		# Open the files 
		firstFile = open(file1, 'r')
		secondFile = open(file2, 'r')

		# Start the list 
		set1 = set()
		set2 = set()

		# Put the files into sets 
		for line in firstFile:

			line = line.lower()
			set1.update(line.split())

		# Put the second file into a set. 
		for line in secondFile: 

			line = line.lower()
			set2.update(line.split())

		# Close the files 
		firstFile.close()
		secondFile.close()

		# Compare each file
		uniqueWords = set1.union(set2)
		intersectionWords = set1.intersection(set2)
		onlySetOne = set1.difference(set2)
		onlySetTwo = set2.difference(set1)
		notInBoth = onlySetOne.union(onlySetTwo)
		
		print('All words')
		print(uniqueWords)
		print('\n')
		print('Words only in both')
		print(intersectionWords)
		print('\n')
		print('Words only in set 1')
		print(onlySetOne)
		print('\n')
		print('Words only in set 2')
		print(onlySetTwo)
		print('\n')
		print('Words not in both')
		print(notInBoth)

	except FileNotFoundError as err: 
		print('Please check your file names.')

	except Exception as err: 
		print('An unknown error was found.')
		print(err)

main()




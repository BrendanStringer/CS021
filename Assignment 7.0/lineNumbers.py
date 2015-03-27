#Brendan L. Stringer 
#CS 021
#lineNumbers.py

#This program will print this function with line numbers while handling errors gracefully. 

def main(): 

	#Open error handling
	try:

		#Get the file name from the user
		programName = input('Enter the program name you want to read from. ')

		#Open the file to read from
		readProgram = open(programName, 'r')

		#Strip the .py file extension 
		programName = programName.rstrip('py')

		#Open the file to write to
		writeProgram = open('ln_' + programName + 'txt', 'w')

		#Initialize the line counter 
		count = 1

		#Print the contents of programName
		for line in readProgram: 

			#Write the line of code to the write file
			writeProgram.write(str(count) + ': ' + line)

			#Advance the line counter 
			count += 1 

		#Close the files 
		readProgram.close()
		writeProgram.close()

	#Here is all the errors are handled 
	except NameError as err:
		print('\n')
		print('Please check the syntax of your file name.')
		print('The error message is displayed below.')
		print(err)
		print('\n')

	except IOError as err: 
		print('\n')
		print('The file you specified does not exist.')
		print('Please check the syntax of your input.')
		print('The error message is displayed below.')
		print(err)
		print('\n')

	except Exception as err: 
		print('\n')
		print('There was an unknown error.')
		print('The error message is displayed below.')
		print(err)
		print('\n')

#Run the main funciton
main()
#Brendan L. Stringer 
#CS 021 
#kinetic.py 

#Determine a moving objects kenetic energy. 

def main(): 

	# # Open the exception handling
	try:

		# Get user input
		mass = float(input('Please enter the mass of the object in kilograms: '))
		velocity = float(input('Please enter the veloctiy of the object in meters per second: '))

		# Input validation
		while mass < 0: 
			print('Please enter a positive value for mass.')
			mass = float(input('Please enter the mass of the object in kilograms: '))

		while velocity < 0: 
			print('Please enter a positive value for velocity.')
			velocity = float(input('Please enter the veloctiy of the object in meters per second: '))		

		# Perform calculations
		keneticEnergy = .5 * mass * (velocity ** 2)

		#Print the results
		print('The kenetic energy is ' + str(keneticEnergy) + ' Joules')

	except NameError as err: 
		print('\n')
		print('You did not enter a valid number.')
		print('Please check the syntax of your inputs.')
		print('The error message is displayed below.')
		print(err)
		print('\n')

	except ValueError as err: 
		print('\n')
		print('You did not enter a valid number.')
		print('Please check the syntax of your inputs.')
		print('The error message is displayed below.')
		print(err)
		print('\n')

	except Exception as err: 
		print('\n')
		print('An unknown error was encountered.')
		print('The error message is found below. ')
		print(err)
		print('\n')

main()
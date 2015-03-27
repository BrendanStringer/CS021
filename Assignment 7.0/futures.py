#Brendan L. Stringer 
#CS 021
#futures.py Text 5.19

#This program will future worth of some money if the user inputs 
#P = present Value 
#i = monthly intrest rate 
#t = number of months 
#using this function 
#F = P * ( 1 + i ) ** t

#####----- DEFINE FUNCTIONS -----#####

#get user input
def getInput(): 

	P = float(input('Please enter the preset worth: $'))
	i = float(input('Please enter the interest rate: %'))
	t = float(input('Please enter the number of months: '))

	return P,i,t

#this function will validate the user input for each value
def validateInput(P,i,t): 

	#validate P
	while P <= 0: 

		print('The present worth must be greater than zero.')
		P = float(input('Please enter the present worth: $'))

	#validte i 
	while i < 0 or i > 100: 

		print('Your interest rate must be between 0 and 100 percent')
		i = float(input('Please enter the interest rate: %'))

	#validate t
	while t < 0: 

		print('The number of months must be greater than zero')
		t = float(input('Please enter the number of months: '))

	return P,i,t

#this will print the results to the user
def printResults(P,i,t,F):
	print('Your account information:')
	print('Present Value: $', format(P, '0.2f'))
	print('Interest Rate: ', format(i, '0.1f'), '%')
	print('Number of Months ', format(t, '0.0f'))
	print('The future value of your account is: $', format(F, '0.2f'))


#the main function will perform all the functions
def main():

	#Get the user input
	P,i,t = getInput()

	#Validate the user input
	P,i,t = validateInput(P,i,t)

	#Perform the Calculations
	F = P * (1 + (i/100)) ** t

	#print the results 
	printResults(P,i,t,F)

#####----- RUN MAIN -----#####

#run the main function
main()


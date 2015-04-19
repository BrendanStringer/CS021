#Brendan L. Stringer 
#CS 021
#Assignment 5.1 Textbook 5.4

#Write a program that asks the user to enter the monthly costs for the following expenses 
#incured from operating his or her automobiel: loan payment, insurance, gas, oil, tires, and 
#maintenance. The program should then display the total monthly cost of these expenses, and the 
#total annual cost of these expenses. 

#####----- DEFINE FUNCTIONS -----#####

#getInfo will get all the user input for the program
def getInfo(): 
	loan = float(input('What is your loan payment? '))
	insurance = float(input('How much do you pay in insurance? '))
	gas = float(input('How much do you spend on gas? '))
	oil = float(input('How much do you spend on oil? '))
	tires = float(input('How much do you spend on tires? '))
	maintenance = float(input('How much do you spend on maintenance? '))

	return loan, insurance, gas, oil, tires, maintenance

#showExpenses will add up the total expenses and then print them
def showExpenses(loan, insurance, gas, oil, tires, maintenance):
	totalMonth = loan + insurance + gas + oil + tires + maintenance
	totalYear = totalMonth * 12

	print('Total monthly expense: $',format(totalMonth, '0.2f'))
	print('Total yearly expense: $',format(totalYear, '0.2f'))

#main will run all the other functions
def main():
	loan, insurance, gas, oil, tires, maintenance = getInfo()

	showExpenses(loan, insurance, gas, oil, tires, maintenance)

#####----- RUN YOUR FUNCTION -----#####

main()




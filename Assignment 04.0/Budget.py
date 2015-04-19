#Brendan L. Stringer
#CS 021
#Budget.py Assignemnt 4.0

#This program will allow the user to enter a budget and sum up all the expenses. 
#At the end it will determine how much of the budget is left. 

#####----- GET INFORMATION FROM USER -----#####

#Get Budget from the user
Budget = float(input('Please input your budget. '))	


#####----- SET DEFAULT VALUES FOR VARIABLES -----#####

#Set a value for Expense
Expense = 1 

#Set a value for Spent
Spent = 0


#####----- CALCULATE BUDGET -----#####

while Expense != 0: 
	
	#Ask the user for an expense
	Expense =  float(input('Enter an amount spent (0 to quit): '))

	#Calculate the rolling total amount spent
	Spent += Expense


#####----- PRINT THE RESULTS -----#####

# Print information about their budget and what they spent
print('You Budgeted: $', format(Budget, '.2f'))
print('You Spent: $', format(Spent, '.2f'))

if Spent < Budget: 

	#Calculate how much under budget the user is
	Diff = Budget - Spent

	#Print difference 
	print('Congraduations you were $', format(Diff, '.2f'), 'under budget.')

elif Spent > Budget:

	#Calcualte how much over budget the user is
	Diff = Spent - Budget

	#Print difference
	print('Oh no, you were $', format(Diff, '.2f'), 'over budget.')

else:
	print('That was close, you hit your budget exactly.')


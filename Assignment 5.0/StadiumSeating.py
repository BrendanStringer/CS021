#Brendan L. Stringer
#CS 021
#Assignment 5.2 Text 5.7

#There are three seating categories at a staium. For a softball game, Class A seats cost $20, 
#Class B seats cost $15, and Class C seats cost 10. Write a program that asks how may tickets 
#for each class of seats were sold, and then displays the amount of income generated from ticket
#sales. 

#####----- SET CONSTANTS -----#####

COST_A = 20
COST_B = 15
COST_C = 10

#####----- DEFINE FUNCTIONS -----#####

#getInfo will get all the information from the user
def getInfo():

	classA = int(input('How many class A seats were sold? '))
	classB = int(input('How many class B seats were sold? '))
	classC = int(input('How many class C seats were sold? '))

	return classA, classB, classC

#showIncome will generate the total income generated
def showIncome(classA, classB, classC, COST_A, COST_B, COST_C):

	#Calculate total cost for each seat class
	totalA = COST_A * classA
	totalB = COST_B * classB
	totalC = COST_C * classC

	#Calculate the total income
	totalIncome = totalA + totalB + totalC

	#Print the data
	print('The total income from class A seats is: $', format(totalA, '0.2f'))
	print('The total income from class B seats is: $', format(totalB, '0.2f'))
	print('The total income from class C seats is: $', format(totalC, '0.2f'))
	print('The total income was: $',format(totalIncome, '0.2f'))

#define the main function
def main():
	
	#Get user input  
	classA, classB, classC = getInfo()

	#Perform Calcs and print data
	showIncome(classA, classB, classC, COST_A, COST_B, COST_C)

#####----- RUN THE CALCULATIONS -----#####
main()







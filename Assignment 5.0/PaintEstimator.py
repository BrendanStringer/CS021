#Brendan L. Stringer 
#CS 021
#Assignment 5.3 Text 5.8

#A painting company has determined that for every 112 square feet of wall space, one gallong of 
#paint and eight hours of labor will be required. the company charges $35.00 per hour for labor.
# Write a program that asks fthe user to enter the square feet of wall spacet obe painted and 
#the price of the paint per gallon. The program should display the following data: 
#The number of gallons of paint required 
#The hours of labor required 
#The cost of the paint 
#The cost of the labor 
#The total cost of the paint job. 


#####----- DEFINE CONSTANTS -----#####
HOUR_LABOR = 35
SQUARE_FOOT_PER_GAL = 112
HOUR_PER_GAL = 8

#####----- IMPORT FUNCTIONS -----#####
import math

#####----- DEFINE FUNCTIONS -----#####

#getInfo gets the user input 
def getInfo(): 
	squareFeet = float(input('Please enter the total square footage: '))
	perGallonCost = float(input('Please enter the cost per gallon of paint: '))

	return squareFeet, perGallonCost

#costEstimate calculates and prints the cost estimate
def costEstimate(squareFeet, perGallonCost, HOUR_LABOR, SQUARE_FOOT_PER_GAL, HOUR_PER_GAL):

	#find number of gallons needed 
	totalNumGal = math.ceil(squareFeet / SQUARE_FOOT_PER_GAL)

	#find labor hours needed
	totalNumLabor = math.ceil((squareFeet / SQUARE_FOOT_PER_GAL) * HOUR_PER_GAL)

	#find cost of paint
	totalCostPaint = totalNumGal * perGallonCost

	#find labor cost
	totalCostLabor = totalNumLabor * HOUR_LABOR

	#find total cost
	totalCost = totalCostPaint + totalCostLabor

	#print the results
	print('Gallons of paint: ', format(totalNumGal, '0.0f'))
	print('Hours of Labor: ', format(totalNumLabor, '0.0f'))
	print('Cost of paint: $', format(totalCostPaint, '0.2f'))
	print('Cost of labor: $', format(totalCostLabor, '0.2f'))
	print('Total Cost: $', format(totalCost, '0.2f'))

#main function
def main(): 
	squareFeet, perGallonCost = getInfo()
	costEstimate(squareFeet, perGallonCost, HOUR_LABOR, SQUARE_FOOT_PER_GAL, HOUR_PER_GAL)

#####----- RUN THE FUNCTION -----#####
main()




#Brendan L. Stringer 
#CS 021 
#Rainfall.py Assignment 4.3

#The program collects data about the average rainfall over a number of years. 


#####----- SET DEFAULT VALUES -----#####

#Assign values to variables
totalRain = 0


#####----- GET USER INPUT -----#####

#Input total number of years
totalYears = int(input('Enter the total number of years: '))


#####----- PERFORM CALCULATIONS -----#####

#For loop for each year
for i in range(1, totalYears+1): 
	print('For year ', format(i, '.0f'))

	#For loop for each month
	for n in range(1, 13): 

		#Get rainfall for each month
		monthRain = float(input('Enter the rainfall amount for month ' + str(n) + ':'))

		#Calculate the total rainfall
		totalRain += monthRain

#Calculate the number of months total 
numMonths = totalYears * 12 

#Calculate the average rain per month
aveRain = totalRain / numMonths


#####----- PRINT RESULTS -----#####

#Print the results
print('For ',format(numMonths, '.0f'),'months')
print('Total rainfall ', format(totalRain,'.2f'))
print('Average rainfall ',format(aveRain,'.2f'))




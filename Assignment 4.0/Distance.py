#Brendan L. Stringer
#CS 021 
#Distance.py Assignment 4.1

#Print and calculate the distance traveled in a formatted table.

#####----- ASK FOR AND VALIDATE VARIABLES -----#####

#Get speed from the user
speed = float(input('Enter your speed in mph: '))

#Validate the speed input
while speed < 0: 

	#Print Error Message
	print('Please enter a speed that is above 0mph ')
	speed = float(input('Enter you speed in mph '))

#Get the time traveled from the user
time = int(input('Enter number of hours traveled: '))

#Validate time traveled
while time < 0: 

	#Print error message
	print('Please enter a time that is above 0 hours ')
	time = float(input('Enter the number of hours traveled '))

#####----- PERFORM CALCULATIONS AND PRINT TABLE -----#####

#Print the Table headers
print('Hour\tDistance Travled')
print('------------------------')

#Calculate time traveled each hour
for i in range(1, time+1):
	
	#Calculate the distance
	distance = i * speed

	#Print the next line in the table
	print(format(i,'.0f'),'\t',format(distance,'.2f'),'miles')


#####----- END -----#####
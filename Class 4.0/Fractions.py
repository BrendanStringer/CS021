#Brendan L. Stringer
#CS 021
#Algorithm Workbench 05

#Write a loop that calculates the total of the following series of numbers: 1/30 + 2/29 + 3/28 ... 30/1

#Assign a value to Total
Total = 0

#Assign a value to Den
Den = 30

#Start the loop
for i in range(1, 31, 1):

	#Calculate the Numerator and denomerator
	Num = i

	#Find the Sum of the Num / Den
	Total += Num / Den

	#Update the Den
	Den -= 1

	#Print the rolling total
	print('The total so far is ', format(Total, '.2f'))

#Print the final total
print('The Total is ', format(Total, '.2f'))
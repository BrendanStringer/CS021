#Brendan L. Stringer 
#CS 021
#Algorithm Workbench 01

# Write a while loop that lets the user enter a number. The number should be multiplied by 10, and the result assigned to a variable named product. The Loop should iterate as long as the product is less than 100. 

#Define Product
Product = 0

while Product <= 100:
	
	#Ask the user to input a number
	Number = float(input('Please input a number. '))

	#Performe calculations to determine what "Product" is
	Product += Number * 10

	#Print the product
	print('Your product is ', format(Product, '.2f'))

#Print a message when the product is over 100
print('Your product has exceeded 100')

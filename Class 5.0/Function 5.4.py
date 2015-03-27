#Brendan L. Stringer 
#CS 021
#Function 5.4

#Define the main function 
def main(): 
	get_name()
	print('Hello',name) #this causes an error 

#Define get_name
def get_name():
	name = input('Enter your name: ')

#Call the main function 
main()
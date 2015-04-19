#Brendan Stringer 
#CS 021
#Assignment 3.1
#This program will calculate a person's BMI and determine if it is within the correct range. 

#Get input from the user
WEIGHT = int(input('What is your weight in pounds? '))
HEIGHT = int(input('What is your height in inches? '))

#Is weight < 50 lbs
if WEIGHT < 50: 
    print('You cannot weigh < 50 lbs')

#Is height < 48 inches
elif HEIGHT < 48: 
    print('You cannot be less than 48 inches tall')

#Variables are valid
else:
    
    #Perform BMI Calculation
    BMI = WEIGHT * 703.0 / (HEIGHT * HEIGHT)

    #Print BMI
    print('Your BMI is ', format(BMI, '.2f'))

    #Print information regarding the users BMI
    if BMI < 18.5: 
        print('You are underweight')
    elif BMI > 25: 
        print('You are overweight')
    else:
        print('You are the optimal weight')

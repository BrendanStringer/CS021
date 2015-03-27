#Brendan Stringer 
#CS 021
#Assignment 3.0
#This program will turn a mass into a weight and determine if an object is too heavy or not.

#Get user input 
MASS = float(input('Please input the mass of the object in kilograms '))

#Determine if a netagive mass was used
if Mass < 0: 
    print('You cannot enter a netagive Mass')

else:
    #Convert it into weight in newtons
    WEIGHT = MASS * 9.9

    #Print information regarding the calculation
    if WEIGHT > 500:
        print('The object is too heavy, it weighs more than 500 newtons')
    
    elif WEIGHT < 100: 
        print('The object is too light, it weighs less than 100 newtons')
    
    else:
        print('The object weighs ', format(WEIGHT,'.2f'), 'newtons')


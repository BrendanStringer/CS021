#Brendan Stringer 
#CS021 
#Assignment 2.0
#This program should convert celcius to farenheit and display the output to two decimal points. 

#Request the temperature in celcius from the user
CEL = float(input('Please input the termperature in celcius that you would like to convert to farenheit    '))

#Perform the calculations
FAR = 1.8 * CEL + 32

#Print the output
print(format(FAR,'5.2f'))
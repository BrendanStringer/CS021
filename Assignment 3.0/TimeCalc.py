#Brendan Stringer 
#CS021
#Assignment 3.0
#This program will convert time

#Get user variable (number of seconds)
NumSeconds = int(input("Input the number of seconds "))

if NumSeconds < 0: 
    print('Please enter a positive number of seconds')

else:
    HrSec = NumSeconds % 86400
    Day = (NumSeconds - HrSec) / 86400
    MinSec = HrSec % 3600
    Hour = (HrSec - MinSec) / 3600
    Sec = MinSec % 60 
    Min = (MinSec - Sec) / 60

    print(format(Day, '.1f'), 'Days, ', format(Hour, '.1f'), 'Hours, ', format(Min, '.1f'), 'Minutes, ', format(Sec, '.1f'), 'Seconds')


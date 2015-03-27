#Brendan L. Stringer
#CS 021 
#game21.py Play a game of 21 

#####----- IMPORT FUNCTIONS -----#####
import random

#####----- DEFINE FUNCTIONS ------#####

#this will roll the dice and return the sum
def rollDice(): 
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)

        roll = d1 + d2

        return roll

#This asks if the user would like to continue
def getResponce():

        choice = input('Do you want to roll? ')

        return choice

#this determines if the user would like to roll again
def detWinner(playPoints, compPoints): 

        print('Player Points: ', format(playPoints, '0.0f'))
        print('Computer Points: ', format(compPoints, '0.0f'))

        if compPoints > 21: 
                print('The computer has bust, Player wins!')
                
        elif playPoints > compPoints: 
                print('Player has beaten the computer!')
                
        elif playPoints == compPoints: 
                print('Player has tied with the computer')
                
        else:
                print('Player has lost to the computer.')

#what happens when the user busts
def bust(playPoints): 

        print('The player has exceeded 21 points. You loose')

#main function
def main(): 

        ##### Initialize Variables ######
        playPoints = 0
        compPoints = 0

        ##### Start the game #####

        while playPoints < 21:

                #Ask if the player would like to roll
                choice = getResponce()

                if choice == 'y': 

                        #roll for the player
                        roll = rollDice()
                        playPoints += roll
                        print('Points: ', format(playPoints, '0.0f'))

                        #roll for the computer
                        roll = rollDice()
                        compPoints += roll

                else: 

                        detWinner(playPoints, compPoints)
                        break

        if playPoints > 21:
                bust(playPoints)

#####----- START THE MAIN FUNCTION -----#####

main()





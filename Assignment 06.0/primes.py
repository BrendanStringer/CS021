#Brendan L. Stringer
#CS 021 
#primes.py text 5-17

#Display all the prime numbers between one and one hundred

#####----- INITIALIZE VARIABLES -----#####
primeList = [2,3]
possPrime = 4

#####----- DEFINE FUNCTIONS -----#####

def isPrime(possPrime, primeList): 

	primeFlag = True

	for prime in primeList: 

		if possPrime % prime == 0: 
			primeFlag = False 
			break

	return primeFlag

def printResults(primeList):

	print(primeList)

def main(primeList, possPrime):

	while possPrime <= 100: 

		primeFlag = isPrime(possPrime, primeList)

		if primeFlag == True:

			primeList.append(possPrime)

		possPrime += 1

	printResults(primeList)

main(primeList, possPrime)
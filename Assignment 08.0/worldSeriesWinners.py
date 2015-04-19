# Brendan L. Stringer 
# CS 021 
# World Series Winners 

# This program will allow the user to enter the name of a baseball team and it will tell them how many times that team has won the world series between 1993 and 2009. 

def main(): 

	# Start error handling
	try: 

		# Get the name of the team from the user
		teamName = str(input('What team would you like to search for? '))

		# Load the teams into a list
		worldSeriesWinners = open('worldSeriesWinners.txt', 'r')
		winnerList = []
		for winner in worldSeriesWinners: 
			winnerList.append(winner.rstrip('\n'))
		worldSeriesWinners.close()

		# Prime the winCount
		winCount = 0

		# Check to see how many times the team has won
		for nextWinner in winnerList: 

			# If the nextWinner matches the teamName add 1 to the winCount
			if nextWinner == teamName: 
				winCount += 1

		# Print the results 
		print('The ' + teamName + ' has won ' + str(winCount) + ' time(s).')

		# Add an additional note if the winCount == 0
		if winCount == 0: 
			print('Please make sure you typed your team name correctly')

	# Error handling
	except IOError as err: 
		print('The worldSeriesWinners file does not exist.')
		print('Please make sure it is in the correct directory.')
		print(err)

	except NameError as err: 
		print('The name you entered is incorrect.')
		print('Please try again')
		print(err)

	except Exception as err: 
		print('There was an unknown error.')
		print(err)

main()

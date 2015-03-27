# Brendan L. Stringer 
# CS 021 
# Exam Grader 

# This program will grade a student's exam based on a text file. Then it will output whether or not the student passed along with the incorrect answer numbers. 

def main(): 

	try: 

		# zero
		ZERO = 0

		# Max Wrong
		MAX_INCORRECT = 5

		# Open the list of correct answers and read them to a list. 
		correctAnswers = open('correct_answers.txt', 'r')
		correctAnswerList = []
		for answer in correctAnswers: 
			correctAnswerList.append(answer.rstrip('\n'))
		correctAnswers.close()

		# Open the list of student answers and read them to a text file 
		studentAnswers = open('student_solution.txt', 'r')
		studentAnswerList = []
		for answer in studentAnswers: 
			studentAnswerList.append(answer.rstrip('\n'))
		studentAnswers.close()

		# Start the list that records the incorrect answers 
		incorrectAnswers = []

		# Compare the student's answers to the correct ones
		for index in range(len(correctAnswerList)): 

			if correctAnswerList[index] != studentAnswerList[index]: 
				incorrectAnswers.append(index)
		
		# Print the results
		if len(incorrectAnswers) == ZER0: 
			print('Congradulations you have passed with a 100%.')

		elif len(incorrectAnswers) >= MAX_INCORRECT: 
			print('Congradulations you have passed.')
			print('These are the questions you got wrong')
			for i in incorrectAnswers: 
				print('Number: ', format(i, '0.0f'))

		else: 
			print('I am sorry you have failed.')
			print('You got ' + format(len(incorrectAnswers), '0.0f') + ' wrong.') 
			print('These are the questions you got wrong.')
			for i in incorrectAnswers: 
				print('Number: ', format(i, '0.0f'))

	except IOError as err:
		print('One of your files does not exist.')
		print('Please verify that correct_answers.txt and student_solution.txt are in the correct directories.')
		print('The error message is displayed below.')
		print(err)

	except Exception as err: 
		print('An unknown error has occured.')
		print(err)

main()
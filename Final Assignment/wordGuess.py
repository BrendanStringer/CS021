# Brendan L. Stringer
# CS 021 Python 
# wordGuess.py

# This program will play a word guessing game with the user. 

# Import tkinter 
import tkinter
import random

# Design a function to display the Gui
class wordGuess:
	def __init__(self): 

		self.wordScramble()

		# Create the main window
		self.main_window = tkinter.Tk()
		self.main_window.wm_title('Guess The Word')

		# Create the frames
		self.word_frame = tkinter.Frame(self.main_window)
		self.input_frame = tkinter.Frame(self.main_window)	
		self.button_frame = tkinter.Frame(self.main_window)
		self.feedback_frame = tkinter.Frame(self.main_window)

		# Pack the Frames 
		self.word_frame.pack()
		self.input_frame.pack()
		self.button_frame.pack()
		self.feedback_frame.pack()

		# Create the word label
		self.word_label = tkinter.Label(self.word_frame, text='Your word to unscramble: ')
		self.scramble_label = tkinter.Label(self.word_frame, text=self.word_scramble)

		# Pack the word_frame 
		self.word_label.pack(side='left')
		self.scramble_label.pack(side='left')

		# Create the guess lable and entry 
		self.guess_label = tkinter.Label(self.input_frame, text='Your guess:')
		self.guess_entry = tkinter.Entry(self.input_frame, width=30)

		# Pack the input frame 
		self.guess_label.pack(side='left')
		self.guess_entry.pack(side='left')

		# Create the buttons
		self.guess_button = tkinter.Button(self.button_frame, text='Guess', command=self.checkGuess)
		self.giveUp_button = tkinter.Button(self.button_frame, text='Give Up', command=self.giveUp)
		self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

		# Pack the button frame 
		self.guess_button.pack(side='left')
		self.giveUp_button.pack(side='left')
		self.quit_button.pack(side='left')

		# Build the feedback labels 
		self.feedback = tkinter.StringVar()
		self.feedback.set('Game Underway')
		self.feedback_view = tkinter.Label(self.feedback_frame, textvariable=self.feedback)

		# Pack the feedback frame 
		self.feedback_view.pack()

		# Start the main loop
		tkinter.mainloop()

	# This function will select a word and the scramble it
	def wordScramble(self): 

		# Start error handling
		try: 

			# Open the dict file
			dict_file = open('dict.txt', 'r')

			# Create a blank dictionary list
			dictionary = []

			# Store all the values of dict.txt in a list  
			for w in dict_file: 
				dictionary.append(w)

			# Close the dictionary file 
			dict_file.close()

			# Choose a random value between 0 and the length of the dictionary
			index = random.randint(0,len(dictionary))

			# Assign that value to the random word
			self.word = dictionary[index]
			self.word = self.word.rstrip('\n')
			# print(self.word)

			# Start the word_scramble Variable
			self.word_scramble = self.word

			# Make sure it does not scramble it back into the word
			while self.word_scramble == self.word: 
				# Start the random word list
				self.word_scramble = []

				# Make a list to shuffle of the word 
				for letter in self.word: 
					self.word_scramble.append(letter)

				# Scramble the word 
				random.shuffle(self.word_scramble)
				self.word_scramble = ''.join(self.word_scramble)

			# Set the feedback
			self.feedback = 'Game Underway'

			# Start the Guess Counter
			self.gCount = 1

		# Close error handling
		except FileNotFoundError as err:
			self.feedback.set('dict.txt not found')
			self.word_scramble = 'ERR'

		except Exception as err: 
			self.word_scramble.set('ERR')
			self.feedback = 'error'

	# The Guess button is a callback for the checkGuess function
	# This function will validate the guesses made by the player
	def checkGuess(self): 

		# Get the guess 
		self.guess = str(self.guess_entry.get())
		self.guess = self.guess.lower()

		# Validate the guess
		if self.guess == '':
			self.feedback.set('Please enter a guess')

		# Handle a correct guess
		elif self.guess == self.word: 
			self.feedback.set('You Win!' + '\n' + 'It took you ' + format(self.gCount, '0.0f') + ' guess(es).')
			self.guess_entry.delete(0,'end')
			self.guess_button.config(state='disabled')
			self.giveUp_button.config(state='disabled')

		# Handle the incorrect guesses
		else: 
			self.feedback.set('Guess ' + format(self.gCount, '0.0f') + ': ' + self.guess + ' is incorrect')
			self.guess_entry.delete(0,'end')
			self.gCount += 1

			# Make sure they have not exceeded their number of guesses
			if self.gCount == 6: 
				self.feedback.set('You are out of guesses, the word is ' + self.word + '.')
				self.guess_button.config(state='disabled')
				self.giveUp_button.config(state='disabled')

	# The Give Up button is a callback for the giveUp function 
	# This function will display the unscrambled word for the player
	def giveUp(self): 

		# Disable the buttons
		self.guess_button.config(state='disabled')
		self.giveUp_button.config(state='disabled')

		# Provide the answer 
		self.feedback.set('The word is ' + self.word + '.')
		self.guess_entry.delete(0,'end')





playGame = wordGuess()
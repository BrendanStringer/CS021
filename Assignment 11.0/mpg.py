# Brendan L. Stringer 
# CS 021
# mpg.py 

import tkinter 

class mpg: 
	def __init__(self): 

		# Create the main window 
		self.main_window = tkinter.Tk()

		# Create the frames 
		self.input1_frame = tkinter.Frame(self.main_window)
		self.input2_frame = tkinter.Frame(self.main_window)
		self.answer_frame = tkinter.Frame(self.main_window)
		self.button_frame = tkinter.Frame(self.main_window)

		# Create the labels for each entry field
		self.gallons_label = tkinter.Label(self.input1_frame, text='Enter the number of gallons:')
		self.miles_label = tkinter.Label(self.input2_frame, text='Enter the number of miles:')

		# Create the entry fields for the input frame 
		self.gallons_entry = tkinter.Entry(self.input1_frame, width=10)
		self.miles_entry = tkinter.Entry(self.input2_frame, width=10)

		# Pack the input frame 
		self.gallons_label.pack(side='left')
		self.gallons_entry.pack(side='left')
		self.miles_label.pack(side='left')
		self.miles_entry.pack(side='left')

		# Creat the output label
		self.answer_label = tkinter.Label(self.answer_frame, text='Miles Per Gallon = ')
		self.answer = tkinter.StringVar()
		self.answer_view = tkinter.Label(self.answer_frame, textvariable=self.answer)

		# Pack the output label 
		self.answer_label.pack(side='left')
		self.answer_view.pack(side='left')

		# Create the buttons
		self.calc_button = tkinter.Button(self.button_frame, text='Calculate MPG', command=self.calc_mpg)
		self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

		# Pack the button frame 
		self.calc_button.pack(side='left')
		self.quit_button.pack(side='left')

		# Pack the frames 
		self.input1_frame.pack()
		self.input2_frame.pack()
		self.answer_frame.pack()
		self.button_frame.pack()

		# Start the tkinter main loop 
		tkinter.mainloop()

	# The calc_mpg function was a call back for the cacl_button widget 
	def calc_mpg(self):

		try: 
			# Get the user input
			self.gallons = float(self.gallons_entry.get())
			self.miles = float(self.miles_entry.get())

			# Perform Calculations
			self.ans = self.miles / self.gallons

			# Update the answer_view widget
			self.answer.set(format(self.ans,'0.2f'))

		except ValueError as err:
			self.answer.set('Invalid Input')

		except Exception as err:
			self.answer.set('Unknown Error')

# Create an instance of the function 
mpg_calculator = mpg()

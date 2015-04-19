# Brendan L. Stringer 
# Simple Math 
# This program is just to test some gui stuff I have been working on 

import tkinter

class simpleMathGUI: 
	def __init__(self):

		# Crete the main window 
		self.main_window = tkinter.Tk()

		# Create a few frames 
		self.title_frame = tkinter.Frame(self.main_window)
		self.number1_frame = tkinter.Frame(self.main_window)
		self.number2_frame = tkinter.Frame(self.main_window)
		self.answer_frame = tkinter.Frame(self.main_window)
		self.button_frame = tkinter.Frame(self.main_window)

		# Creat the title 
		self.main_title = tkinter.Label(self.title_frame, text='This program will add the two numbers')

		# Pack the main title 
		self.main_title.pack()

		# Create the number 1 widgets 
		self.number1_label = tkinter.Label(self.number1_frame, text='Please enter the first number.')
		self.number1_entry = tkinter.Entry(self.number1_frame, width=10)

		# Pack number1 frame 
		self.number1_label.pack(side='left')
		self.number1_entry.pack(side='left')

		# Create the number 2 widgets 
		self.number2_label = tkinter.Label(self.number2_frame, text='Please enter the second number.')
		self.number2_entry = tkinter.Entry(self.number2_frame, width=10)

		# Pack the number2 frame 
		self.number2_label.pack(side='left')
		self.number2_entry.pack(side='left')

		# Make the answer label 
		self.answer_label = tkinter.Label(self.answer_frame, text='The Sum is :')

		# Make the value variable
		self.total = tkinter.StringVar()

		# Create the label and associate it with the total object 
		self.sum_label = tkinter.Label(self.answer_frame, textvariable=self.total)

		# Pack the answer frame 
		self.answer_label.pack(side='left')
		self.sum_label.pack(side='left')

		# Create the calc button 
		self.calc_button = tkinter.Button(self.button_frame, text='Calculate', command=self.calc)

		# Create the quit button
		self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

		# Pack the button frame
		self.calc_button.pack(side='left')
		self.quit_button.pack(side='left')

		# Pack the frames 
		self.title_frame.pack()
		self.number1_frame.pack()
		self.number2_frame.pack()
		self.answer_frame.pack()
		self.button_frame.pack()

		# Start the main loop 
		tkinter.mainloop() 

	# The calc module is a callback to this fuction 
	def calc(self): 

		# Get the first value
		num1 = float(self.number1_entry.get())

		# Get the second value 
		num2 = float(self.number2_entry.get())

		# Perform the calc 
		total = num1 + num2

		# Update the display variable 
		self.total.set(total)

# Create an instance of simpleMathGUI
program = simpleMathGUI()
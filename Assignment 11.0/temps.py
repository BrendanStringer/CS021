# Brendan L. Stringer 
# CS 021 
# temps.py

import tkinter

class convertCelsius: 
	def __init__(self):

		# Create the main window 
		self.main_window = tkinter.Tk()

		# Create the Frames
		self.input_frame = tkinter.Frame(self.main_window)
		self.answer_frame = tkinter.Frame(self.main_window)
		self.button_frame = tkinter.Frame(self.main_window)

		# Pack the frames 
		self.input_frame.pack(side='left')
		self.answer_frame.pack(side='left')
		self.button_frame.pack(side='left')

		# Create the input label and entry 
		self.celsius_label = tkinter.Label(self.input_frame, text='Enter the Celsius temperature:')
		self.celsius_entry = tkinter.Entry(self.input_frame, width=10)

		# Pack the input frame 
		self.celsius_label.pack()
		self.celsius_entry.pack()

		# Create the fahrenheit label and answer 
		self.answer_label = tkinter.Label(self.answer_frame, text='Fahrenheit temperature:')
		self.ans = tkinter.StringVar()
		self.ans_label = tkinter.Label(self.answer_frame, textvariable=self.ans)

		# Pack the answer frame 
		self.answer_label.pack()
		self.ans_label.pack()

		# Create the buttons 
		self.calc_button = tkinter.Button(self.button_frame, text='Convert to Fahrenheit', command=self.convert)
		self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

		# Pack the buttons 
		self.calc_button.pack()
		self.quit_button.pack()

		# Start the main loop 
		tkinter.mainloop()

	# calc button is a callback to this function 
	def convert(self):

		try:

			# Get the celsius value
			self.cel = float(self.celsius_entry.get())

			# Convert to Farenheight
			self.far = 1.8 * self.cel + 32

			# Update the label
			self.ans.set(self.far)

		except ValueError as err: 
			self.ans.set('Invalide input')

		except Exception as err: 
			self.ans.set('ERROR')

# Create an instance of the convertCelsius class 
convert_stuff = convertCelsius() 
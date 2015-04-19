# Brendan L. Stringer 
# Simple Math 
# This program is just to test some gui stuff I have been working on 

class simpleMathGUI: 
	def __init__(self):

		# Crete the main window 
		self.main_window = tinkter.Tk()

		# Create a few frames 
		self.number1_frame = tkinter.Frame(self.main_window)
		self.number2_frame = tkinter.Frame(self.main_window)
		self.button_frame = tkinter.Frame(self.main_window)

		# Create the number 1 widgets 
		self.number1_label = tkinter.Label(self.number1_frame, text='Please enter the first number.')
		self.number1_entry = tkinter.Entry(self.number1_frame, width=10)

		# Pack number1 frame 
		self.number1_frame.pack(side='left')
		self.number1_entry.pack(side='left')

		# Create the number 2 widgets 
		self.number2_label = tkinter.Label(self.number2_frame, text='Please enter the second number.')
		self.number2_entry = tkinter.Entry(self.number2_entry, width=10)

		# Pack the number2 frame 
		self.number2_label.pack(side='left')
		self.number2_entry.pack(side='left')

		# Create the buttons 
		self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

		# Pack the button frame
		self.quit_button.pack()

		# Pack the frames 
		self.number1_frame.pack()
		self.number2_frame.pack()
		self.button_frame.pack()

		# Start the main loop 
		tkinter.mainloop()

# Create an instance of simpleMathGUI
program = simpleMathGUI()
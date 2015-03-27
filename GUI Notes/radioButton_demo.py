# Brendan Stringer 
# Radio Button Demo 

import tkinter 
import tkinter.messagebox 

class MyGUI: 
	def __init__(self): 

		# Create the main window 
		self.main_window = tkinter.Tk()

		# Create two frames 
		# One for the Radio Buttons and one for the regular buttons 
		self.top_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)

		# Create an IntVar object to use with the Radio Buttons 
		self.radio_var = tkinter.IntVar()

		# Set the IntVar object to 1
		self.radio_var.set(1)

		# Create the Radiobutton widgets in the top_frame
		self.rb1 = tkinter.Radiobutton(self.top_frame, text='Option 1', variable=self.radio_var, value=1) 
		self.rb2 = tkinter.Radiobutton(self.top_frame, text='Option 2', variable=self.radio_var, value=2)
		self.rb3 = tkinter.Radiobutton(self.top_frame, text='Option 3', variable=self.radio_var, value=3)

		# Pack the radio buttons 
		self.rb1.pack()
		self.rb2.pack()
		self.rb3.pack()

		# Create and OK button and a quit button 
		self.ok_button = tkinter.Button(self.bottom_frame, text='Okay', command=self.show_choice)
		self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

		# Pack the Quit an Okay buttons 
		self.ok_button.pack(side='left')
		self.quit_button.pack(side='left')

		# Pack the frames 
		self.top_frame.pack()
		self.bottom_frame.pack()

		# Start the mainloop 
		tkinter.mainloop()

		# The show_choice is a callback function for the Okay button
	def show_choice(self): 

		tkinter.messagebox.showinfo('Selection', 'You selected and option ' + str(self.radio_var.get()))

# Create an instance of the MyGUI class 
my_gui = MyGUI()
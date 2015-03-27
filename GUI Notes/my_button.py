# This program demonstrates the button widget
# when the user clicks the button, an info dialog box is displayed. 

import tkinter
import tkinter.messagebox

class MyGUI: 
	def __init__(self): 
		# Create the main window widget
		self.main_window = tkinter.Tk()

		# Create a button widget. The text "Click Me!" should appear on the face of the button. 
		# The do_something method should be executed when the user clicks the button. 
		self.my_button = tkinter.Button(self.main_window, text='Click Me!', command=self.do_something)

		# Pack the button 
		self.my_button.pack()

		# Enter the tkinter main loop. 
		tkinter.mainloop()

	# The do_something method is a callback function for the button widget. 

	def do_something(self): 
		# Display an info dialog box.
		tkinter.messagebox.showinfo('Response','Thanks for clicking the button.') 

# Create an instance of the MyGUI Class. 
my_gui = MyGUI()
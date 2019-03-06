Scale	
The Scale widget provides a graphical slider object that allows you to select values from a specific scale.

Syntax:	
w = Scale ( master, option, ... )

Parameters:	 
• master: This represents the parent window.
• options: Here is the list of most commonly used options for this widget. These options can be used as key-value pairs separated by commas.

Example:S
import tkinter
root =tkinter.Tk()
scale1 = tkinter.Scale( root, from_=0,to=42 )
scale1.pack()
scale2=tkinter.Scale( root, from_=100,to=200,orient="horizontal" )
scale2.pack()
root.mainloop()

Example:S1
import tkinter
def sel():
	selection = "Value = " + str(var.get())
	label.config(text = selection)

root =tkinter.Tk()
var =tkinter.DoubleVar()
scale = tkinter.Scale( root, variable = var )
scale.pack()
button =tkinter.Button(root, text="Get Scale Value", command=sel)
button.pack()
label =tkinter.Label(root)
label.pack()
root.mainloop()

--------------------------------------------------------------------------------------------------------------

Spinbox	
The Spinbox widget is a variant of the standard Tkinter Entry widget, which can be used to select from a fixed
number of values.

Syntax:	
w = Spinbox( master, option, ... )

Parameters:
• master: This represents the parent window.
• options: Here is the list of most commonly used options for this widget. These options can be used as key-
value pairs separated by commas.

Example:Sp1
import tkinter
root =tkinter.Tk()
w = tkinter.Spinbox(root, from_=0, to=10)
w.pack()

root.mainloop()

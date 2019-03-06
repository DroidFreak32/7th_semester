Checkbutton	
       The Checkbutton widget is used to display a number of options to a user as toggle buttons. The user can then
select one or more options by clicking the button corresponding to each option.

Syntax:	
 w = Checkbutton ( master, option, ... )

Parameters:	
• master: This represents the parent window.
• options: Here is the list of most commonly used options for this widget. These options can be used as key-
value pairs separated by commas.

Options:
activebackground ------> Background color when the checkbutton is under the cursor.
activeforeground ------> Foreground color when the checkbutton is under the cursor.
bg --------> The normal background color displayed behind the label and indicator.
bd --------> The size of the border around the indicator. Default is 2 pixels.
command --------> A procedure to be called every time the user changes the state of this checkbutton.
font ----------> The font used for the text.
fg --------> The color used to render the text.
height --------> The number of lines of text on the checkbutton. Default is 1.
offvalue ---------> Normally, a checkbutton's associated control variable will be set to 0 when it is cleared (off).
You can supply an alternate value for the off state by setting offvalue to that value.
onvalue --------> Normally, a checkbutton's associated control variable will be set to 1 when it is set (on). You
can supply an alternate value for the on state by setting onvalue to that value.
padx --------> How much space to leave to the left and right of the checkbutton and text. Default is 1 pixel.
pady ---------> How much space to leave above and below the checkbutton and text. Default is 1 pixel.
state --------> The default is state=NORMAL, but you can use state=DISABLED to gray out the control and
make it unresponsive. If the cursor is currently over the checkbutton, the state is ACTIVE.
variable -----------> The control variable that tracks the current state of the checkbutton. Normally this variable is
an IntVar, and 0 means cleared and 1 means set, but see the offvalue and onvalue options
above.

Example:c1
import tkinter
root = tkinter.Tk()
CheckVar1 = tkinter.IntVar()
CheckVar2 = tkinter.IntVar()

C1 =tkinter.Checkbutton(root, text = "Music", variable = CheckVar1, onvalue = 1, offvalue = 0)
C2 =tkinter.Checkbutton(root, text = "Video", variable = CheckVar2, onvalue = 1, offvalue = 0)

C1.pack()
C2.pack()

root.mainloop()
----------------------------------------------------------------------------------
Example:c2
import tkinter 
def display():
	if(CheckVar1.get() and CheckVar2.get()):	
		print("Checkbox1=",CheckVar1.get())
		print("Checkbox2=",CheckVar2.get())
	elif(CheckVar2.get()):
		print("Checkbox2=",CheckVar2.get())
	elif(CheckVar1.get()):
		print("Checkbox1=",CheckVar1.get())
	else:
		print("Not selected any")

root = tkinter.Tk()
CheckVar1 = tkinter.IntVar()
CheckVar2 = tkinter.IntVar()

C1 =tkinter.Checkbutton(root, text = "Music", variable = CheckVar1, onvalue = 1, offvalue = 0)
C2 =tkinter.Checkbutton(root, text = "Video", variable = CheckVar2, onvalue = 1, offvalue = 0)

B1=tkinter.Button(root, text="Submit",command=display)

C1.pack()
C2.pack()
B1.pack()

root.mainloop()

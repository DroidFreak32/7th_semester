Radiobutton	
  
	This widget implements a multiple-choice button, which is a way to offer many possible selections to the user and
lets user choose only one of them.

Syntax:
       w = Radiobutton ( master, option, ...)

Parameters:
• master: This represents the parent window.
• options: Here is the list of most commonly used options for this widget. These options can be used as key-value pairs separated by commas.

Options:
activebackground ----> The background color when the mouse is over the radiobutton.
activeforeground -----> The foreground color when the mouse is over the radiobutton.
Bg -----> The normal background color behind the indicator and label.
Borderwidth -----> The size of the border around the indicator part itself. Default is 2 pixels.
Command -----> A procedure to be called every time the user changes the state of this radiobutton.
Cursor ------> If you set this option to a cursor name (arrow, dot etc.), the mouse cursor will change to that
pattern when it is over the radiobutton.
Font ------> The font used for the text.
Fg -------> The color used to render the text.
Height ------> The number of lines (not pixels) of text on the radiobutton. Default is 1.
highlightbackground -----> The color of the focus highlight when the radiobutton does not have focus.
Highlightcolor -------> The color of the focus highlight when the radiobutton has the focus.
Image -----> To display a graphic image instead of text for this radiobutton, set this option to an image
object.
Justify -----> If the text contains multiple lines, this option controls how the text is justified: CENTER (the
default), LEFT, or RIGHT.
Padx ------> How much space to leave to the left and right of the radiobutton and text. Default is 1.
Pady ------> How much space to leave above and below the radiobutton and text. Default is 1.
Value -----> When a radiobutton is turned on by the user, its control variable is set to its current value
option. If the control variable is an IntVar, give each radiobutton in the group a different
integer value option. If the control variable is aStringVar, give each radiobutton a different
string value option.
Variable ----> The control variable that this radiobutton shares with the other radiobuttons in the group.
This can be either an IntVar or a StringVar.
State -----> The default is state=NORMAL, but you can set state=DISABLED to gray out the control and
make it unresponsive. If the cursor is currently over the radiobutton, the state is ACTIVE.
Text -------> The label displayed next to the radiobutton. Use newlines ("\n") to display multiple lines of
text.
Textvariable ------> To slave the text displayed in a label widget to a control variable of classStringVar, set this
option to that variable

Example:r1a
import tkinter 

root = tkinter.Tk()

R1 = tkinter.Radiobutton(root, text="Option 1")
R2 = tkinter.Radiobutton(root, text="Option 2")
R3 = tkinter.Radiobutton(root, text="Option 3")

R1.pack()
R2.pack()
R3.pack()

root.mainloop()
--------------------------------------------------------------------------
Example:r1b
import tkinter 

root = tkinter.Tk()
var = tkinter.IntVar()

R1 = tkinter.Radiobutton(root, text="Option 1", variable=var, value=1)
R2 = tkinter.Radiobutton(root, text="Option 2", variable=var, value=2)
R3 = tkinter.Radiobutton(root, text="Option 3", variable=var, value=3)

R1.pack()
R2.pack()
R3.pack()

root.mainloop()
-----------------------------------------------------------------------------
Example:r2
import tkinter 
def sel():
	selection = "You selected the option " + str(var.get())
	label.config(text = selection)

root = tkinter.Tk()
var = tkinter.IntVar()

R1 = tkinter.Radiobutton(root, text="Option 1", variable=var, value=1,command=sel)
R2 = tkinter.Radiobutton(root, text="Option 2", variable=var, value=2,command=sel)
R3 = tkinter.Radiobutton(root, text="Option 3", variable=var, value=3,command=sel)

label = tkinter.Label(root)

R1.pack()
R2.pack()
R3.pack()
label.pack()

root.mainloop()




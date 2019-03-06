Entry(textbox):
The Entry widget is used to accept single-line text strings from a user.

Syntax:
w = Entry( master, option, ... )

Parameters:	
• master: This represents the parent window.
• options: Here is the list of most commonly used options for this widget. These options can be used as key-value pairs separated by commas.

Options:
bg ----------> The normal background color displayed behind the label and indicator.
bd ----------> The size of the border around the indicator. Default is 2 pixels.
command ---------- >A procedure to be called every time the user changes the state of this checkbutton.
cursor ----------> If you set this option to a cursor name (arrow, dot etc.), the mouse cursor will change to that pattern when it is over the checkbutton.
font ----------> The font used for the text.
fg -----------> The color used to render the text.
justify ---------> If the text contains multiple lines, this option controls how the text is justified: CENTER, LEFT, or RIGHT.
selectbackground ----------> The background color to use displaying selected text.
selectborderwidth ----------> The width of the border to use around selected text. The default is one pixel.
selectforeground ----------> The foreground (text) color of selected text.
textvariable ------------> In order to be able to retrieve the current text from your entry widget, you must set this optionto an instance of the StringVar class.
show ----------> Normally, the characters that the user types appear in the entry. To make a .password. entry that echoes each character as an asterisk, set show="*".

Example:E1
import tkinter
window = tkinter.Tk()
label = tkinter.Label(window, text="Username")
entry = tkinter.Entry(window)
label.pack()
entry.pack()
window.mainloop()

Example:E2
import tkinter
window = tkinter.Tk()
label = tkinter.Label(window, text="Username")
entry = tkinter.Entry(window)
label.pack(side="left")
entry.pack(side="left")
window.mainloop()

Example:E3
import tkinter
window = tkinter.Tk()
var1=tkinter.StringVar()
var2=tkinter.StringVar()

def display():
	var2.set(var1.get())	

label1 = tkinter.Label(window, text="Username")
entry1 = tkinter.Entry(window,textvariable=var1,show="*")

label2 = tkinter.Label(window, text="Hi,")
entry2=tkinter.Entry(window,textvariable=var2)

button= tkinter.Button(window, text ="Submit",command=display)

label1.pack()
entry1.pack()
button.pack()
label2.pack(side="left")
entry2.pack(side="left")

window.mainloop()




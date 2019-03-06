Label	
      This widget implements a display box where you can place text or images. The text displayed by this widget can be updated at any time you want.

Syntax
w = Label ( master, option, ... )

Parameters:	 
• master: This represents the parent window.
• options: Here is the list of most commonly used options for this widget. These options can be used as key-value pairs separated by commas.

Options:
anchor ----------> This options controls where the text is positioned if the widget has more space than the text needs. The default is anchor=CENTER, which centers the text in the available space.
bg ----------> The normal background color displayed behind the label and indicator.
bitmap --------> Set this option equal to a bitmap or image object and the label will display that graphic.
bd -----------> The size of the border around the indicator. Default is 2 pixels.
cursor ----------> If you set this option to a cursor name (arrow, dot etc.), the mouse cursor will change to that pattern when it is over the checkbutton.
font -----------> If you are displaying text in this label (with the text or textvariable option, the font option specifies in what font that text will be displayed.
fg -----------> If you are displaying text or a bitmap in this label, this option specifies the color of the text. Ifyou are displaying a bitmap, this is the color that will appear at the position of the 1-bits in the bitmap.
image -----------> To display a static image in the label widget, set this option to an image object.

Example:l1
import tkinter
window = tkinter.Tk()
label = tkinter.Label(window, text="Hey, How are you ?")
label.pack()
window.mainloop()

Example:l2
import tkinter
window = tkinter.Tk()
label = tkinter.Label(window, text="Hey, How are you ?",bg="orange",fg="black",font="Timesnewroman" ,bd=4)
label.pack()
window.mainloop()

Example:l3 #using variable class 
import tkinter
window = tkinter.Tk()
var=tkinter.StringVar() #for integer - IntVar()
label = tkinter.Label(window, textvariable=var,bg="orange",fg="black",font="Timesnewroman" ,bd=4)
var.set("Hi, Helloooo")
label.pack()
window.mainloop()



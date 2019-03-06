tkMessageBox module (messagebox)
	The tkMessageBox module(messagebox) is used to display message boxes in your applications. This module provides a number of functions that you can use to display an appropriate message. Some of these functions are showinfo, showwarning, showerror, askquestion, askokcancel, askyesno and
askretryignore

Syntax:
  tkMessageBox.FunctionName(title, message [, options])

Parameters:
• FunctionName: This is the name of the appropriate message box function.
• title: This is the text to be displayed in the title bar of a message box.
• message: This is the text to be displayed as a message.
• options: options are alternative choices that you may use to tailor a standard message box. Some of the options that you can use are default and parent. The default option is used to specify the default button, such as ABORT, RETRY, or IGNORE in the message box. The parent option is used to specify the window on top of which the message box is to be displayed.

You could use one of the following functions with dialogue box:
• showinfo()
• showwarning()
• showerror ()
• askquestion()
• askokcancel()
• askyesno ()
• askretrycancel ()

Example:m1
import tkinter
import tkinter.messagebox
root = tkinter.Tk()
def hello():
  tkinter.messagebox.showinfo("Say Hello", "Hello World")
B1 =  tkinter.Button(root, text = "Say Hello", command = hello)
B1.pack()
root.mainloop()

Example:m2
import tkinter
import tkinter.messagebox
root = tkinter.Tk()
def hello():
  tkinter.messagebox.showerror("Error", "Something Wrong")
B1 =  tkinter.Button(root, text = "submit", command = hello)
B1.pack()
root.mainloop()

Example:txt1
import tkinter
import tkinter.messagebox
root = tkinter.Tk()
var=tkinter.StringVar()
def hello():
  tkinter.messagebox.showinfo(message="Hello "+var.get())
entry=tkinter.Entry(root,textvariable=var)
B1 =  tkinter.Button(root, text = "Say Hello", command = hello)
entry.pack()
B1.pack()
root.mainloop()

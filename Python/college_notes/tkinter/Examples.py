Ex:1
import tkinter
window = tkinter.Tk()

def display():
	label1.config(fg="black",bg="orange")	

label1 = tkinter.Label(window, text="NUM1",fg="green",bg="yellow")
button= tkinter.Button(window, text ="Submit",command=display)

label1.pack()
button.pack()

window.mainloop()

Ex:2
import tkinter
window = tkinter.Tk()

def display():
	label1.config(text="Goooood",fg="green",bg="yellow")	

label1 = tkinter.Label(window, text="Hey, How are you????",fg="green",bg="yellow")
button= tkinter.Button(window, text ="Click",command=display)

label1.pack()
button.pack()

window.mainloop()

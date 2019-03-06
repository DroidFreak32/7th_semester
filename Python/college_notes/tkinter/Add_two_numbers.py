import tkinter
window = tkinter.Tk()
var1=tkinter.IntVar()
var2=tkinter.IntVar()
var3=tkinter.IntVar()

def display():
	var3.set(var1.get()+var2.get())	

label1 = tkinter.Label(window, text="NUM1")
entry1 = tkinter.Entry(window,textvariable=var1)

label2 = tkinter.Label(window, text="NUM2")
entry2=tkinter.Entry(window,textvariable=var2)

label3 = tkinter.Label(window, text="Result")
entry3=tkinter.Entry(window,textvariable=var3)

button= tkinter.Button(window, text ="Submit",command=display)

label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
label3.pack()
entry3.pack()
button.pack()
window.mainloop()

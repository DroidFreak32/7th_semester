Button:
   The Button widget is used to display buttons in your application.

w = Button ( master, option=value, ... )

Parameters:	
• master: This represents the parent window.
• options: Here is the list of most commonly used options for this widget. These options can be used as key-value pairs separated by commas.

options:
activebackground -----------> Background color when the button is under the cursor.
activeforeground -----------> Foreground color when the button is under the cursor.
bd ------------> Border width in pixels. Default is 2.
bg ------------> Normal background color.
command ----------> Function or method to be called when the button is clicked.
fg -----------> Normal foreground (text) color.
font ----------> Text font to be used for the button's label.

Example: B1
import tkinter
window = tkinter.Tk()
button= tkinter.Button(window, text ="Hello")
button.pack()
window.mainloop()

Example: B2
import tkinter
window = tkinter.Tk()
button= tkinter.Button(window, text ="Hello",bd=5,bg="yellow",fg="red",font=20,justify="center",height=3)
button.pack()
window.mainloop()





















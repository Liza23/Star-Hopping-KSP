from tkinter import *

root = Tk()

# Creating a Label Widget
myLabel1 = Label(root, text="Interface")
myLabel2 = Label(root, text="Hello World")
# Shaving it onto the screen
# myLabel1.pack()

myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)

root.mainloop()

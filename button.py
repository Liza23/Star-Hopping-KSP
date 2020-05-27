from tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root, text="You clicked the button.")
	myLabel.pack()

myButton = Button(root, text="Click", command=myClick, fg="white", bg="blue")
myButton.pack()

#padx=50, pady=50: to resize the button
# state=DISABLED to disable button click

root.mainloop()

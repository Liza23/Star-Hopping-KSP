from tkinter import *

root = Tk()

initial = Label(root, text="Enter input here:")
initial.pack()

e = Entry(root, width=50, borderwidth=5, bg="pink")
e.pack()
#e.insert(0, "Enter your name: ")

def myClick():
	hello = "You entered " + e.get()
	#gets whatever has been written in the entry box
	myLabel = Label(root, text=hello)
	myLabel.pack()

myButton = Button(root, text="Click", command=myClick, fg="white", bg="peach puff")
myButton.pack()

#padx=50, pady=50: to resize the button
# state=DISABLED to disable button click

root.mainloop()

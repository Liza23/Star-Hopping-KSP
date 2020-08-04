from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.geometry("400x400")

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

label = Label(root, text=horizontal.get()).pack()

def slide():
	label = Label(root, text=horizontal.get()).pack()
	root.geometry(str(horizontal.get())+"x400")

btn = Button(root, text="Click here", command=slide).pack()

root.mainloop()
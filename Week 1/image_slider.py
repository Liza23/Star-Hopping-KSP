import cv2 as cv
import glob
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.geometry("400x400")


img1 = ImageTk.PhotoImage(Image.open("images/img1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("images/img2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("images/img3.jpg"))
img4 = ImageTk.PhotoImage(Image.open("images/img4.jpg"))
img5 = ImageTk.PhotoImage(Image.open("images/img5.jpg"))

image_list = [img1, img2, img3, img4, img5]

horizontal = Scale(root, from_=0, to=4, orient=HORIZONTAL)
horizontal.pack()

def slide():
	x = int(horizontal.get())
	img_label = Label(image=image_list[x])
	img_label.pack()

btn = Button(root, text="Click here", command=slide)
btn.pack()

btn_exit = Button(root, text="Exit", command=root.quit)
btn_exit.pack()

root.mainloop()
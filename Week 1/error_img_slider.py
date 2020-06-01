import cv2 as cv
import glob
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.geometry("400x400")

path = glob.glob("C:/Users/HP/Desktop/Ongoing Projects/Krittika Sumer Project_Hopping/images/*.jpg")
cv_img = []
for img in path:
    n = cv.imread(img)
    cv_img.append(n)

img_label = Label(image=cv_img)
img_label.pack()




	
root.mainloop()
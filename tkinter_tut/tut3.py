from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("733x434")

photo1 = PhotoImage(file=r"C:\Users\Mukesh Kumar\OneDrive\Pictures\Screenshots\Screenshot 2026-04-08 231232.png")
lab1 = Label(image=photo1)
lab1.pack()

#for JPG images
photo2 = Image.open(r"C:\Users\Mukesh Kumar\OneDrive\Pictures\Screenshots\Screenshot 2026-07-08 125327.jpeg")
image2 = ImageTk.PhotoImage(photo2)

#creating another label for the second image
lab2 = Label(image=image2)
lab2.pack()

root.mainloop()
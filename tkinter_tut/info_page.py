from tkinter import *
from PIL import Image, ImageTk

root = Tk()

salman = Image.open(r"C:\Python\tkinter_tut\Salman Khan.png")
img1 = ImageTk.PhotoImage(salman)
lab = Label(image=img1)
lab.pack()

root.mainloop()
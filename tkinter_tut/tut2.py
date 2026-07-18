from tkinter import *

root = Tk()

#formar: width x height
#root.geometry is used fo setting the size of the window
root.geometry("444x234")

#format: width, height
#root.minsize is used fo setting the min. size of the window
root.minsize(200, 100)

#format: width, height
#root.maxsize is used fo setting the max. size of the window
root.maxsize(1200, 988)

lab = Label(text="Hi guys! Welcome to my first GUI")
lab.pack()

root.mainloop()
from tkinter import *

root = Tk()

root.geometry("444x233")
root.title("My GUI With Code With Harry")

#important label options
#text - adds texts
#bd - background
#fg - foeground
#font - sets the font
#font=("roman", 19, "bold")
#font=("roman 19 bold")
#padx - x padding
#pady - y padding
#relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text="Loyola School, Telco, Jamshedpur, is a private Catholic primary and secondary school located \nin Jamshedpur, in the state of Jharkhand, India. Founded by the Jesuits in 2015, the school provides education to \nstudents from kindergarten through standard 12, and receives no government aid.", bg="red", fg="white", padx=45, pady=55, font=("comicsansms 9 bold"), borderwidth=3, relief=SUNKEN)

#imortant pack options
#anchor = nw
#side = top, bottom, left, right
#fill = "x"
#fill="y"
#padx
#pady

title_label.pack(side="left", fill="y",padx=30, pady=30)

root.mainloop()
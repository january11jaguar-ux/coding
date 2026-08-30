from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

btn = Button(root, text="scan for Virus", command=msg)
btn.place(x=40,y=80)

root.mainloop()
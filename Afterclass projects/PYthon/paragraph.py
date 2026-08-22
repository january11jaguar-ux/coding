from tkinter import*
from datetime import date

root = Tk()
root.title('getting started with Widgets')
root.geometry('600x500')

lbl = Label(text ="story time!", fg="white", bg="#6B1281", height=1 , width=300)

name_lbl = Label(text = "paragraph", bg= "#FC7DEE")
name_entry = Entry()

def display():
    name=name_entry.get()

    greet = "-"+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, date.today())
    
text_box = Text(height=3)

btn = Button(text ="Begin", command = display, height=1,bg="#E141E1", fg="white")

#organize the widgets
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()
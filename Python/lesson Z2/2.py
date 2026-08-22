from tkinter import*
from datetime import date

root = Tk()
root.title('getting started with Widgets')
root.geometry('400x300')

lbl = Label(text ="Hey There!", fg="white", bg="#6B1281", height=1 , width=300)

name_lbl = Label(text = "Full Name", bg= "#FC7DEE")
name_entry = Entry()

def display():
    name=name_entry.get()

    global Message
    Message = "wlecome to the Application! \n Today's date is: "
    greet = "Hello "+name+"\n"

    text_box.insert(END, greet)
    text_box.insert(END, Message)
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
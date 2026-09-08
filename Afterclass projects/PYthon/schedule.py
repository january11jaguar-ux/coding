from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Schedul Application")
root.configure(bg="forest green")
root.geometry("650x400")

upload = Image.open("Python/lesson Z6/pexels-codioful-6985199.jpg")
upload = upload.resize((300,300))
image= ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg="beige")
label.place(x=180, y=20)

label1=Label(
    root,
    text="Hey User! Welcome to Schedule Application",
    bg="beige"
)
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo(
        "Alert",
        "Do you want to start creating a schedule?"
    )
    if MsgBox == "ok":
        topwin()
button1 = Button(
    root, 
    text="Let's get started!",
    command=msg,
    bg="maroon",
    fg="white"
)
button1.place(x=260,y=360)

def topwin():
    top = Toplevel()
    top.title("Schedule application")
    top.configure(bg="violet")
    top.geometry("600x350+50+50")

    Label(
        top,
        text="Enter your schedule:",
        bg="violet",
        font=("Arial", 16)
    )

    entry = Entry(
        top,
        width=50,
        font=("Arial", 14)
    )

    def save_schedule():
        schedule = entry.get()
        print(schedule)
        messagebox.showinfo(
            "Schedule Saved",
            "Your schedule has been saved!"
        )

    btn = Button(
        top,
        text="Save Schedule",
        command=save_schedule,
        bg="maroon",
        fg="white"
    )
    btn.pack()
    entry.pack()
root.mainloop()
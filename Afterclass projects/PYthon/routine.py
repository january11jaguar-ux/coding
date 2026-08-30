import tkinter as tk
from tkinter import messagebox

routine = ["Homework", "Clean room", "Snack", "Read", "Prep for tomorrow"]
index = 0

def last_char(e):
    text = entry.get()
    label_last.config(text=f"Last: {text[-1] if text else '(none)'}")

def clicked(e):
    label_click.config(text="You clicked the routine area")

def next_task():
    global index
    if not entry.get().strip():
        messagebox.showwarning("Warning", "Please type a task first")
        return
    if index < len(routine):
        label_next.config(text=f"Next: {routine[index]}")
        index += 1
    else:
        label_next.config(text="Routine complete")

root = tk.Tk()
root.title("Routine Checker")

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)
entry.bind("<KeyRelease>", last_char)

label_last = tk.Label(root, text="Last: (none)", font=("Arial", 12))
label_last.pack()

area = tk.Label(root, text="Click here", bg="lightblue", width=20, height=2)
area.pack(pady=5)
area.bind("<Button-1>", clicked)

label_click = tk.Label(root, text="", font=("Arial", 12))
label_click.pack()

button = tk.Button(root, text="Next Task", font=("Arial", 14), command=next_task)
button.pack(pady=5)

label_next = tk.Label(root, text="", font=("Arial", 12))
label_next.pack()

root.mainloop()

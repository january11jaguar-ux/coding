from tkinter import *

root = Tk()
root.title('Number pad')
root.geometry('250x300')

nums = [[9,8,7],[6,5,4],[1,2,3],['#',0,'*']]

for i in range(4):
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i,weight=1, minsize=50)
    for j in range(0, 3):
        frame =Frame(
            master=root,
            relief=SUNKEN,
            borderwidth=10
        )
        frame.grid(row=i, column=j)
        label=Label(master=frame, text=nums[i][j], bg="beige")
        label.pack(padx=3, pady=3)
root.mainloop()
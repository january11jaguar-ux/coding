from tkinter import *

root = Tk()
root.title('i like the raised frame')
root.geometry('450x500')

nums = [[9,8,7],[6,5,4],[1,2,3],['#',0,'*']]

for i in range(4):
    root.columnconfigure(i, weight=3, minsize=75)
    root.rowconfigure(i,weight=3, minsize=50)
    for j in range(0, 3):
        frame =Frame(
            master=root,
            relief=RAISED,
            borderwidth=15
        )
        frame.grid(row=i, column=j)
        label=Label(master=frame, text=nums[i][j], bg="beige")
        label.pack(padx=5, pady=5)
root.mainloop()
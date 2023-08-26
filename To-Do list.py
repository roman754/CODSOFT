from tkinter import *
from tkinter.font import Font

root = Tk()
root.configure(bg="#000000")
root.title('To-Do List Application')
root.geometry("750x500")
font = Font(family="Arial", size=22, weight="bold")
frame = Frame(root)
frame.pack(pady=10)

list1 = Listbox(frame, font=font, width=40, height=7, bg="#FFFFFF", bd=0, fg="#5c4033", highlightthickness=0, selectbackground="#0000FF", activestyle="none")
list1.pack(side=LEFT, fill=BOTH)

a = Scrollbar(frame)
a.pack(side=RIGHT, fill=BOTH)
list1.config(yscrollcommand=a.set)
a.config(command=list1.yview)

entry = Entry(root, font=("Arial", 22), width=26, bg='#CDC9C9')
entry.pack(pady=20)

button = Frame(root, bg='#8B7B8B')
button.pack(pady=20)

def add_item():
    list1.insert(END,entry.get())
    entry.delete(0, END)
    
def del_item():
    list1.delete(ANCHOR)

add_button = Button(frame, text="Add Item", command=add_item, bg="#F5F5F5", font=("arial", 12))
add_button.pack()

del_button = Button(frame, text="Delete Item", command=del_item, bg="#F5F5F5", font=("arial", 12))
del_button.pack()

root.mainloop()

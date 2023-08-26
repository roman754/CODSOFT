from tkinter import *
import tkinter as tk

def btn_click(number):
    a=display.get()
    display.delete(0,tk.END)
    display.insert(tk.END,a+str(number))

def btn_clear():
    display.delete(0,tk.END)

def btn_equal():
    try:
        a=display.get()
        b=eval(a)
        display.delete(0,tk.END)
        display.insert(tk.END,b)
    except:
        display.delete(0,tk.END)
        display.insert(tk.END,"Error")
root=tk.Tk()
root.title("Calculator")

display=tk.Entry(root,width=25,justify=tk.RIGHT)
display.grid(row=0,column=0,columnspan=4)

b1=tk.Button(root,text='1',command=lambda: btn_click(1))
b1.grid(row=1,column=0)

b2=tk.Button(root,text='2',command=lambda: btn_click(2))
b2.grid(row=1,column=1)

b3=tk.Button(root,text='3',command=lambda: btn_click(3))
b3.grid(row=1,column=2)

b4=tk.Button(root,text='4',command=lambda: btn_click(4))
b4.grid(row=2,column=0)

b5=tk.Button(root,text='5',command=lambda: btn_click(5))
b5.grid(row=2,column=1)

b6=tk.Button(root,text='6',command=lambda: btn_click(6))
b6.grid(row=2,column=2)

b7=tk.Button(root,text='7',command=lambda: btn_click(7))
b7.grid(row=3,column=0)

b8=tk.Button(root,text='8',command=lambda: btn_click(8))
b8.grid(row=3,column=1)

b9=tk.Button(root,text='9',command=lambda: btn_click(9))
b9.grid(row=3,column=2)

b10=tk.Button(root,text='0',command=lambda: btn_click(0))
b10.grid(row=4,column=1)

b11=tk.Button(root,text='+',command=lambda: btn_click("+"))
b11.grid(row=1,column=3)

b12=tk.Button(root,text='-',command=lambda: btn_click("-"))
b12.grid(row=2,column=3)

b13=tk.Button(root,text='*',command=lambda: btn_click("*"))
b13.grid(row=3,column=3)

b14=tk.Button(root,text='/',command=lambda: btn_click("/"))
b14.grid(row=4,column=3)

b15=tk.Button(root,text='=',command=btn_equal)
b15.grid(row=4,column=2)

b16=tk.Button(root,text='C',command=btn_clear)
b16.grid(row=4,column=0)

root.mainloop()

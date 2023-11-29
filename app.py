from tkinter import *
from tkinter import messagebox
from math import sqrt


#For showing error when devide by zero
def show_error():
    messagebox.showerror("Devision by zero", "You cannot devide by zero")


def add():
    awnser = float(input_1.get()) + float(input_2.get())
    show_result.config(text=awnser)

def minus():
    awnser = float(input_1.get()) - float(input_2.get())
    show_result.config(text=awnser)

def multiply():
    awnser = float(input_1.get()) * float(input_2.get())
    show_result.config(text=awnser)

def devide():
    if int(input_2.get()) == 0:

        show_error()

    else:
        awnser = float(input_1.get()) / float(input_2.get())
        show_result.config(text=awnser, fg= "white")

def power(): 
    awnser = float(input_1.get()) ** float(input_2.get())
    show_result.config(text=awnser)

def square_root():
    awnser = sqrt(float(input_1.get()))
    show_result.config(text=awnser)

windows = Tk()
windows.title("Calculator")

Label(windows, text="Insert number 1 here:", bg="white").pack()
input_1 = Entry(windows)
input_1.pack()

Label(windows, text="Insert number 2 here:)", bg="white").pack()
input_2 = Entry(windows)
input_2.pack()

btn_add = Button(windows, text="+", command=add)
btn_add.pack()
btn_add.place(x=100, y=110)

btn_minus = Button(windows, text="-", command=minus)
btn_minus.pack()
btn_minus.place(x=200, y=110)

btn_multiply = Button(windows, text="x", command=multiply)
btn_multiply.pack()
btn_multiply.place(x=300, y=110)

btn_devide = Button(windows, text="÷", command=devide)
btn_devide.pack()
btn_devide.place(x=400, y=110)

btn_power = Button(windows, text="^", command=power)
btn_power.pack()
btn_power.place(x=200, y=150)

btn_squar_root= Button(windows, text="√", command=square_root)
btn_squar_root.pack()
btn_squar_root.place(x=300, y=150)

result_label = Label(windows, text="Result:")
result_label.pack()
result_label.place(x=250, y=250)
show_result = Label(windows, text="",font=('ubuntu', 28), bg="grey", width=18)
show_result.pack()
show_result.place(x=70, y=270)



windows.geometry("500x400")
windows.mainloop()

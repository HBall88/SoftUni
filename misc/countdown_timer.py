from tkinter import *
from time import strftime

root = Tk()
root.geometry("500x200")

root.title('Py_clock')


def time():
    string = strftime('%H:%M:%S %p')
    mark.config(text=string)
    mark.after(1000, time)


mark = Label(root,
             font=('calibri', 40, 'bold'),
             pady=150,
             foreground='black')
mark.pack(anchor='center')
time()

mainloop()
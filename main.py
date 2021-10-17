from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Digital Clock")

def time():
    string = strftime("%H:%M:%S %p")
    Label.config(text=string)
    Label.after(1000, time)

Label = Label(root, font=("Segoe UI", 70), background="#000", foreground="cyan")
Label.pack(anchor="center")
time()

mainloop()


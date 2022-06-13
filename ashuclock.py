from time import strftime
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

root = Tk()
root.title("Satyam clock")
root.resizable(0,0)
root.wm_iconbitmap('clock.ico')

def time():
	string = strftime(" %H:%M:%S %p ")
	lable.config(text=string)
	lable.after(1000, time)

lable = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
lable.pack()

time()
def message():
	if messagebox.askyesnocancel("Close", "Do you want to close?"):
		root.destroy()

root.protocol("WM_DELETE_WINDOW",message)

root.mainloop()
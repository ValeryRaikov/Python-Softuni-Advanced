# First python clock project with tkinter:

from tkinter import *
from time import strftime

# create tkinter window:
root = Tk()
root.title('Clock')
root.config(bg="red")

# function to display current time: 
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)
 
# additional stylization:
lbl = Label(root, font=('calibri', 50, 'bold'), background='skyblue', foreground='blue')
 
lbl.pack(anchor='center')
time()
 
mainloop()
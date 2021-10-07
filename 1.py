from tkinter import *
#import tkMessageBox
from screeninfo import get_monitors

def helloCallBack():
   print('-----')
screen = get_monitors()[0]
tk = Tk()
tk.geometry(str(screen.width) + "x" + str(screen.height))
l = Label(tk)
b = Button(tk, text ="Hello", command = helloCallBack)
b.place(relx=0.5, rely = 0.9)
tk.mainloop()

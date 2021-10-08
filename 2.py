from imutils.video import VideoStream
import cv2 as cv
import imutils
import time
import numpy as n
from PIL import Image as Img, ImageTk
from tkinter import *

with open('/home/pi/screen.txt') as f:
    lines = f.readlines()

x = int(lines[0])
y = int(lines[1])
w = int(lines[2])
h = int(lines[3])
#x = 100
#y = 200
#w = 320
#h = 240

def shutdownCallback():
    exec(open('shutdown.py').read())
vs1 = VideoStream(src=0).start()
vs2 = VideoStream(src=2).start()
time.sleep(1)
window = Tk()
#window.geometry(str(screen.width) + "x" + str(screen.height))
window.geometry("1024x768")

imageLabel1 = Label(window)
imageLabel2 = Label(window)
imageLabel1.pack()
imageLabel2.place(x=x, y=y, width=w, height=h)
b = Button(window, text="Power", command=shutdownCallback)

b.place(relx=0.5, rely=0.9, width=100, height=30)

#l.place(
#imageLabel.grid()

def show_frame():
    #frame1 = imutils.resize(vs1.read(), width=screen.width, height=screen.height)
    frame1 = imutils.resize(vs1.read(), width=1024, height=768)
    frame2 = imutils.resize(vs2.read(), width=w, height=h)
    # frame2 = imutils.resize(vs2.read(), width=w, height=h )

    #frame1[y:h+y,x:w+x] = frame2
    
    img1 = Img.fromarray(frame1)
    imgTk1 = ImageTk.PhotoImage(image=img1)
    imageLabel1.imgTk = imgTk1
    imageLabel1.configure(image=imgTk1)

    img2 = Img.fromarray(frame2)
    imgTk2 = ImageTk.PhotoImage(image=img2)
    imageLabel2.imgTk = imgTk2
    imageLabel2.configure(image=imgTk2)

    window.after(40, show_frame)
    
show_frame()
window.mainloop()

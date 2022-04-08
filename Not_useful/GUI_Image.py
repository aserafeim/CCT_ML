# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 05:31:26 2021

@author: aserafeim
"""
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title('Example')

# frame=Frame(root) #This can create empty space above and below
# frame.pack()


px = []
py = []


def leftclick(event):
    px.append(event.x)
    py.append(event.y)
    print('Left')
    return px,py
    
    


root.bind('<Button-1>',leftclick)


button_quit=Button(root,text='Exit',command=root.quit)

button_quit.pack()


my_img=ImageTk.PhotoImage(Image.open('CCT_4140.jpg'))
my_label=Label(image=my_img)
my_label.pack()





root.mainloop()

print(px, py)
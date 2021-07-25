# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 13:53:33 2021

@author: aserafeim
"""

from tkinter import *


root=Tk()

px = []
py = []


def leftclick(event):
    px.append(event.x)
    py.append(event.y)
    print('Left')
    return px,py
    
    

frame=Frame(root,height=300, width =300)
frame.bind('<Button-1>',leftclick)
frame.pack()

button_exit=Button(root,text='Exit',command=root.quit)
button_exit.pack()



root.mainloop()

print(px)
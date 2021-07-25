# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 18:31:45 2021

@author: aserafeim
"""

import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title('Example')

State=NONE

Temp_l=[]
px=[]
py=[]

def leftclick(event):
    px.append(event.x)
    py.append(event.y)
    print('Left')
    return px,py
    
def Tempreg():
    root.bind('<Button-1>',leftclick)
    global Temp_l
    if py != []:
        emp_l.append(py[-1])
        
    return Temp_l
    
    

#Temperature and time User inputs
Temp=Label(root,text='Temperature')
Temp.grid(row=1,column=0,padx=10, pady=10)

Temp1= Entry(root, width=10, borderwidth=5)
Temp1.grid(row=1, column=1, columnspan=1, padx=10, pady=10)

Temp2= Entry(root, width=10, borderwidth=5)
Temp2.grid(row=1, column=2, columnspan=1, padx=10, pady=10)

Temp_button=Button(root, text='register temp', command=Tempreg)
Temp_button.grid(row=1, column=3)

# print(State)

# if State=='Tempreg':
#     root.bind('<Button-1>',leftclick)
    # Temp_l=[py[0],py[1]]





button_quit=Button(root,text='Exit',command=root.quit)

button_quit.grid(row=2,column=0)


my_img=ImageTk.PhotoImage(Image.open('CCT_4140.jpg'))
my_label=Label(image=my_img)
my_label.grid(row=0, column=0)





root.mainloop()


# print

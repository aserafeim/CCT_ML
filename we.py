# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:53:05 2021

@author: alexs
"""
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("Title")
root.geometry('600x600')

def resize_image(event):
    global label
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open('CCT_4140.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)

root.mainloop()
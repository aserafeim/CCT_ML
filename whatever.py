# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 13:47:52 2021

@author: alexs
"""

from scipy.interpolate import interp1d
import numpy as np
from tkinter import filedialog as fd
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


filename = fd.askopenfilename()
my_img=ImageTk.PhotoImage(Image.open(filename))
my_label=Label(image=my_img)
my_label.grid(row=0, column=0,columnspan=5)
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 18:31:45 2021

@author: aserafeim
"""

import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog as fd
from scipy.interpolate import interp1d
from tkinter import ttk
import numpy as np
import math
import json


root = Tk()
root.title('Example')
root.iconbitmap('')

# Getting screen dimensions and setting window geometry

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
# root.geometry(str(int(screen_width/2))+'x'+str(int(screen_height/1.15)))

# Creating Tabs in the window

my_notebook = ttk.Notebook(root)
my_notebook.grid(row=0, column=0, columnspan=5, rowspan=5, sticky='NSEW')

Calibration_Frame = Frame(my_notebook, width=int(screen_width / 2), height=int(screen_height / 1.15))
Critical_Temp_Frame = Frame(my_notebook, width=int(screen_width/2), height=int(screen_height/1.15))
Composition_Frame = Frame(my_notebook, width=int(screen_width/2), height=int(screen_height/1.15))
Phasefraction_Frame = Frame(my_notebook, width=int(screen_width/2), height=int(screen_height/1.15))

my_notebook.add(Calibration_Frame, text='Calibration')
my_notebook.add(Critical_Temp_Frame, text='Critical Temp')
my_notebook.add(Composition_Frame, text='Composition_AustenitizationData_GrainSize')
my_notebook.add(Phasefraction_Frame, text='Phasefraction')

# Dynamically adjust rows and columns (Calibration Frame)

Grid.rowconfigure(Calibration_Frame, index=0, weight=1)
Grid.rowconfigure(Calibration_Frame, index=1, weight=1)
Grid.rowconfigure(Calibration_Frame, index=2, weight=1)
Grid.rowconfigure(Calibration_Frame, index=3, weight=1)


Grid.columnconfigure(Calibration_Frame, index=0, weight=1)
Grid.columnconfigure(Calibration_Frame, index=1, weight=1)
Grid.columnconfigure(Calibration_Frame, index=2, weight=1)
Grid.columnconfigure(Calibration_Frame, index=3, weight=1)
Grid.columnconfigure(Calibration_Frame, index=4, weight=1)

# Dynamically adjust rows and columns (Critical Temp Frame)

Grid.rowconfigure(Critical_Temp_Frame, index=0, weight=1)
Grid.rowconfigure(Critical_Temp_Frame, index=1, weight=1)
Grid.rowconfigure(Critical_Temp_Frame, index=2, weight=1)

Grid.columnconfigure(Critical_Temp_Frame, index=0, weight=1)
Grid.columnconfigure(Critical_Temp_Frame, index=1, weight=1)
Grid.columnconfigure(Critical_Temp_Frame, index=2, weight=1)
Grid.columnconfigure(Critical_Temp_Frame, index=3, weight=1)
Grid.columnconfigure(Critical_Temp_Frame, index=4, weight=1)

# Dynamically adjust rows and columns (Composition, Austenitization Data, Grain Size)

Grid.rowconfigure(Composition_Frame, index=0, weight=1)
Grid.rowconfigure(Composition_Frame, index=1, weight=1)
Grid.rowconfigure(Composition_Frame, index=2, weight=1)
Grid.rowconfigure(Composition_Frame, index=3, weight=1)
Grid.rowconfigure(Composition_Frame, index=4, weight=1)
Grid.rowconfigure(Composition_Frame, index=5, weight=1)
Grid.rowconfigure(Composition_Frame, index=6, weight=1)
Grid.rowconfigure(Composition_Frame, index=7, weight=1)

Grid.columnconfigure(Composition_Frame, index=0, weight=1)
Grid.columnconfigure(Composition_Frame, index=1, weight=1)
Grid.columnconfigure(Composition_Frame, index=2, weight=1)
Grid.columnconfigure(Composition_Frame, index=3, weight=1)
Grid.columnconfigure(Composition_Frame, index=4, weight=1)

# Dynamically adjust rows and columns (Phase Fractions)

Grid.rowconfigure(Phasefraction_Frame, index=0, weight=1)
Grid.rowconfigure(Phasefraction_Frame, index=1, weight=1)
Grid.rowconfigure(Phasefraction_Frame, index=2, weight=1)
Grid.rowconfigure(Phasefraction_Frame, index=3, weight=1)

Grid.columnconfigure(Phasefraction_Frame, index=0, weight=1)
Grid.columnconfigure(Phasefraction_Frame, index=1, weight=1)
Grid.columnconfigure(Phasefraction_Frame, index=2, weight=1)
Grid.columnconfigure(Phasefraction_Frame, index=3, weight=1)
Grid.columnconfigure(Phasefraction_Frame, index=4, weight=1)

# Defining containers

State=NONE
Status=False
Temp_l=[]
Time_l=[]
Ferr_l_t=[]
Ferr_l_T=[]
Pear_l_t=[]
Pear_l_T=[]
Bain_l_t=[]
Bain_l_T=[]
Pear_data={}
Ferr_data={}
Bain_data={}
px=[]
py=[]
Ms_Temp_l=[]
Ac_Temp_l=[]
Aus_Temp_l=[]
Ms_Temp_inp = {}
Ac_Temp_inp = {}
Grain_S_data = {}
Element_data = {}
# Carbon_data = {}
# Manganese_data = {}
Aus_Time_inp = {}
Aus_Temp_inp = {}
Log_state_1=0

def nullf(event):
    pass

def Test_1(f,inp):
    c=a*np.exp(b*f(inp))
    return c

###########################CALIBRATION################################################################

##### TEMPERATURE INPUT

def rightclick_Temp(event):
    
    Temp_l.append(event.y)
    print('Left')
    return Temp_l

def Get_data_Temp():
    global Temp_inp
    Temp_inp=[int(Temp1.get()), int(Temp2.get())]
    
def Tempreg_on():
    my_label.bind('<Button-1>',rightclick_Temp)

def Tempreg_off():
    my_label.bind('<Button-1>',nullf)
    global f_Temp
    f_Temp= interp1d(Temp_l, Temp_inp,fill_value='extrapolate')

# Temperature User inputs

Temp=Label(Calibration_Frame, text='Temperature', font='TkDefaultFont 9 bold', fg='blue')
Temp.grid(row=0,column=0,padx=10, pady=10)

Temp1= Entry(Calibration_Frame, width=10, borderwidth=5)
Temp1.grid(row=0, column=1, columnspan=1, padx=10, pady=10)

Temp2= Entry(Calibration_Frame, width=10, borderwidth=5)
Temp2.grid(row=0, column=2, columnspan=1, padx=10, pady=10)

# Temperature buttons

Temp_button=Button(Calibration_Frame, text='Tempreg on', command=lambda: [Tempreg_on(), Get_data_Temp()])
Temp_button.grid(row=0, column=3)

Temp_button=Button(Calibration_Frame, text='Tempreg off', command=Tempreg_off)
Temp_button.grid(row=0, column=4)

##### TIME LOG CONTROL

Time_log=Label(Calibration_Frame, text='Is time axis logarithmic?', font='TkDefaultFont 9 bold', fg='blue')
Time_log.grid(row=1,column=0,padx=10, pady=10)

def Log_on():
    global Log_state
    Log_state=TRUE

def Log_off():
    global Log_state
    Log_state=FALSE


Yes_button=Button(Calibration_Frame, text='     Yes     ', command=Log_on)
Yes_button.grid(row=1, column=1)

No_button=Button(Calibration_Frame, text='     No     ', command=Log_off)
No_button.grid(row=1, column=2)


# Time Input

def rightclick_Time(event):
    Time_l.append(event.x)
    print('Left')
    return Time_l

def Get_data_Time():
    global Time_inp
    Time_inp=[int(Time1.get()), int(Time2.get())]

def Timereg_on():
    my_label.bind('<Button-1>',rightclick_Time)

def Timereg_off():
    global f_Time,a,b
    if Log_state==True:
        b=math.log(Time_inp[0]/Time_inp[1])/(Time_inp[0]-Time_inp[1])
        a=Time_inp[0]/math.exp(b*Time_inp[0])
    f_Time=interp1d(Time_l, Time_inp,fill_value='extrapolate')
    my_label.bind('<Button-1>',nullf)


# Time User inputs

Time=Label(Calibration_Frame, text='Time (x axis)', font='TkDefaultFont 9 bold', fg='blue')
Time.grid(row=2,column=0,padx=10, pady=10)

Time1= Entry(Calibration_Frame, width=10, borderwidth=5)
Time1.grid(row=2, column=1, columnspan=1, padx=10, pady=10)

Time2= Entry(Calibration_Frame, width=10, borderwidth=5)
Time2.grid(row=2, column=2, columnspan=1, padx=10, pady=10)

# Time buttons

Time_button=Button(Calibration_Frame, text='Timereg on', command=lambda: [Timereg_on(), Get_data_Time()])
Time_button.grid(row=2, column=3)

Time_button=Button(Calibration_Frame, text='Timereg off', command=Timereg_off)
Time_button.grid(row=2, column=4)


#################################CRTITICAL TEMPERATURE##########################################################

##### MS AND MF TEMPERATURES

def rightclick_MsTemp(event):
    Ms_Temp_l.append(event.y)
    print('Left')
    return Ms_Temp_l


def Get_data_MsTemp():
    global Ms_Temp_inp
    # input_2= int(Ms_Temp2.get()) if Ms_Temp2.get()!=Nan else 
    # print('Fail') if Ms_Temp2.get()=='' else print('s')
    if Ms_Temp2.get()=='':
        Ms_Temp_inp = {'Ms:': int(Ms_Temp1.get()), 'Mf:': ''}
    else:
        Ms_Temp_inp = {'Ms:': int(Ms_Temp1.get()), 'Mf:': int(Ms_Temp2.get())}


def MsTempreg_on():
    my_label.bind('<Button-1>', rightclick_MsTemp)


def MsTempreg_off():
    my_label.bind('<Button-1>', nullf)

# User inputs (Ms)

Ms_Temp=Label(Critical_Temp_Frame, text='Ms/Mf Temperature', font='TkDefaultFont 9 bold', fg='blue')
Ms_Temp.grid(row=0,column=0,padx=10, pady=10)

Ms_Temp1= Entry(Critical_Temp_Frame, width=10, borderwidth=5)
Ms_Temp1.grid(row=0, column=1, columnspan=1, padx=10, pady=10)

Ms_Temp2= Entry(Critical_Temp_Frame, width=10, borderwidth=5)
Ms_Temp2.grid(row=0, column=2, columnspan=1, padx=10, pady=10)

#Temperature buttons (Ms)

Ms_Temp_button=Button(Critical_Temp_Frame, text='MsTempreg on', command=lambda: [MsTempreg_on(), Get_data_MsTemp()])
Ms_Temp_button.grid(row=0, column=3)

Ms_Temp_button2=Button(Critical_Temp_Frame, text='MsTempreg off', command=MsTempreg_off)
Ms_Temp_button2.grid(row=0, column=4)

##### AC1 AND AC3 TEMPERATURE

def rightclick_AcTemp(event):
    Ac_Temp_l.append(event.y)
    print('Left')
    return Ac_Temp_l


def Get_data_AcTemp():
    global Ac_Temp_inp
    Ac_Temp_inp = {'Ac1:': int(Ac_Temp1.get()), 'Ac3:': int(Ac_Temp2.get())}


def AcTempreg_on():
    my_label.bind('<Button-1>', rightclick_AcTemp)


def AcTempreg_off():
    my_label.bind('<Button-1>', nullf)

# User inputs (Ac1 and Ac3)

Ac_Temp=Label(Critical_Temp_Frame, text='Ac Temperature', font='TkDefaultFont 9 bold', fg='blue')
Ac_Temp.grid(row=1,column=0,padx=10, pady=10)

Ac_Temp1= Entry(Critical_Temp_Frame, width=10, borderwidth=5)
Ac_Temp1.grid(row=1, column=1, columnspan=1, padx=10, pady=10)
# Ac_Temp1.insert(0, 'Ac1')

Ac_Temp2= Entry(Critical_Temp_Frame, width=10, borderwidth=5)
Ac_Temp2.grid(row=1, column=2, columnspan=1, padx=10, pady=10)
# Ac_Temp2.insert(0, 'Ac3')

# Temperature buttons (Ac1 and Ac3)

Ac_Temp_button=Button(Critical_Temp_Frame, text='AcTempreg on', command=lambda: [AcTempreg_on(), Get_data_AcTemp()])
Ac_Temp_button.grid(row=1, column=3)

Ac_Temp_button2=Button(Critical_Temp_Frame, text='AcTempreg off', command=AcTempreg_off)
Ac_Temp_button2.grid(row=1, column=4)

#####################COMPOSITION, AUSTENITIZATION TIME, AUSTENITIZATION TEMP, GRAIN SIZE

##### AUSTENITIZATION TEMP

def rightclick_AusTemp(event):
    Aus_Temp_l.append(event.y)
    print('Left')
    return Aus_Temp_l


def Get_data_AusTemp():
    global Aus_Temp_inp
    Aus_Temp_inp = {'Austenitization Temp:': float(Aus_Temp1.get())}

def AusTempreg_on():
    my_label.bind('<Button-1>', rightclick_AusTemp)


def AusTempreg_off():
    my_label.bind('<Button-1>', nullf)

# User inputs (Aus Temp)

Aus_Temp = Label(Composition_Frame, text='Aus Temperature', font='TkDefaultFont 9 bold', fg='blue')
Aus_Temp.grid(row=0,column=0,padx=10, pady=10)

Aus_Temp1= Entry(Composition_Frame, width=10, borderwidth=5)
Aus_Temp1.grid(row=0, column=1, columnspan=1, padx=10, pady=10)


# Temperature buttons (Aus)

Aus_Temp_button=Button(Composition_Frame, text='AusTempreg on', command=lambda: [AusTempreg_on(), Get_data_AusTemp()])

Aus_Temp_button.grid(row=0, column=2)

Aus_Temp_button2=Button(Composition_Frame, text='AusTempreg off', command=AusTempreg_off)
Aus_Temp_button2.grid(row=0, column=3)

#### AUSTENITIZATION TIME

# User inputs (Aus Temp)
def Get_data_AusTime():
    global Aus_Time_inp
    Aus_Time_inp = {'Austenitization Time:': float(Aus_Time1.get())}


Aus_Time = Label(Composition_Frame, text='Aus Time', font='TkDefaultFont 9 bold', fg='blue')
Aus_Time.grid(row=1,column=0,padx=10, pady=10)

Aus_Time1= Entry(Composition_Frame, width=10, borderwidth=5)
Aus_Time1.grid(row=1, column=1, columnspan=1, padx=10, pady=10)

Aus_Time_button=Button(Composition_Frame, text='Register', command=lambda: Get_data_AusTime())
Aus_Time_button.grid(row=1, column=2)

##### GRAIN SIZE

def Get_data_GS():
    global Grain_S_data
    Grain_S_data = {'Grain Size:': float(Grain_Size1.get())}

Grain_Size = Label(Composition_Frame, text='Grain Size', font='TkDefaultFont 9 bold', fg='blue')
Grain_Size.grid(row=2, column=0,padx=10, pady=10)

Grain_Size1= Entry(Composition_Frame, width=10, borderwidth=5, textvariable='')
Grain_Size1.grid(row=2, column=1, columnspan=1, padx=10, pady=10)

Grain_Size_button=Button(Composition_Frame, text='Register', command=lambda: Get_data_GS())
Grain_Size_button.grid(row=2, column=2)

#### COMPOSITION

# def Get_data_Carbon():
#     global Carbon_data
#     Carbon_data = {'Carbon(wt%):': float(Carbon_Comp_Entry.get())}
#
# def Get_data_Manganese():
#     global Manganese_data
#     Manganese_data = {'Manganese(wt%):': float(Mn_Comp_Entry.get())}
#
# def Get_data_Silicon():
#     pass
#
# def Get_data_Sulphur():
#     pass

Comp_Label = Label(Composition_Frame, text='Composition: ', font='TkDefaultFont 9 bold', fg='dark blue')
Comp_Label.grid(row=3, column=0, padx=10, pady=10)

# x = 8
# y = 0
#
# def Add_Elements():
#     global x
#     global y
#
#     if y > 3:
#         x = x+2
#         y = 0
#
#     element_label = Label(Composition_Frame, text=clicked.get() + '(wt%)', font='TkDefaultFont 9 bold', fg='blue')
#     element_label.grid(row=x, column=y, padx=10, pady=10)
#
#     element_entry = Entry(Composition_Frame, width=10, borderwidth=5)
#     element_entry.grid(row=x, column=y+1, columnspan=1, padx=10, pady=10)
#
#     y = y+2
#
# options = [
#     'Phosphorus',
#     'Chromium',
#     'Molybdenum',
#     'Vanadium',
#     'Nickel',
#     'Copper',
#     'Aluminum',
#     'Titanium'
# ]
#
# clicked = StringVar()
# clicked.set('Choose Element')
#
# drop = OptionMenu(Composition_Frame, clicked, *options)
# drop.grid(row=3, column=1)
#
# Add_Elements_Button = Button(Composition_Frame, text='Add Element', command=Add_Elements)
# Add_Elements_Button.grid(row=3, column=2)
#
# Carbon_Comp_Label = Label(Composition_Frame, text='Carbon (wt%)', font='TkDefaultFont 9 bold', fg='blue')
# Carbon_Comp_Label.grid(row=4, column=0, padx=10, pady=10)
#
# Carbon_Comp_Entry = Entry(Composition_Frame, width=10, borderwidth=5)
# Carbon_Comp_Entry.grid(row=4, column=1, columnspan=1, padx=10, pady=10)
#
# Mn_Comp_Label = Label(Composition_Frame, text='Manganese (wt%)', font='TkDefaultFont 9 bold', fg='blue')
# Mn_Comp_Label.grid(row=4, column=2, padx=10, pady=10)
#
# Mn_Comp_Entry = Entry(Composition_Frame, width=10, borderwidth=5)
# Mn_Comp_Entry.grid(row=4, column=3, columnspan=1, padx=10, pady=10)
#
# Carbon_Comp_button=Button(Composition_Frame, text='Register', command=lambda: Get_data_Carbon())
# Carbon_Comp_button.grid(row=5, column=0)
#
# Manganese_Comp_button=Button(Composition_Frame, text='Register', command=lambda: Get_data_Manganese())
# Manganese_Comp_button.grid(row=5, column=2)
#
# Si_Comp_Label = Label(Composition_Frame, text='Silicon (wt%)', font='TkDefaultFont 9 bold', fg='blue')
# Si_Comp_Label.grid(row=6, column=0, padx=10, pady=10)
#
# Si_Comp_Entry = Entry(Composition_Frame, width=10, borderwidth=5)
# Si_Comp_Entry.grid(row=6, column=1, columnspan=1, padx=10, pady=10)
#
# S_Comp_Label = Label(Composition_Frame, text='Sulphur (wt%)', font='TkDefaultFont 9 bold', fg='blue')
# S_Comp_Label.grid(row=6, column=2, padx=10, pady=10)
#
# S_Comp_Entry = Entry(Composition_Frame, width=10, borderwidth=5)
# S_Comp_Entry.grid(row=6, column=3, columnspan=1, padx=10, pady=10)
#
# Silicon_Comp_button=Button(Composition_Frame, text='Register', command=lambda: Get_data_Silicon())
# Silicon_Comp_button.grid(row=7, column=0)
#
# Sulphur_Comp_button=Button(Composition_Frame, text='Register', command=lambda: Get_data_Sulphur())
# Sulphur_Comp_button.grid(row=7, column=2)

x = 4
y = 0

sv = StringVar()

def Get_data():
    pass
    global Element_data
    Element_data[create_label['text']] = float(create_entry.get())

def Create_Widgets():
    pop.destroy()
    global x
    global y
    global create_entry
    global create_label

    if y > 3:
        x = x+2
        y = 0

    create_label = Label(Composition_Frame, text=sv.get(), font='TkDefaultFont 9 bold', fg='blue')
    create_label.grid(row=x, column=y, padx=10, pady=10)

    create_entry = Entry(Composition_Frame, width=10, borderwidth=5)
    create_entry.grid(row=x, column=y+1, columnspan=1, padx=10, pady=10)

    create_button = Button(Composition_Frame, text='Register', command=lambda: Get_data())
    create_button.grid(row=x+1, column=y, pady=10)

    y = y+2

def Add_Element():

    global pop
    global element_entry


    pop = Toplevel(Composition_Frame)
    pop.title('Add Element')

    element_label = Label(pop, text='Add Element Name', font='TkDefaultFont 9 bold', fg='blue')
    element_label.grid(row=0, column=0, padx=10, pady=10)

    element_entry = Entry(pop, textvariable=sv, width=10, borderwidth=5)
    element_entry.grid(row=0, column=2, columnspan=1, padx=10, pady=10)

    element_button = Button(pop, text='Register', command=Create_Widgets)
    element_button.grid(row=1, column=1, padx=10, pady=10)

Add_Elements_Button = Button(Composition_Frame, text='Add Element', command=Add_Element)
Add_Elements_Button.grid(row=3, column=1)

##########################PHASE FRACTIONS################################################################################################3
#######Button for combined total fractions of ferrite and pearlite

Fraction_log=Label(Phasefraction_Frame, text='Are Pearlite and ferrite lines together?', font='TkDefaultFont 9 bold', fg='blue')
Fraction_log.grid(row=3,column=0,padx=10, pady=10)

def Log_on():
    global Log_state_1
    Log_state_1=TRUE

def Log_off():
    global Log_state_1
    Log_state_1=FALSE


Yes_button=Button(Phasefraction_Frame, text='     Yes     ', command=Log_on)
Yes_button.grid(row=3, column=1)

No_button=Button(Phasefraction_Frame, text='     No     ', command=Log_off)
No_button.grid(row=3, column=2)


##### FERRITE PF


def leftclick_Ferr(event):
    global Ferr_l_T
    global Ferr_l_t
    Ferr_l_t.append(event.x)
    Ferr_l_T.append(event.y)
    print('Left')
    # return Ferr_l_t,Ferr_l_T

def Get_data_Ferr():
    global Ferr_inp
    Ferr_inp=int(Ferrite_frac.get())

def Ferr_reg_on():
    my_label.bind('<Button-1>',leftclick_Ferr)

def Ferr_reg_off():
    my_label.bind('<Button-1>',nullf)

def Calc_and_reset(time,temp,fraction,f_Temp,f_Time):
    #Add ferrite data to a dictionary and convert to real time and temperature
    #Reset the matrixes
    global Ferr_data
    global Ferr_l_T
    global Ferr_l_t
    # Ferr_data[fraction]=[f_Time(time),f_Temp(temp)]
    Ferr_data[fraction]={'Time': list(Test_1(f_Time,time)),'Temperature':list(f_Temp(temp))}
    Ferr_l_T=[]
    Ferr_l_t=[]

# Label

Ferrite=Label(Phasefraction_Frame, text='Ferrite fractions', font='TkDefaultFont 9 bold', fg='blue')
Ferrite.grid(row=0,column=0,padx=10, pady=10)

# Fraction insert box

Ferrite_frac= Entry(Phasefraction_Frame, width=10, borderwidth=5)
# Ferrite_frac.insert(0,'Enter Ferrite fraction in %')
Ferrite_frac.grid(row=0, column=1, columnspan=1, padx=10, pady=10)

# Buttons

Ferr1_button=Button(Phasefraction_Frame, text='Ferr_reg on', command=lambda: [Ferr_reg_on(), Get_data_Ferr()])
Ferr1_button.grid(row=0, column=2)

Ferr2_button=Button(Phasefraction_Frame, text='Ferr_reg off', command=Ferr_reg_off)
Ferr2_button.grid(row=0, column=3)

Ferr3_button=Button(Phasefraction_Frame, text='Calculate and reset', command=lambda : Calc_and_reset(Ferr_l_t, Ferr_l_T, Ferr_inp, f_Temp, f_Time))
Ferr3_button.grid(row=0, column=4)

################################# PEARLITE PF

def leftclick_Pear(event):
    global Pear_l_T
    global Pear_l_t
    Pear_l_t.append(event.x)
    Pear_l_T.append(event.y)
    print('Left')
    # return Ferr_l_t,Ferr_l_T

def Get_data_Pear():
    global Pear_inp
    Pear_inp=int(Pearlite_frac.get())

def Pear_reg_on():
    my_label.bind('<Button-1>',leftclick_Pear)

def Pear_reg_off():
    my_label.bind('<Button-1>',nullf)

def Calc_and_reset_Pear(time,temp,fraction,f_Temp,f_Time):
    #Add ferrite data to a dictionary and convert to real time and temperature
    #Reset the matrixes
    global Pear_data
    global Pear_l_T
    global Pear_l_t
    # Ferr_data[fraction]=[f_Time(time),f_Temp(temp)]
    Pear_data[fraction]={'Time': list(Test_1(f_Time,time)),'Temperature':list(f_Temp(temp))}
    Pear_l_T=[]
    Pear_l_t=[]

################################# Label

Pearlite=Label(Phasefraction_Frame, text='Pearlite fractions', font='TkDefaultFont 9 bold', fg='blue')
Pearlite.grid(row=1,column=0,padx=10, pady=10)

########################## Fraction insert box

Pearlite_frac= Entry(Phasefraction_Frame, width=10, borderwidth=5)
Pearlite_frac.grid(row=1, column=1, columnspan=1, padx=10, pady=10)

######################### Buttons

Pear1_button=Button(Phasefraction_Frame, text='Pear_reg on', command=lambda: [Pear_reg_on(), Get_data_Pear()])
Pear1_button.grid(row=1, column=2)

Pear2_button=Button(Phasefraction_Frame, text='Pear_reg off', command=Pear_reg_off)
Pear2_button.grid(row=1, column=3)

Pear3_button=Button(Phasefraction_Frame, text='Calculate and reset', command=lambda : Calc_and_reset_Pear(Pear_l_t, Pear_l_T, Pear_inp, f_Temp, f_Time))
Pear3_button.grid(row=1, column=4)

############################################## BAINITE PF

def leftclick_Bain(event):
    global Bain_l_T
    global Bain_l_t
    Bain_l_t.append(event.x)
    Bain_l_T.append(event.y)
    print('Left')
    # return Ferr_l_t,Ferr_l_T

def Get_data_Bain():
    global Bain_inp
    Bain_inp=int(Bainite_frac.get())

def Bain_reg_on():
    my_label.bind('<Button-1>',leftclick_Bain)

def Bain_reg_off():
    my_label.bind('<Button-1>',nullf)

def Calc_and_reset_Bain(time,temp,fraction,f_Temp,f_Time):
    #Add ferrite data to a dictionary and convert to real time and temperature
    #Reset the matrixes
    global Bain_data
    global Bain_l_T
    global Bain_l_t
    # Ferr_data[fraction]=[f_Time(time),f_Temp(temp)]
    Bain_data[fraction]={'Time': list(Test_1(f_Time,time)),'Temperature':list(f_Temp(temp))}
    Bain_l_T=[]
    Bain_l_t=[]

#######################  Label

Bainite=Label(Phasefraction_Frame, text='Bainite fractions', font='TkDefaultFont 9 bold', fg='blue')
Bainite.grid(row=2,column=0,padx=10, pady=10)

####################### Fraction insert box

Bainite_frac= Entry(Phasefraction_Frame, width=10, borderwidth=5)
Bainite_frac.grid(row=2, column=1, columnspan=1, padx=10, pady=10)

###################### Buttons

Bain1_button=Button(Phasefraction_Frame, text='Bain_reg on', command=lambda: [Bain_reg_on(), Get_data_Bain()])
Bain1_button.grid(row=2, column=2)

Bain2_button=Button(Phasefraction_Frame, text='Bain_reg off', command=Bain_reg_off)
Bain2_button.grid(row=2, column=3)

Bain3_button=Button(Phasefraction_Frame, text='Calculate and reset', command=lambda : Calc_and_reset_Bain(Bain_l_t, Bain_l_T, Bain_inp, f_Temp, f_Time))
Bain3_button.grid(row=2, column=4)


#####################EXITS###########################################################################################################################

button_quit=Button(Phasefraction_Frame, text='Exit', command=root.quit)
button_quit.grid(row=4,column=0)

#####################IMAGE PROCESSING#####################################################################################################################

top = Toplevel()
top.title('IMAGE')
top.geometry(str(int(screen_width / 2)) + 'x' + str(int(screen_height / 1.15)))
Grid.rowconfigure(top, index=0, weight=1)
Grid.rowconfigure(top, index=1, weight=1)
Grid.rowconfigure(top, index=2, weight=1)
Grid.columnconfigure(top, index=0, weight=1)

def openimage():
    global screen_width
    global screen_height
    global my_label
    global new_image
    global photo
    global image
    global newjsonfile


    fnamecontainer = []
    top.filename = fd.askopenfilename(title='Select file', filetypes=(
    ('jpg files', '*.jpg'), ('png file', '*.png'), ('jpeg file', '*.jpeg'), ('all files', '*.*')))
    my_label = Label(top, text=top.filename)
    my_label.grid(row=2, column=0)
    image = Image.open(top.filename)


    ####Resizing of the image to be half the screen height

    image_width=image.size[0]
    image_height=image.size[1]
    new_image_width=screen_width/2
    delta_change=(new_image_width-image_width)/image_width
    new_image_height=image_height*(1+delta_change)
    if new_image_height >= screen_height/1.15:
        new_image_height=screen_height/1.3
        delta_change = (new_image_height-image_height)/image_height
        new_image_width = image_width*(1+delta_change)
    new_image=image.resize((int(new_image_width),int(new_image_height)))
    # new_image.save('test_image.jpg')
    # filename = 'test_image.jpg'
    photo = ImageTk.PhotoImage(new_image)
    my_label = Label(top, image=photo)
    # my_image_label.bind('<Configure>', resize_image)
    my_label.grid(row=1, column=0, sticky='NSEW')
    for i in top.filename.split('/'):
        fnamecontainer.append(i)
    imagefname = fnamecontainer[-1].split('.')[0]
    print(imagefname)
    newjsonfile = open(imagefname + '.json','w')

imagebutton = Button(top, text='Select File', command=openimage)
imagebutton.grid(row=0, column=0, pady=10)

root.mainloop()

###############################POST_PROCESSING#######################################################

global newjsonfile

Phase_Data_dict = {'Phase Data': {'Ferrite:': Ferr_data,'Pearlite:': Pear_data, 'Bainite:': Bain_data},'Status':Log_state_1}
Critical_Temp_dict = {'Critical Temp Data': {'Ms_Temp:': Ms_Temp_inp, 'Ac Temp:': Ac_Temp_inp}}
Comp_dict = {'Composition Data:': Element_data}
Aus_dict = {'Austenitization Data:': {'Aus_Temp:': Aus_Temp_inp, 'Aus_Time:': Aus_Time_inp}}
Grain_dict = {'Grain Size Data:': {'Grain Size:': Grain_S_data}}

Data_dict = {**Phase_Data_dict, **Critical_Temp_dict, **Comp_dict, **Aus_dict, **Grain_dict}
Main_json = json.dumps(Data_dict, indent=4)
try:
    newjsonfile.write(Main_json)
    newjsonfile.close()
except:
    print('NO IMAGE FILE CHOSEN')


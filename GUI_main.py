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
import numpy as np
import math
import json

root=Tk()
root.title('Example')
# root.tk.call('tk', 'scaling', 1.0)

print(root.winfo_screenwidth())
print(root.winfo_screenheight())
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
# root.geometry(str(int(screen_width/2))+'x'+str(screen_height))


# root.geometry('800x1920')


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

def nullf(event):
    pass


def Test_1(f,inp): #####RENAME this
    c=a*np.exp(b*f(inp))
    return c

#######################TEMPERATURE INPUT############################

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
    f_Temp= interp1d(Temp_l, Temp_inp)
    
    

#Temperature User inputs
Temp=Label(root,text='Temperature')
Temp.grid(row=1,column=0,padx=10, pady=10)

Temp1= Entry(root, width=10, borderwidth=5)
Temp1.grid(row=1, column=1, columnspan=1, padx=10, pady=10)

Temp2= Entry(root, width=10, borderwidth=5)
Temp2.grid(row=1, column=2, columnspan=1, padx=10, pady=10)

#Temperature buttons

Temp_button=Button(root, text='Tempreg on', command=lambda: [Tempreg_on(), Get_data_Temp()])
Temp_button.grid(row=1, column=3)

Temp_button=Button(root, text='Tempreg off', command=Tempreg_off)
Temp_button.grid(row=1, column=4)


##########################TIME INPUT###############################

def rightclick_Time(event): #####Rename to left
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
    f_Time=interp1d(Time_l, Time_inp)
    my_label.bind('<Button-1>',nullf)
    

#Time User inputs
Time=Label(root,text='Time (x axis)')
Time.grid(row=2,column=0,padx=10, pady=10)

Time1= Entry(root, width=10, borderwidth=5)
Time1.grid(row=2, column=1, columnspan=1, padx=10, pady=10)

Time2= Entry(root, width=10, borderwidth=5)
Time2.grid(row=2, column=2, columnspan=1, padx=10, pady=10)

#Time buttons

Time_button=Button(root, text='Timereg on', command=lambda: [Timereg_on(), Get_data_Time()])
Time_button.grid(row=2, column=3)

Time_button=Button(root, text='Timereg off', command=Timereg_off)
Time_button.grid(row=2, column=4)


##########################TIME_LOG CONTROL###############################

Time_log=Label(root,text='Is time axis logarithmic?')
Time_log.grid(row=3,column=0,padx=10, pady=10)

def Log_on():
    global Log_state
    Log_state=TRUE

def Log_off():
    global Log_state
    Log_state=FALSE
    
    
Yes_button=Button(root, text='Yes', command=Log_on)
Yes_button.grid(row=3, column=1)

No_button=Button(root, text='No', command=Log_off)
No_button.grid(row=3, column=2)

# if Status==True:

#     Status=False
##########################Ferrite_INPUT###############################

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
    
    

#Label
Ferrite=Label(root,text='Ferrite fractions')
Ferrite.grid(row=4,column=0,padx=10, pady=10)

#Fraction insert box
Ferrite_frac= Entry(root, width=10,borderwidth=5)
# Ferrite_frac.insert(0,'Enter Ferrite fraction in %')
Ferrite_frac.grid(row=4, column=1, padx=10, pady=10)

#Buttons

Ferr1_button=Button(root, text='Ferr_reg on', command=lambda: [Ferr_reg_on(), Get_data_Ferr()])
Ferr1_button.grid(row=4, column=2)

Ferr2_button=Button(root, text='Ferr_reg off', command=Ferr_reg_off)
Ferr2_button.grid(row=4, column=3)

Ferr3_button=Button(root, text='Calculate and reset', command=lambda : Calc_and_reset(Ferr_l_t,Ferr_l_T,Ferr_inp,f_Temp,f_Time))
Ferr3_button.grid(row=4, column=4)


##########################Pearlite_INPUT###############################

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
    
    

#Label
Pearlite=Label(root,text='Pearlite fractions')
Pearlite.grid(row=5,column=0,padx=10, pady=10)

#Fraction insert box
Pearlite_frac= Entry(root, width=10,borderwidth=5)
Pearlite_frac.grid(row=5, column=1, padx=10, pady=10)

#Buttons

Pear1_button=Button(root, text='Pear_reg on', command=lambda: [Pear_reg_on(), Get_data_Pear()])
Pear1_button.grid(row=5, column=2)

Pear2_button=Button(root, text='Pear_reg off', command=Pear_reg_off)
Pear2_button.grid(row=5, column=3)

Pear3_button=Button(root, text='Calculate and reset', command=lambda : Calc_and_reset_Pear(Pear_l_t,Pear_l_T,Pear_inp,f_Temp,f_Time))
Pear3_button.grid(row=5, column=4)



##########################Bainite_INPUT###############################

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
    
    

#Label
Bainite=Label(root,text='Bainite fractions')
Bainite.grid(row=6,column=0,padx=10, pady=10)

#Fraction insert box
Bainite_frac= Entry(root, width=10,borderwidth=5)
Bainite_frac.grid(row=6, column=1, padx=10, pady=10)

#Buttons

Bain1_button=Button(root, text='Bain_reg on', command=lambda: [Bain_reg_on(), Get_data_Bain()])
Bain1_button.grid(row=6, column=2)

Bain2_button=Button(root, text='Pear_reg off', command=Bain_reg_off)
Bain2_button.grid(row=6, column=3)

Bain3_button=Button(root, text='Calculate and reset', command=lambda : Calc_and_reset_Bain(Bain_l_t,Bain_l_T,Bain_inp,f_Temp,f_Time))
Bain3_button.grid(row=6, column=4)


#####################Utility###########################

button_quit=Button(root,text='Exit',command=root.quit)
button_quit.grid(row=7,column=0)

#####################Open_FILE###############################

# def open_image():
#     pass

    

# open_image_button=Button(root,text='Select file', command=open_image())
# open_image_button.grid(row=0,column=6)


# filename = fd.askopenfilename()
filename = 'CCT_4140.jpg'
image = Image.open(filename)
image_width=image.size[0]
image_height=image.size[1]
new_image_height=screen_height/3
delta_change=(new_image_height-image_height)/image_height
new_image_width=image_width*(1+delta_change)
new_image=image.resize((int(new_image_width),int(new_image_height)))
my_img=ImageTk.PhotoImage(new_image)
my_label=Label(image=my_img)
my_label.grid(row=0, column=0,columnspan=5)


root.mainloop()

# 
# 

# if Log_state==True:
#     b=math.log(Time_inp[0]/Time_inp[1])/(Time_l[0]-Time_l[1])
#     a=Time_inp[0]/math.exp(b*Time_l[0])

####POST_PROCESSING

#####DATA INTERPOLATION#####

# Interpolate data on fixed temperatures


# Cooling rate estimation




Main_json=json.dumps({'Ferrite': Ferr_data,'Pearlite': Pear_data, 'Bainite': Bain_data})



jsonFile = open("CCT.json", "w")
jsonFile.write(Main_json)
jsonFile.close()
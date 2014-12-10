import sys
import tkFont
import tkMessageBox
import ttk
from Tkinter import *

def temperature():
    your_temp = temper.get()
    if your_temp.isdigit() == False:
        tkMessageBox.showinfo(message='Incorrect Input \n Please Try Again.')
        return
    if unit.get() == 'Celsius': #convert Celsius to other unit
        ctoc = "%.2f" % your_temp
        ctof = "%.2f" % ((1.8 * your_temp) + 32)
        ctok = "%.2f" % (your_temp + 273.15)
        ctora = "%.2f" % ((your_temp * 1.8) +32 + 459.67)
        ctoc_label = Label(text=str(ctoc)+' Celsius. ', fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12)).pack()
        ctof_label = Label(text=str(ctof)+' Fahrenheit. ', fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12)).pack()
        ctok_label = Label(text=str(ctok)+' Kelvin. ', fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12)).pack()
        ctora_label = Label(text=str(ctora)+' Rankine. ', fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12)).pack()
    elif unit.get() == 'Fahrenheit': #convert Fahrenheit to other unit
        ftoc = "%.2f" % ((your_temp - 32) / 1.8)
        ftof = "%.2f" % your_temp
        ftok = "%.2f" % ((your_temp + 459.67) / 1.8)
        ftora = "%.2f" % (your_temp + 459.67)
        ftoc_label = Label(text=str(ftoc)+' Celsius. ', fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12)).pack()
        ftof_label = Label(text=str(ftof)+' Fahrenheit. ', fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12)).pack()
        ftok_label = Label(text=str(ftok)+' Kelvin. ', fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12)).pack()
        ftora_label = Label(text=str(ftora)+' Rankine. ', fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12)).pack()
    elif unit.get() == 'Kelvin': #convert Kelvin to other unit
        ktoc = "%.2f" % (your_temp - 273.15)
        ktof = "%.2f" % ((your_temp * 1.8) - 459.67)
        ktok = "%.2f" % your_temp
        ktora = "%.2f" % (your_temp * 1.8)
        ktoc_label = Label(text=str(ktoc)+' Celsius. ', fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12)).pack()
        ktof_label = Label(text=str(ktof)+' Fahrenheit. ', fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12)).pack()
        ktok_label = Label(text=str(ktok)+' Kelvin. ', fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12)).pack()
        ktora_label = Label(text=str(ktora)+' Rankine. ', fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12)).pack()
    elif unit.get() == 'Rankine': #convert Rankine to other unit
        ratoc = "%.2f" % ((your_temp - 32 - 459.67) / 1.8)
        ratof = "%.2f" % (your_temp - 459.67)
        ratok = "%.2f" % (your_temp / 1.8)
        ratora = "%.2f" % your_temp
        ratoc_label = Label(text=str(ratoc)+' Celsius. ', fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12)).pack()
        ratof_label = Label(text=str(ratof)+' Fahrenheit. ', fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12)).pack()
        ratok_label = Label(text=str(ratok)+' Kelvin. ', fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12)).pack()
        ratora_label = Label(text=str(ratora)+' Rankine. ', fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12)).pack()

    calculate.config(state='disable')
        
#make frame
mGui = Tk()
mGui.geometry('600x500+300+100')
mGui.title('TforPET Version X')
mGui.config(background = '#FFFFFF')

#head and tail text 
mLabel = Label(text='Temperature Converter',fg='blue',bg='#FFFFFF',font=tkFont.Font(family="Calibri",size=20,weight=tkFont.BOLD)).pack()
mLabel2 = Label(text='For Pet Lovers',fg='blue',bg='#FFFFFF',font = tkFont.Font(family="Calibri", size=20,weight=tkFont.BOLD)).pack()
mLabel3 = Label(text='Faculty of Information Technology @ KMITL',bg='#FFFFFF').place(x=350,y=470)

#temperature input
tlabel = Label(text='Input Temperature',fg='black',bg='#FFFFFF',font=tkFont.Font(size=12,weight=tkFont.BOLD)).place(x=40,y=125)
temper = StringVar()
your_temp = Entry(mGui, textvariable=temper)
your_temp.pack(pady = 50)

#box unit
unit = IntVar()
box = ttk.Combobox(mGui,textvariable=unit)
box['values'] = ('Celsius', 'Fahrenheit', 'Kelvin', 'Rankine')
box.current(0)
box.place(x=400,y=127)

#calculate button
calculate = Button(text="Calculate",command=temperature,fg='black',bg='light blue',font=tkFont.Font(size = 12))
calculate.pack()

mGui.mainloop()

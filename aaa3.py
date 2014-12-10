import sys
import tkFont
import tkMessageBox
import ttk
from Tkinter import *

def temperature():
    your_temp2 = temper.get() #check incorrect input
    if your_temp2.isdigit() == False and '.' not in your_temp2:
        tkMessageBox.showinfo(message='Incorrect Input \n Please Try Again.')
        return

    your_temp = float(temper.get())
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

    convert.config(state='disable')

def aboutpro():
    tkMessageBox.showinfo(message='Nattakit Waiyawatpattarakul 57070033 \nAkkapon Chainarong 57070146')

def thanks():
    tkMessageBox.showinfo(message='We truly appreciate for your taught in resolving the problem. \
                \nAJ.Chotipat Pornavalai and P.Judge Pichatorn Eak-Une \nThank you for your feedback.')

def helpdoc():
    tkMessageBox.showinfo(message='This program will help you convert temperature more easily.\
                \nAnd checking for your pet will comfortable with that temperature.')

def howto():
    tkMessageBox.showinfo(message='Step 1\nInput your temperature. Do not include with alphabet\
                \nExample 25, 32.72 but Kaka, Ronal07 cannot use on this program \nStep 2 \
                \nChoose your unit and your pet. \nStep 3 \nClick Convert.')

def exitt():
    mExit = tkMessageBox.askokcancel(title='Quit',message='Are You Sure')
    if mExit > 0:
        mGui.destroy()
        return
        
#make frame
mGui = Tk()
mGui.geometry('600x500+300+100')
mGui.title('TforPET Version X')
mGui.config(background = '#FFFFFF')

#head and tail text 
mLabel = Label(text='Temperature Converter',fg='blue',bg='#FFFFFF',font=tkFont.Font(size=20,weight=tkFont.BOLD)).pack()
mLabel2 = Label(text='For Pet Lovers',fg='blue',bg='#FFFFFF',font = tkFont.Font(size=20,weight=tkFont.BOLD)).pack()
mLabel3 = Label(text='Faculty of Information Technology @ KMITL',bg='#FFFFFF').place(x=350,y=470)

#temperature input
tlabel = Label(text='Input Temperature',fg='black',bg='#FFFFFF',font=tkFont.Font(size=12,weight=tkFont.BOLD)).place(x=40,y=125)
temper = StringVar()
your_temp = Entry(mGui, textvariable=temper)
your_temp.pack(pady = 50)

#box unit
unit = StringVar()
box = ttk.Combobox(mGui,textvariable=unit)
box['values'] = ('Celsius', 'Fahrenheit', 'Kelvin', 'Rankine')
box.current(0)
box.place(x=400,y=127)

#convert button
convert = Button(text="Convert",command=temperature,fg='black',bg='light blue',font=tkFont.Font(size = 12))
convert.pack()

#pet button
pets = Button(text="Did it comfortable for pet?",fg='black',bg='light blue',font=tkFont.Font(size = 12))
pets.pack(pady=10)

#create menu bar
#about-us menu
menubar = Menu(mGui)
topmenu = Menu(menubar,tearoff=0)
topmenu.add_command(label='About Producer',command=aboutpro)
topmenu.add_command(label='Thanksgiving',command=thanks)
menubar.add_cascade(label='About us',menu=topmenu)

#help menu
secmenu = Menu(menubar,tearoff = 0)
secmenu.add_command(label='Help Docs',command=helpdoc)
secmenu.add_command(label='How to use',command=howto)
menubar.add_cascade(label='Help',menu=secmenu)

#exit menu
exmenu = Menu(menubar,tearoff=0)
exmenu.add_command(label='Quit',command=exitt)
menubar.add_cascade(label='Exit',menu=exmenu)

mGui.config(menu=menubar)
mGui.mainloop()

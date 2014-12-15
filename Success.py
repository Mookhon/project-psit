import sys
import tkFont
import tkMessageBox
import ttk
from Tkinter import *

#main function
def temperature():
    allowed = '1234567890.-'
    dot = 0
    dash = 0
    fault = 0
    
    #input checker
    for i in temp.get():
        if i not in allowed or temp.get() == '-.' or temp.get() == '.-':
            fault = 1
        elif i == '.':
            dot += 1
        elif i == '-':
            dash += 1
        elif '-' in temp.get() and temp.get()[0] != '-':
            fault = 1
            
    #input error
    if len(temp.get()) > 12:
        tkMessageBox.showinfo(message='Support Only 12 Digit.')
        return
    elif fault == 1 or dot > 1 or dash > 1 or temp.get() == '.' or temp.get() == '-':
        tkMessageBox.showinfo(message='Incorrect Input \n Please Try Again.')
        return
    elif temp.get() == '':
        tkMessageBox.showinfo(message='Please Input Number')
        return
    else:
        tempcalc = float(temp.get())

    #calculator
    tempcalc = float(temp.get())
    if unit.get() == 'Celsius': #convert Celsius to other unit
        var_1.set("%.2f" % tempcalc+" Celcius.")
        var_2.set("%.2f" % ((1.8 * tempcalc) + 32)+" Fahrenheit.")
        var_3.set("%.2f" % (tempcalc + 273.15)+" Kelvin.")
        var_4.set("%.2f" % ((tempcalc * 1.8) +32 + 459.67)+" Rankine.")
    elif unit.get() == 'Fahrenheit': #convert Fahrenheit to other unit
        var_1.set("%.2f" % ((tempcalc-32)/1.8)+" Celcius.")
        var_2.set("%.2f" % tempcalc + " Fahrenheit.")
        var_3.set("%.2f" % ((tempcalc+459.67)/1.8)+" Kelvin.")
        var_4.set("%.2f" % (tempcalc+459.67)+" Rankine.")
    elif unit.get() == 'Kelvin': #convert Kelvin to other unit
        var_1.set("%.2f" % (tempcalc - 273.15)+" Celcius.")
        var_2.set("%.2f" % ((tempcalc * 1.8) - 459.67)+" Fahrenheit.")
        var_3.set("%.2f" % tempcalc+" Kelvin.")
        var_4.set("%.2f" % (tempcalc * 1.8)+" Rankine.")
    elif unit.get() == 'Rankine': #convert Rankine to other unit
        var_1.set("%.2f" % ((tempcalc - 32 - 459.67) / 1.8)+" Celcius.")
        var_2.set("%.2f" % (tempcalc - 459.67)+" Fahrenheit.")
        var_3.set("%.2f" % (tempcalc / 1.8)+" Kelvin.")
        var_4.set("%.2f" % tempcalc+" Rankine.")
    dot = 0
    fault = 0

#pet checker function
def petter():
    petcheck_2 = temp.get()
    if petcheck_2.isdigit() == False and '.' not in petcheck_2:
        tkMessageBox.showinfo(message='Incorrect Input \n Please Try Again.')
        return
    petcheck = float(temp.get())
    if pet.get() == 'Dog':
        if unit.get() == 'Fahrenheit':
            if petcheck >= 100 and petcheck <= 102.5:
                tkMessageBox.showinfo(message='Your dog will comfortable with this temperature :)')
            elif petcheck < 100:
                tkMessageBox.showinfo(message='It is too cold. Keep your dog warm!')
            else:
                tkMessageBox.showinfo(message='Care your dog. Maybe he has a fever.\nTake him to veteranian if you possible.')
        elif unit.get() == 'Celsius':
            if petcheck >= 38 and petcheck <= 39.2:
                tkMessageBox.showinfo(message='Your dog will comfortable with this temperature :)')
            elif petcheck < 38:
                tkMessageBox.showinfo(message='It is too cold. Keep your dog warm!')
            else:
                tkMessageBox.showinfo(message='Care your dog. Maybe he has a fever.\nTake him to veteranian if you possible.')
        else:
            tkMessageBox.showinfo(message='This unit is not support!\nTry again with Celsius and Fahrenheit')
    elif pet.get() == 'Cat':
        if unit.get() == 'Fahrenheit':
            if petcheck >= 101.5 and petcheck <= 126:
                tkMessageBox.showinfo(message='Your cat will comfortable with this temperature :)')
            elif petcheck < 101.5:
                tkMessageBox.showinfo(message='It is too cold. Keep your cat warm!')
            else:
                tkMessageBox.showinfo(message='Care your cat. Maybe he has a fever.\nTake him to veteranian if you possible.')
        elif unit.get() == 'Celsius':
            if petcheck >= 37.5 and petcheck <= 52:
                tkMessageBox.showinfo(message='Your cat will comfortable with this temperature :)')
            elif petcheck < 37.5:
                tkMessageBox.showinfo(message='It is too cold. Keep your cat warm!')
            else:
                tkMessageBox.showinfo(message='Care your cat. Maybe he has a fever.\nTake him to veteranian if you possible.')
        else:
            tkMessageBox.showinfo(message='This unit is not support!\nTry again with Celsius and Fahrenheit')
    elif pet.get() == 'Hamster':
        if unit.get() == 'Fahrenheit':
            if petcheck >= 68 and petcheck <= 72:
                tkMessageBox.showinfo(message='Your hamster will comfortable with this temperature :)')
            elif petcheck < 68:
                tkMessageBox.showinfo(message='It is too cold. Keep your hamster warm!')
            else:
                tkMessageBox.showinfo(message='Care your hamster. Maybe he has a fever.\nTake him to veteranian if you possible.')
        elif unit.get() == 'Celsius':
            if petcheck >= 20 and petcheck <= 22:
                tkMessageBox.showinfo(message='Your hamster will comfortable with this temperature :)')
            elif petcheck < 20:
                tkMessageBox.showinfo(message='It is too cold. Keep your hamster warm!')
            else:
                tkMessageBox.showinfo(message='Care your hamster. Maybe he has a fever.\nTake him to veteranian if you possible.')
        else:
            tkMessageBox.showinfo(message='This unit is not support!\nTry again with Celsius and Fahrenheit')
    elif pet.get() == 'Sugar Glider':
        if unit.get() == 'Fahrenheit':
            if petcheck >= 80 and petcheck <= 85:
                tkMessageBox.showinfo(message='Your sugar glider will comfortable with this temperature :)')
            elif petcheck < 80:
                tkMessageBox.showinfo(message='It is too cold. Keep your sugar glider warm!')
            else:
                tkMessageBox.showinfo(message='Care your sugar glider. Maybe he has a fever.\nTake him to veteranian if you possible.')
        elif unit.get() == 'Celsius':
            if petcheck >= 26.6 and petcheck <= 29.5:
                tkMessageBox.showinfo(message='Your sugar glider will comfortable with this temperature :)')
            elif petcheck < 26.6:
                tkMessageBox.showinfo(message='It is too cold. Keep your sugar glider warm!')
            else:
                tkMessageBox.showinfo(message='Care your sugar glider. Maybe he has a fever.\nTake him to veteranian if you possible.')
        else:
            tkMessageBox.showinfo(message='This unit is not support!\nTry again with Celsius and Fahrenheit')
    elif pet.get() == 'Hedgehog':
        if unit.get() == 'Fahrenheit':
            if petcheck >= 72 and petcheck <= 80:
                tkMessageBox.showinfo(message='Your hedgehog will comfortable with this temperature :)')
            elif petcheck < 72:
                tkMessageBox.showinfo(message='It is too cold. Keep your hedgehog warm!')
            else:
                tkMessageBox.showinfo(message='Care your hedgehog. Maybe he has a fever.\nTake him to veteranian if you possible.')
        elif unit.get() == 'Celsius':
            if petcheck >= 22.2 and petcheck <= 26.6:
                tkMessageBox.showinfo(message='Your hedgehog will comfortable with this temperature :)')
            elif petcheck < 22.2:
                tkMessageBox.showinfo(message='It is too cold. Keep your hedgehog warm!')
            else:
                tkMessageBox.showinfo(message='Care your hedgehog. Maybe he has a fever.\nTake him to veteranian if you possible.')
        else:
            tkMessageBox.showinfo(message='This unit is not support!\nTry again with Celsius and Fahrenheit')
    elif pet.get() == 'Rabbit':
        if unit.get() == 'Fahrenheit':
            if petcheck >= 50 and petcheck <= 83:
                tkMessageBox.showinfo(message='Your rabbit will comfortable with this temperature :)')
            elif petcheck < 50:
                tkMessageBox.showinfo(message='It is too cold. Keep your rabbit warm!')
            else:
                tkMessageBox.showinfo(message='Care your rabbit. Maybe he has a fever.\nTake him to veteranian if you possible.')
        elif unit.get() == 'Celsius':
            if petcheck >= 10 and petcheck <= 28.3:
                tkMessageBox.showinfo(message='Your rabbit will comfortable with this temperature :)')
            elif petcheck < 10:
                tkMessageBox.showinfo(message='It is too cold. Keep your rabbit warm!')
            else:
                tkMessageBox.showinfo(message='Care your rabbit. Maybe he has a fever.\nTake him to veteranian if you possible.')
        else:
            tkMessageBox.showinfo(message='This unit is not support!\nTry again with Celsius and Fahrenheit')
    elif pet.get() == 'Bird':
        if unit.get() == 'Fahrenheit':
            if petcheck >= 65 and petcheck <= 80:
                tkMessageBox.showinfo(message='Your bird will comfortable with this temperature :)')
            elif petcheck < 65:
                tkMessageBox.showinfo(message='It is too cold. Keep your bird warm!')
            else:
                tkMessageBox.showinfo(message='Care your bird. Maybe he has a fever.\nTake him to veteranian if you possible.')
        elif unit.get() == 'Celsius':
            if petcheck >= 18.3 and petcheck <= 26.6:
                tkMessageBox.showinfo(message='Your bird will comfortable with this temperature :)')
            elif petcheck < 18.3:
                tkMessageBox.showinfo(message='It is too cold. Keep your bird warm!')
            else:
                tkMessageBox.showinfo(message='Care your bird. Maybe he has a fever.\nTake him to veteranian if you possible.')
        else:
            tkMessageBox.showinfo(message='This unit is not support!\nTry again with Celsius and Fahrenheit')

#menubar function
def aboutpro():
    tkMessageBox.showinfo(message='Nattakit Waiyawatpattarakul 57070033 \nAkkapon Chainarong 57070146')

def thanks():
    tkMessageBox.showinfo(message='We truly appreciate for your taught in resolving the problem. \
                \nProfessor Chotipat Pornavalai and Teacher Assistant Pichatorn Eak-Une \nThank you for your feedback.')

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
mGui.resizable(width=False, height=False)
mGui.config(background = '#FFFFFF')

#head and tail text 
mLabel = Label(text='Temperature Converter',fg='blue',bg='#FFFFFF',font=tkFont.Font(size=20,weight=tkFont.BOLD)).pack()
mLabel2 = Label(text='For Pet Lovers',fg='blue',bg='#FFFFFF',font = tkFont.Font(size=20,weight=tkFont.BOLD)).pack()
mLabel3 = Label(text='Faculty of Information Technology @ KMITL',bg='#FFFFFF').place(x=350,y=470)

#temperature input
tlabel = Label(text='Input Temperature',fg='black',bg='#FFFFFF',font=tkFont.Font(size=12)).place(x=40,y=125)
temp = Entry(mGui)
temp.pack(pady = 50)

#box unit
unit = StringVar()
box = ttk.Combobox(mGui,textvariable=unit,state='readonly')
box['values'] = ('Celsius', 'Fahrenheit', 'Kelvin', 'Rankine')
box.current(0)
box.place(x=400,y=127)

#convert button
convert = Button(text="Convert",command=temperature,fg='black',bg='light blue',font=tkFont.Font(size = 12))
convert.pack(pady=10)

#comfort button
p_label = Label(text='Choose Your Pet',fg='black',bg='#FFFFFF',font=tkFont.Font(size=12)).place(x=40,y=169)
pets = Button(text="Did it comfortable for pet?",command=petter,fg='black',bg='light blue',font=tkFont.Font(size = 12))
pets.pack(pady=5)

#pet box
pet = StringVar()
p_box = ttk.Combobox(mGui,textvariable=pet,state='readonly')
p_box['values'] = ('Dog', 'Cat', 'Hamster', 'Hedgehog', 'Sugar Glider', 'Bird', 'Rabbit')
p_box.current(0)
p_box.place(x=400,y=167)

#display of label
var_1 = StringVar()
var_2 = StringVar()
var_3 = StringVar()
var_4 = StringVar()
label_1 = Label(mGui, textvariable=var_1, fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12))
label_2 = Label(mGui, textvariable=var_2, fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12))
label_3 = Label(mGui, textvariable=var_3, fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12))
label_4 = Label(mGui, textvariable=var_4, fg='black',bg="#FFFFFF",font = tkFont.Font(size = 12))
label_1.pack()
label_2.pack()
label_3.pack()
label_4.pack()

#create menu bar
#about-us menu
menubar = Menu(mGui)
topmenu = Menu(menubar,tearoff=0)
topmenu.add_command(label='About Producer',command=aboutpro)
topmenu.add_command(label='Thanksgiving',command=thanks)
menubar.add_cascade(label='About Us',menu=topmenu)

#help menu
secmenu = Menu(menubar,tearoff = 0)
secmenu.add_command(label='Help Docs',command=helpdoc)
secmenu.add_command(label='How to Use',command=howto)
menubar.add_cascade(label='Help',menu=secmenu)

#exit menu
exmenu = Menu(menubar,tearoff=0)
exmenu.add_command(label='Quit',command=exitt)
menubar.add_cascade(label='Exit',menu=exmenu)

mGui.config(menu=menubar)
mGui.mainloop()

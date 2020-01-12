
import os
import subprocess
from tkinter.colorchooser import *
from tkinter import *
import sys
from SerialWrapper import SerialWrapper
print(sys.path)

ser = SerialWrapper('/COM4', 9600)


class GUI(SerialWrapper):
    ser = SerialWrapper

    def __init__(self, master):
        self.master = master
        master.title("Control Panel")

        # window.protocol('WM_DELETE_WINDOW', catchOnClose)
        window.geometry('350x350')
        window.title("RGB Backlight")
        image = PhotoImage(
            file="C:\\Users\\Ryan\\Documents\\Python Projects\\PyControlled LED\\checkitoutwithstevebrule.png")
        background_label = Label(window, image=image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        window.configure(background='white')
        lbl = Label(text="RGB Backlight Controls", font=(
            "Comic Sans", 14))
        lbl.grid(column=0, row=0)

    def onOffButtons(self):
        btn = Button(window, text="ON", bg="green",
                     command=self.clickedOn, width=10)
        btn.grid(column=0, row=1)
        btn = Button(window, text="OFF", bg="red",
                     command=self.clickedOff, width=10)
        btn.grid(column=1, row=1)

    def selectColor(self):
        lbl = Label(text="Change Color", font=(
            "Comic Sans", 12))
        lbl.grid(column=0, row=3)
        btn = Button(text='Select Color', command=self.getColor)
        btn.grid(column=0, row=4)

    def changeBrightness(self):
        btn = Button(window, text="BRIGHTER",
                     command=self.clickedBrighter, width=10)
        btn.grid(column=1, row=3)
        btn = Button(window, text="DARKER",
                     command=self.clickedDarker, width=10)
        btn.grid(column=1, row=4)

    def applicationsButtons(self):
        b1 = Button(window, text="Discord")
        b2 = Button(window, text="Steam", command=lambda: os.startfile(
            "C:\Program Files (x86)\Steam\Steam.exe"))
        b3 = Button(window, text="Google")

        b1.grid(column=4, row=1)
        b2.grid(column=4, row=3)
        b3.grid(column=4, row=6)

    def clickedOn(self):
        ser.writeCommands("ON\n")

    def clickedOff(self):
        ser.writeCommands("OFF\n")

    def clickedBrighter(self):
        ser.writeCommands("BRIGHTER\n")

    def clickedDarker(self):
        ser.writeCommands("DARKER\n")

    def clickedRainbow(self):
        ser.writeCommands("RAINBOW\n")

    def closeConnect(self):
        ser.writeCommands("CLOSE")

    def getColor(self):
        color = askcolor()
        print(color)
        if color[0] != None:
            ser.writeCommands("SOLID\n")
            print(str(str(color[0][0]) + " " + str(color[0][1]) +
                      " " + str(color[0][2])) + '\n')
            ser.writeCommands(
                str(str(color[0][0]) + " " + str(color[0][1]) +
                    " " + str(color[0][2])) + '\n')

    def catchOnClose(self):
        clickedOff()
        window.destroy()


def clickedOn():
    ser.writeCommands("ON\n")


def clickedOff():
    ser.writeCommands("OFF\n")


def clickedBrighter():
    ser.writeCommands("BRIGHTER\n")


def clickedDarker():
    ser.writeCommands("DARKER\n")


def clickedRainbow():
    ser.writeCommands("RAINBOW\n")


def closeConnect():
    ser.writeCommands("CLOSE")


def getColor():
    color = askcolor()
    print(color)
    if color[0] != None:
        ser.writeCommands("SOLID\n")
        print(str(str(color[0][0]) + " " + str(color[0][1]) +
                  " " + str(color[0][2])) + '\n')
        ser.writeCommands(
            str(str(color[0][0]) + " " + str(color[0][1]) +
                " " + str(color[0][2])) + '\n')


def catchOnClose():
    clickedOff()
    window.destroy()


window = Tk()
window.protocol('WM_DELETE_WINDOW', catchOnClose)
window.geometry('350x350')
window.title("RGB Backlight")
image = PhotoImage(
    file="C:\\Users\\Ryan\\Documents\\Python Projects\\PyControlled LED\\checkitoutwithstevebrule.png")
background_label = Label(window, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
window.configure(background='white')
lbl = Label(text="RGB Backlight Controls", font=(
    "Comic Sans", 14))
lbl.grid(column=0, row=0)
btn = Button(window, text="ON", bg="green", command=clickedOn, width=10)
btn.grid(column=0, row=1)
btn = Button(window, text="OFF", bg="red", command=clickedOff, width=10)
btn.grid(column=1, row=1)
lbl = Label(text="Change Color", font=(
    "Comic Sans", 12))
lbl.grid(column=0, row=3)
btn = Button(text='Select Color', command=getColor)
btn.grid(column=0, row=4)
btn = Button(window, text="BRIGHTER", command=clickedBrighter, width=10)
btn.grid(column=1, row=3)
btn = Button(window, text="DARKER", command=clickedDarker, width=10)
btn.grid(column=1, row=4)

b1 = Button(window, text="Discord")
b2 = Button(window, text="Steam", command=lambda: os.startfile(
    "C:\Program Files (x86)\Steam\Steam.exe"))
b3 = Button(window, text="Google")

b1.grid(column=4, row=1)
b2.grid(column=4, row=3)
b3.grid(column=4, row=6)
mainloop()
window.mainloop()

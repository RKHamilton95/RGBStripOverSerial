from tkinter import *
from SerialStart import writeCommands

colors = {
    "RED", "ORANGE", "YELLOW", "GREEN", "LIGHTBLUE", "BLUE", "INDIGO", "WHITE"
}


def clickedOn():
    writeCommands("ON\n")


def clickedOff():
    writeCommands("OFF\n")


def clickedBrighter():
    writeCommands("BRIGHTER\n")


def clickedDarker():
    writeCommands("DARKER\n")


def clickedSolid():
    writeCommands("SOLID\n")
    print(optionVar.get())
    writeCommands(optionVar.get()+"\n")


def clickedRainbow():
    writeCommands("RAINBOW\n")


def closeConnect():
    writeCommands("CLOSE")


window = Tk()
optionVar = StringVar(window)
optionVar.set("RED")
window.geometry('300x300')
window.title("RGB Backlight")
window.configure(background='white')
lbl = Label(text="RGB Backlight Control", font=(
    "Comic Sans", 16), bg='white', justify=CENTER)
lbl.grid(column=1, row=0)
btn = Button(window, text="ON", bg="green", command=clickedOn, width=10)
btn.grid(column=1, row=1)
btn = Button(window, text="OFF", bg="red", command=clickedOff, width=10)
btn.grid(column=1, row=2)
w = OptionMenu(window, optionVar, *colors)
w.grid(column=1, row=3)
btn = Button(window, text="Set Color", command=clickedSolid, width=10)
btn.grid(column=1, row=4)
btn = Button(window, text="BRIGHTER", command=clickedBrighter, width=10)
btn.grid(column=1, row=5)
btn = Button(window, text="DARKER", command=clickedDarker, width=10)
btn.grid(column=1, row=6)
btn = Button(window, text="CLOSE", command=closeConnect, width=10)
btn.grid(column=1, row=7)
btn = Button(window, text="RAINBOW", command=clickedRainbow, width=10)
btn.grid(column=1, row=8)
window.mainloop()

from tkinter.colorchooser import *
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


def clickedRainbow():
    writeCommands("RAINBOW\n")


def closeConnect():
    writeCommands("CLOSE")


def getColor():
    color = askcolor()
    print(color)
    writeCommands("SOLID\n")
    print(str(str(color[0][0]) + " " + str(color[0][1]) +
              " " + str(color[0][2])) + '\n')
    writeCommands(
        str(str(color[0][0]) + " " + str(color[0][1]) +
            " " + str(color[0][2])) + '\n')


window = Tk()
window.geometry('350x350')
window.title("RGB Backlight")
image = PhotoImage(
    file="./images/checkitoutwithstevebrule.logo.png")
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
# btn = Button(window, text="Set Color", command=clickedSolid, width=10)
# btn.grid(column=0, row=5)
btn = Button(window, text="BRIGHTER", command=clickedBrighter, width=10)
btn.grid(column=1, row=3)
btn = Button(window, text="DARKER", command=clickedDarker, width=10)
btn.grid(column=1, row=4)
# btn = Button(window, text="CLOSE", command=closeConnect, width=10)
# btn.grid(column=2, row=4)
# btn = Button(window, text="RAINBOW", command=clickedRainbow, width=10)
# btn.grid(column=2, row=3)
mainloop()
window.mainloop()

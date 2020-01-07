from tkinter.colorchooser import *
from tkinter import *
from SerialStart import SerialWrapper

ser = SerialWrapper('/COM4')

colors = {
    "RED", "ORANGE", "YELLOW", "GREEN", "LIGHTBLUE", "BLUE", "INDIGO", "WHITE"
}


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
mainloop()
window.mainloop()

# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# GUI module generated by PAGE version 4.26
# in conjunction with Tcl version 8.6
# Jan 11, 2020 02:37:32 PM EST  platform: Windows NT
import sys
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import customGUI_support
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    customGUI_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    customGUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("687x449+1253+589")
        top.minsize(120, 1)
        top.maxsize(7684, 1421)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#2C2F33")
        top.configure(highlightbackground="#c0c0c0")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg='#bcbcbc')
        top.configure(menu = self.menubar)

        self.OFFButton = tk.Button(top)
        self.OFFButton.place(relx=0.159, rely=0.089, height=34, width=57)
        self.OFFButton.configure(activebackground="#c60000")
        self.OFFButton.configure(activeforeground="white")
        self.OFFButton.configure(activeforeground="#000000")
        self.OFFButton.configure(background="#c60000")
        self.OFFButton.configure(disabledforeground="#a3a3a3")
        self.OFFButton.configure(foreground="#000000")
        self.OFFButton.configure(highlightbackground="#d9d9d9")
        self.OFFButton.configure(highlightcolor="black")
        self.OFFButton.configure(pady="0")
        self.OFFButton.configure(text='''OFF''')

        self.ONButton = tk.Button(top)
        self.ONButton.place(relx=0.064, rely=0.089, height=34, width=57)
        self.ONButton.configure(activebackground="#00e111")
        self.ONButton.configure(activeforeground="black")
        self.ONButton.configure(background="#00e111")
        self.ONButton.configure(disabledforeground="#00e111")
        self.ONButton.configure(foreground="#000000")
        self.ONButton.configure(highlightbackground="#d9d9d9")
        self.ONButton.configure(highlightcolor="black")
        self.ONButton.configure(pady="0")
        self.ONButton.configure(text='''ON''')

        self.SteamBtn = tk.Button(top)
        self.SteamBtn.place(relx=0.408, rely=0.178, height=64, width=64)
        self.SteamBtn.configure(activebackground="#2C2F33")
        self.SteamBtn.configure(activeforeground="white")
        self.SteamBtn.configure(activeforeground="#2C2F33")
        self.SteamBtn.configure(background="#2C2F33")
        self.SteamBtn.configure(cursor="hand2")
        self.SteamBtn.configure(disabledforeground="#a3a3a3")
        self.SteamBtn.configure(foreground="#000000")
        self.SteamBtn.configure(highlightbackground="#d9d9d9")
        self.SteamBtn.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"/Users/Ryan/Documents/PythonProjects/PyControlledLED/PyDashBoard/images/steamIcon.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.SteamBtn.configure(image=_img0)
        self.SteamBtn.configure(padx="0")
        self.SteamBtn.configure(pady="0")
        self.SteamBtn.configure(relief="flat")

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.32, rely=0.022, relheight=0.958)
        self.TSeparator1.configure(orient="vertical")

        self.TSeparator2 = ttk.Separator(top)
        self.TSeparator2.place(relx=0.015, rely=0.539, relwidth=0.917)

        self.BrightnessLbl = tk.Label(top)
        self.BrightnessLbl.place(relx=0.07, rely=0.318, height=21, width=114)
        self.BrightnessLbl.configure(activebackground="#f9f9f9")
        self.BrightnessLbl.configure(activeforeground="black")
        self.BrightnessLbl.configure(background="#d9d9d9")
        self.BrightnessLbl.configure(disabledforeground="#a3a3a3")
        self.BrightnessLbl.configure(font="-family {Yu Gothic UI Semibold} -size 13 -weight bold")
        self.BrightnessLbl.configure(foreground="#2C2F33")
        self.BrightnessLbl.configure(highlightbackground="#d9d9d9")
        self.BrightnessLbl.configure(highlightcolor="black")
        self.BrightnessLbl.configure(text='''Brightness''')

        self.BacklightLbl = tk.Label(top)
        self.BacklightLbl.place(relx=0.044, rely=0.022, height=21, width=154)
        self.BacklightLbl.configure(activebackground="#f9f9f9")
        self.BacklightLbl.configure(activeforeground="black")
        self.BacklightLbl.configure(background="#d9d9d9")
        self.BacklightLbl.configure(disabledforeground="#a3a3a3")
        self.BacklightLbl.configure(font="-family {Yu Gothic UI Semibold} -size 13 -weight bold")
        self.BacklightLbl.configure(foreground="#000000")
        self.BacklightLbl.configure(highlightbackground="#d9d9d9")
        self.BacklightLbl.configure(highlightcolor="#000000")
        self.BacklightLbl.configure(text='''Backlight Control''')

        self.SelectAColorLbl = tk.Label(top)
        self.SelectAColorLbl.place(relx=0.044, rely=0.178, height=21, width=154)
        self.SelectAColorLbl.configure(activebackground="#f9f9f9")
        self.SelectAColorLbl.configure(activeforeground="black")
        self.SelectAColorLbl.configure(background="#d9d9d9")
        self.SelectAColorLbl.configure(disabledforeground="#a3a3a3")
        self.SelectAColorLbl.configure(font="-family {Yu Gothic UI Semibold} -size 13 -weight bold")
        self.SelectAColorLbl.configure(foreground="#000000")
        self.SelectAColorLbl.configure(highlightbackground="#d9d9d9")
        self.SelectAColorLbl.configure(highlightcolor="black")
        self.SelectAColorLbl.configure(text='''Select A Color''')

        self.SelectAColorBtn = tk.Button(top)
        self.SelectAColorBtn.place(relx=0.087, rely=0.245, height=24, width=97)
        self.SelectAColorBtn.configure(activebackground="#ececec")
        self.SelectAColorBtn.configure(activeforeground="#000000")
        self.SelectAColorBtn.configure(background="#d9d9d9")
        self.SelectAColorBtn.configure(disabledforeground="#a3a3a3")
        self.SelectAColorBtn.configure(foreground="#000000")
        self.SelectAColorBtn.configure(highlightbackground="#d9d9d9")
        self.SelectAColorBtn.configure(highlightcolor="black")
        self.SelectAColorBtn.configure(pady="0")
        self.SelectAColorBtn.configure(text='''Select a color''')

        self.BacklightLbl_10 = tk.Label(top)
        self.BacklightLbl_10.place(relx=0.48, rely=0.022, height=41, width=204)
        self.BacklightLbl_10.configure(activebackground="#f9f9f9")
        self.BacklightLbl_10.configure(activeforeground="black")
        self.BacklightLbl_10.configure(background="#d9d9d9")
        self.BacklightLbl_10.configure(disabledforeground="#a3a3a3")
        self.BacklightLbl_10.configure(font="-family {Yu Gothic UI Semibold} -size 20 -weight bold")
        self.BacklightLbl_10.configure(foreground="#000000")
        self.BacklightLbl_10.configure(highlightbackground="#d9d9d9")
        self.BacklightLbl_10.configure(highlightcolor="black")
        self.BacklightLbl_10.configure(text='''Applications''')

        self.SteamBtn_12 = tk.Button(top)
        self.SteamBtn_12.place(relx=0.524, rely=0.178, height=64, width=64)
        self.SteamBtn_12.configure(activebackground="#2C2F33")
        self.SteamBtn_12.configure(activeforeground="white")
        self.SteamBtn_12.configure(activeforeground="#2C2F33")
        self.SteamBtn_12.configure(background="#2C2F33")
        self.SteamBtn_12.configure(cursor="hand2")
        self.SteamBtn_12.configure(disabledforeground="#a3a3a3")
        self.SteamBtn_12.configure(foreground="#000000")
        self.SteamBtn_12.configure(highlightbackground="#d9d9d9")
        self.SteamBtn_12.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"/Users/Ryan/Documents/PythonProjects/PyControlledLED/PyDashBoard/images/discord.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.SteamBtn_12.configure(image=_img1)
        self.SteamBtn_12.configure(padx="0")
        self.SteamBtn_12.configure(pady="0")
        self.SteamBtn_12.configure(relief="flat")
        self.SteamBtn_12.configure(takefocus="0")

        self.SteamBtn_13 = tk.Button(top)
        self.SteamBtn_13.place(relx=0.64, rely=0.178, height=64, width=64)
        self.SteamBtn_13.configure(activebackground="#2C2F33")
        self.SteamBtn_13.configure(activeforeground="white")
        self.SteamBtn_13.configure(activeforeground="#2C2F33")
        self.SteamBtn_13.configure(background="#2C2F33")
        self.SteamBtn_13.configure(cursor="hand2")
        self.SteamBtn_13.configure(disabledforeground="#a3a3a3")
        self.SteamBtn_13.configure(foreground="#000000")
        self.SteamBtn_13.configure(highlightbackground="#d9d9d9")
        self.SteamBtn_13.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"/Users/Ryan/Documents/PythonProjects/PyControlledLED/PyDashBoard/images/steamIcon.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.SteamBtn_13.configure(image=_img2)
        self.SteamBtn_13.configure(padx="0")
        self.SteamBtn_13.configure(pady="0")
        self.SteamBtn_13.configure(relief="flat")
        self.SteamBtn_13.configure(takefocus="0")

        self.SteamBtn_14 = tk.Button(top)
        self.SteamBtn_14.place(relx=0.757, rely=0.178, height=64, width=64)
        self.SteamBtn_14.configure(activebackground="#2C2F33")
        self.SteamBtn_14.configure(activeforeground="white")
        self.SteamBtn_14.configure(activeforeground="#2C2F33")
        self.SteamBtn_14.configure(background="#2C2F33")
        self.SteamBtn_14.configure(cursor="hand2")
        self.SteamBtn_14.configure(disabledforeground="#a3a3a3")
        self.SteamBtn_14.configure(foreground="#000000")
        self.SteamBtn_14.configure(highlightbackground="#d9d9d9")
        self.SteamBtn_14.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"/Users/Ryan/Documents/PythonProjects/PyControlledLED/PyDashBoard/images/steamIcon.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.SteamBtn_14.configure(image=_img3)
        self.SteamBtn_14.configure(padx="0")
        self.SteamBtn_14.configure(pady="0")
        self.SteamBtn_14.configure(relief="flat")
        self.SteamBtn_14.configure(takefocus="0")

        self.SteamBtn_1 = tk.Button(top)
        self.SteamBtn_1.place(relx=0.408, rely=0.334, height=64, width=64)
        self.SteamBtn_1.configure(activebackground="#2C2F33")
        self.SteamBtn_1.configure(activeforeground="white")
        self.SteamBtn_1.configure(activeforeground="#2C2F33")
        self.SteamBtn_1.configure(background="#2C2F33")
        self.SteamBtn_1.configure(cursor="hand2")
        self.SteamBtn_1.configure(disabledforeground="#a3a3a3")
        self.SteamBtn_1.configure(foreground="#000000")
        self.SteamBtn_1.configure(highlightbackground="#d9d9d9")
        self.SteamBtn_1.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"/Users/Ryan/Documents/PythonProjects/PyControlledLED/PyDashBoard/images/steamIcon.png")
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.SteamBtn_1.configure(image=_img4)
        self.SteamBtn_1.configure(padx="0")
        self.SteamBtn_1.configure(pady="0")
        self.SteamBtn_1.configure(relief="flat")
        self.SteamBtn_1.configure(takefocus="0")

        self.SteamBtn_2 = tk.Button(top)
        self.SteamBtn_2.place(relx=0.524, rely=0.334, height=64, width=64)
        self.SteamBtn_2.configure(activebackground="#2C2F33")
        self.SteamBtn_2.configure(activeforeground="white")
        self.SteamBtn_2.configure(activeforeground="#2C2F33")
        self.SteamBtn_2.configure(background="#2C2F33")
        self.SteamBtn_2.configure(cursor="hand2")
        self.SteamBtn_2.configure(disabledforeground="#a3a3a3")
        self.SteamBtn_2.configure(foreground="#000000")
        self.SteamBtn_2.configure(highlightbackground="#d9d9d9")
        self.SteamBtn_2.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"/Users/Ryan/Documents/PythonProjects/PyControlledLED/PyDashBoard/images/steamIcon.png")
        global _img5
        _img5 = tk.PhotoImage(file=photo_location)
        self.SteamBtn_2.configure(image=_img5)
        self.SteamBtn_2.configure(padx="0")
        self.SteamBtn_2.configure(pady="0")
        self.SteamBtn_2.configure(relief="flat")
        self.SteamBtn_2.configure(takefocus="0")

        self.SteamBtn_3 = tk.Button(top)
        self.SteamBtn_3.place(relx=0.64, rely=0.334, height=64, width=64)
        self.SteamBtn_3.configure(activebackground="#2C2F33")
        self.SteamBtn_3.configure(activeforeground="white")
        self.SteamBtn_3.configure(activeforeground="#2C2F33")
        self.SteamBtn_3.configure(background="#2C2F33")
        self.SteamBtn_3.configure(cursor="hand2")
        self.SteamBtn_3.configure(disabledforeground="#a3a3a3")
        self.SteamBtn_3.configure(foreground="#000000")
        self.SteamBtn_3.configure(highlightbackground="#d9d9d9")
        self.SteamBtn_3.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"/Users/Ryan/Documents/PythonProjects/PyControlledLED/PyDashBoard/images/steamIcon.png")
        global _img6
        _img6 = tk.PhotoImage(file=photo_location)
        self.SteamBtn_3.configure(image=_img6)
        self.SteamBtn_3.configure(padx="0")
        self.SteamBtn_3.configure(pady="0")
        self.SteamBtn_3.configure(relief="flat")
        self.SteamBtn_3.configure(takefocus="0")

        self.SteamBtn_4 = tk.Button(top)
        self.SteamBtn_4.place(relx=0.757, rely=0.334, height=64, width=64)
        self.SteamBtn_4.configure(activebackground="#2C2F33")
        self.SteamBtn_4.configure(activeforeground="white")
        self.SteamBtn_4.configure(activeforeground="#2C2F33")
        self.SteamBtn_4.configure(background="#2C2F33")
        self.SteamBtn_4.configure(cursor="hand2")
        self.SteamBtn_4.configure(disabledforeground="#a3a3a3")
        self.SteamBtn_4.configure(foreground="#000000")
        self.SteamBtn_4.configure(highlightbackground="#d9d9d9")
        self.SteamBtn_4.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"/Users/Ryan/Documents/PythonProjects/PyControlledLED/PyDashBoard/images/steamIcon.png")
        global _img7
        _img7 = tk.PhotoImage(file=photo_location)
        self.SteamBtn_4.configure(image=_img7)
        self.SteamBtn_4.configure(padx="0")
        self.SteamBtn_4.configure(pady="0")
        self.SteamBtn_4.configure(relief="flat")
        self.SteamBtn_4.configure(takefocus="0")

        self.TScale2 = ttk.Scale(top, from_=0, to=1.0)
        self.TScale2.place(relx=0.079, rely=0.383, relwidth=0.146, relheight=0.0
                , height=26, bordermode='ignore')
        self.TScale2.configure(length="255")
        self.TScale2.configure(takefocus="")

        self.TFrame1 = ttk.Frame(top)
        self.TFrame1.place(relx=0.349, rely=0.561, relheight=0.412
                , relwidth=0.59)
        self.TFrame1.configure(relief='raised')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="raised")
        self.TFrame1.configure(takefocus="0")

        self.TScale1_21 = ttk.Scale(self.TFrame1, from_=0, to=1.0)
        self.TScale1_21.place(relx=0.328, rely=0.054, relwidth=0.0
                , relheight=0.703, width=35, bordermode='ignore')
        self.TScale1_21.configure(orient="vertical")
        self.TScale1_21.configure(takefocus="")

        self.TScale1_20 = ttk.Scale(self.TFrame1, from_=0, to=1.0)
        self.TScale1_20.place(relx=0.449, rely=0.054, relwidth=0.0
                , relheight=0.703, width=35, bordermode='ignore')
        self.TScale1_20.configure(orient="vertical")
        self.TScale1_20.configure(takefocus="")

        self.TScale1_5 = ttk.Scale(self.TFrame1, from_=0, to=1.0)
        self.TScale1_5.place(relx=0.578, rely=0.054, relwidth=0.0
                , relheight=0.703, width=35, bordermode='ignore')
        self.TScale1_5.configure(orient="vertical")
        self.TScale1_5.configure(takefocus="")

        self.TScale1_6 = ttk.Scale(self.TFrame1, from_=0, to=1.0)
        self.TScale1_6.place(relx=0.709, rely=0.054, relwidth=0.0
                , relheight=0.703, width=35, bordermode='ignore')
        self.TScale1_6.configure(orient="vertical")
        self.TScale1_6.configure(takefocus="")

        self.TScale1_7 = ttk.Scale(self.TFrame1, from_=0, to=1.0)
        self.TScale1_7.place(relx=0.844, rely=0.054, relwidth=0.0
                , relheight=0.703, width=35, bordermode='ignore')
        self.TScale1_7.configure(orient="vertical")
        self.TScale1_7.configure(takefocus="")

        self.TScale1_22 = ttk.Scale(self.TFrame1, from_=0, to=1.0)
        self.TScale1_22.place(relx=0.198, rely=0.054, relwidth=0.0
                , relheight=0.703, width=35, bordermode='ignore')
        self.TScale1_22.configure(orient="vertical")
        self.TScale1_22.configure(takefocus="")

        self.TScale1_23 = ttk.Scale(self.TFrame1, from_=0, to=1.0)
        self.TScale1_23.place(relx=0.069, rely=0.054, relwidth=0.0
                , relheight=0.703, width=35, bordermode='ignore')
        self.TScale1_23.configure(orient="vertical")
        self.TScale1_23.configure(takefocus="")

        self.Button1 = tk.Button(self.TFrame1)
        self.Button1.place(relx=0.067, rely=0.778, height=34, width=37)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Button''')

        self.Button1_9 = tk.Button(self.TFrame1)
        self.Button1_9.place(relx=0.195, rely=0.778, height=34, width=37)
        self.Button1_9.configure(activebackground="#ececec")
        self.Button1_9.configure(activeforeground="#000000")
        self.Button1_9.configure(background="#d9d9d9")
        self.Button1_9.configure(disabledforeground="#a3a3a3")
        self.Button1_9.configure(foreground="#000000")
        self.Button1_9.configure(highlightbackground="#d9d9d9")
        self.Button1_9.configure(highlightcolor="black")
        self.Button1_9.configure(pady="0")
        self.Button1_9.configure(text='''Button''')

        self.Button1_10 = tk.Button(self.TFrame1)
        self.Button1_10.place(relx=0.326, rely=0.778, height=34, width=37)
        self.Button1_10.configure(activebackground="#ececec")
        self.Button1_10.configure(activeforeground="#000000")
        self.Button1_10.configure(background="#d9d9d9")
        self.Button1_10.configure(disabledforeground="#a3a3a3")
        self.Button1_10.configure(foreground="#000000")
        self.Button1_10.configure(highlightbackground="#d9d9d9")
        self.Button1_10.configure(highlightcolor="black")
        self.Button1_10.configure(pady="0")
        self.Button1_10.configure(text='''Button''')

        self.Button1_11 = tk.Button(self.TFrame1)
        self.Button1_11.place(relx=0.447, rely=0.778, height=34, width=37)
        self.Button1_11.configure(activebackground="#ececec")
        self.Button1_11.configure(activeforeground="#000000")
        self.Button1_11.configure(background="#d9d9d9")
        self.Button1_11.configure(disabledforeground="#a3a3a3")
        self.Button1_11.configure(foreground="#000000")
        self.Button1_11.configure(highlightbackground="#d9d9d9")
        self.Button1_11.configure(highlightcolor="black")
        self.Button1_11.configure(pady="0")
        self.Button1_11.configure(text='''Button''')

        self.Button1_12 = tk.Button(self.TFrame1)
        self.Button1_12.place(relx=0.575, rely=0.778, height=34, width=37)
        self.Button1_12.configure(activebackground="#ececec")
        self.Button1_12.configure(activeforeground="#000000")
        self.Button1_12.configure(background="#d9d9d9")
        self.Button1_12.configure(disabledforeground="#a3a3a3")
        self.Button1_12.configure(foreground="#000000")
        self.Button1_12.configure(highlightbackground="#d9d9d9")
        self.Button1_12.configure(highlightcolor="black")
        self.Button1_12.configure(pady="0")
        self.Button1_12.configure(text='''Button''')

        self.Button1_13 = tk.Button(self.TFrame1)
        self.Button1_13.place(relx=0.706, rely=0.778, height=34, width=37)
        self.Button1_13.configure(activebackground="#ececec")
        self.Button1_13.configure(activeforeground="#000000")
        self.Button1_13.configure(background="#d9d9d9")
        self.Button1_13.configure(disabledforeground="#a3a3a3")
        self.Button1_13.configure(foreground="#000000")
        self.Button1_13.configure(highlightbackground="#d9d9d9")
        self.Button1_13.configure(highlightcolor="black")
        self.Button1_13.configure(pady="0")
        self.Button1_13.configure(text='''Button''')

        self.Button1_14 = tk.Button(self.TFrame1)
        self.Button1_14.place(relx=0.844, rely=0.778, height=34, width=37)
        self.Button1_14.configure(activebackground="#ececec")
        self.Button1_14.configure(activeforeground="#000000")
        self.Button1_14.configure(background="#d9d9d9")
        self.Button1_14.configure(disabledforeground="#a3a3a3")
        self.Button1_14.configure(foreground="#000000")
        self.Button1_14.configure(highlightbackground="#d9d9d9")
        self.Button1_14.configure(highlightcolor="black")
        self.Button1_14.configure(pady="0")
        self.Button1_14.configure(text='''Button''')

        self.SetBrightnessBtn = tk.Button(top)
        self.SetBrightnessBtn.place(relx=0.087, rely=0.448, height=24, width=87)
        self.SetBrightnessBtn.configure(activebackground="#ececec")
        self.SetBrightnessBtn.configure(activeforeground="#000000")
        self.SetBrightnessBtn.configure(background="#d9d9d9")
        self.SetBrightnessBtn.configure(disabledforeground="#a3a3a3")
        self.SetBrightnessBtn.configure(foreground="#000000")
        self.SetBrightnessBtn.configure(highlightbackground="#d9d9d9")
        self.SetBrightnessBtn.configure(highlightcolor="black")
        self.SetBrightnessBtn.configure(pady="0")
        self.SetBrightnessBtn.configure(text='''Set Brightness''')

        self.TFrame2 = ttk.Frame(top)
        self.TFrame2.place(relx=0.015, rely=0.557, relheight=0.412
                , relwidth=0.298)
        self.TFrame2.configure(relief='raised')
        self.TFrame2.configure(borderwidth="2")
        self.TFrame2.configure(relief="raised")

        self.BacklightLbl_11 = tk.Label(self.TFrame2)
        self.BacklightLbl_11.place(relx=0.0, rely=0.0, height=41, width=204)
        self.BacklightLbl_11.configure(activebackground="#f9f9f9")
        self.BacklightLbl_11.configure(activeforeground="black")
        self.BacklightLbl_11.configure(background="#d9d9d9")
        self.BacklightLbl_11.configure(disabledforeground="#a3a3a3")
        self.BacklightLbl_11.configure(font="-family {Yu Gothic UI Semibold} -size 20 -weight bold")
        self.BacklightLbl_11.configure(foreground="#000000")
        self.BacklightLbl_11.configure(highlightbackground="#d9d9d9")
        self.BacklightLbl_11.configure(highlightcolor="black")
        self.BacklightLbl_11.configure(text='''Media''')

        self.SteamBtn_13 = tk.Button(self.TFrame2)
        self.SteamBtn_13.place(relx=0.049, rely=0.27, height=54, width=54)
        self.SteamBtn_13.configure(activebackground="#2C2F33")
        self.SteamBtn_13.configure(activeforeground="white")
        self.SteamBtn_13.configure(activeforeground="#2C2F33")
        self.SteamBtn_13.configure(background="#2C2F33")
        self.SteamBtn_13.configure(cursor="hand2")
        self.SteamBtn_13.configure(disabledforeground="#a3a3a3")
        self.SteamBtn_13.configure(foreground="#000000")
        self.SteamBtn_13.configure(highlightbackground="#d9d9d9")
        self.SteamBtn_13.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"/Users/Ryan/Documents/PythonProjects/PyControlledLED/PyDashBoard/images/steamIcon.png")
        global _img8
        _img8 = tk.PhotoImage(file=photo_location)
        self.SteamBtn_13.configure(image=_img8)
        self.SteamBtn_13.configure(padx="0")
        self.SteamBtn_13.configure(pady="0")
        self.SteamBtn_13.configure(relief="flat")

        self.SteamBtn_14 = tk.Button(self.TFrame2)
        self.SteamBtn_14.place(relx=0.356, rely=0.27, height=54, width=54)
        self.SteamBtn_14.configure(activebackground="#2C2F33")
        self.SteamBtn_14.configure(activeforeground="white")
        self.SteamBtn_14.configure(activeforeground="#2C2F33")
        self.SteamBtn_14.configure(background="#2C2F33")
        self.SteamBtn_14.configure(cursor="hand2")
        self.SteamBtn_14.configure(disabledforeground="#a3a3a3")
        self.SteamBtn_14.configure(foreground="#000000")
        self.SteamBtn_14.configure(highlightbackground="#d9d9d9")
        self.SteamBtn_14.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"/Users/Ryan/Documents/PythonProjects/PyControlledLED/PyDashBoard/images/steamIcon.png")
        global _img9
        _img9 = tk.PhotoImage(file=photo_location)
        self.SteamBtn_14.configure(image=_img9)
        self.SteamBtn_14.configure(padx="0")
        self.SteamBtn_14.configure(pady="0")
        self.SteamBtn_14.configure(relief="flat")

        self.SteamBtn_15 = tk.Button(self.TFrame2)
        self.SteamBtn_15.place(relx=0.683, rely=0.27, height=54, width=54)
        self.SteamBtn_15.configure(activebackground="#2C2F33")
        self.SteamBtn_15.configure(activeforeground="white")
        self.SteamBtn_15.configure(activeforeground="#2C2F33")
        self.SteamBtn_15.configure(background="#2C2F33")
        self.SteamBtn_15.configure(cursor="hand2")
        self.SteamBtn_15.configure(disabledforeground="#a3a3a3")
        self.SteamBtn_15.configure(foreground="#000000")
        self.SteamBtn_15.configure(highlightbackground="#d9d9d9")
        self.SteamBtn_15.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"/Users/Ryan/Documents/PythonProjects/PyControlledLED/PyDashBoard/images/steamIcon.png")
        global _img10
        _img10 = tk.PhotoImage(file=photo_location)
        self.SteamBtn_15.configure(image=_img10)
        self.SteamBtn_15.configure(padx="0")
        self.SteamBtn_15.configure(pady="0")
        self.SteamBtn_15.configure(relief="flat")

        self.SteamBtn_16 = tk.Button(self.TFrame2)
        self.SteamBtn_16.place(relx=0.049, rely=0.595, height=54, width=54)
        self.SteamBtn_16.configure(activebackground="#2C2F33")
        self.SteamBtn_16.configure(activeforeground="white")
        self.SteamBtn_16.configure(activeforeground="#2C2F33")
        self.SteamBtn_16.configure(background="#2C2F33")
        self.SteamBtn_16.configure(cursor="hand2")
        self.SteamBtn_16.configure(disabledforeground="#a3a3a3")
        self.SteamBtn_16.configure(foreground="#000000")
        self.SteamBtn_16.configure(highlightbackground="#d9d9d9")
        self.SteamBtn_16.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"/Users/Ryan/Documents/PythonProjects/PyControlledLED/PyDashBoard/images/steamIcon.png")
        global _img11
        _img11 = tk.PhotoImage(file=photo_location)
        self.SteamBtn_16.configure(image=_img11)
        self.SteamBtn_16.configure(padx="0")
        self.SteamBtn_16.configure(pady="0")
        self.SteamBtn_16.configure(relief="flat")

        self.SteamBtn_17 = tk.Button(self.TFrame2)
        self.SteamBtn_17.place(relx=0.361, rely=0.595, height=54, width=54)
        self.SteamBtn_17.configure(activebackground="#2C2F33")
        self.SteamBtn_17.configure(activeforeground="white")
        self.SteamBtn_17.configure(activeforeground="#2C2F33")
        self.SteamBtn_17.configure(background="#2C2F33")
        self.SteamBtn_17.configure(cursor="hand2")
        self.SteamBtn_17.configure(disabledforeground="#a3a3a3")
        self.SteamBtn_17.configure(foreground="#000000")
        self.SteamBtn_17.configure(highlightbackground="#d9d9d9")
        self.SteamBtn_17.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"/Users/Ryan/Documents/PythonProjects/PyControlledLED/PyDashBoard/images/steamIcon.png")
        global _img12
        _img12 = tk.PhotoImage(file=photo_location)
        self.SteamBtn_17.configure(image=_img12)
        self.SteamBtn_17.configure(padx="0")
        self.SteamBtn_17.configure(pady="0")
        self.SteamBtn_17.configure(relief="flat")

        self.SteamBtn_18 = tk.Button(self.TFrame2)
        self.SteamBtn_18.place(relx=0.683, rely=0.595, height=54, width=54)
        self.SteamBtn_18.configure(activebackground="#2C2F33")
        self.SteamBtn_18.configure(activeforeground="white")
        self.SteamBtn_18.configure(activeforeground="#2C2F33")
        self.SteamBtn_18.configure(background="#2C2F33")
        self.SteamBtn_18.configure(cursor="hand2")
        self.SteamBtn_18.configure(disabledforeground="#a3a3a3")
        self.SteamBtn_18.configure(foreground="#000000")
        self.SteamBtn_18.configure(highlightbackground="#d9d9d9")
        self.SteamBtn_18.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"/Users/Ryan/Documents/PythonProjects/PyControlledLED/PyDashBoard/images/steamIcon.png")
        global _img13
        _img13 = tk.PhotoImage(file=photo_location)
        self.SteamBtn_18.configure(image=_img13)
        self.SteamBtn_18.configure(padx="0")
        self.SteamBtn_18.configure(pady="0")
        self.SteamBtn_18.configure(relief="flat")

if __name__ == '__main__':
    vp_start_gui()


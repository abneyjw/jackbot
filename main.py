from tkinter import *
from tkinter import ttk
from ctypes import windll
import time
from spotify import *
windll.shcore.SetProcessDpiAwareness(1)




mySpot = Spotify()
mySpot.setup()
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
title= ttk.Label(frm, text="Spotify")
title.grid(column=0, row=0)
ttk.Button(frm, text="Pause", command=lambda: mySpot.interact("pause")).grid(column=1, row=1)
ttk.Button(frm, text="Play", command=lambda: mySpot.interact("play")).grid(column=2, row=1)

while True:
    title["text"]= mySpot.current()
    root.update()



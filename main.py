from tkinter import *
from tkinter import ttk
from ctypes import windll
import time
from spotify import *
windll.shcore.SetProcessDpiAwareness(1)

n = 0

mySpot = Spotify()
mySpot.setup()
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
title= ttk.Label(frm, text="Spotify")
title.grid(column=0, row=0)
ttk.Button(frm, text="Prev", command=lambda: mySpot.interact("prev")).grid(column=1, row=1)
ttk.Button(frm, text="Play/Pause", command=lambda: mySpot.interact("toggle")).grid(column=2, row=1)
ttk.Button(frm, text="Skip", command=lambda: mySpot.interact("skip")).grid(column=3, row=1)

while True:
    if (n == 10):
        title["text"]= mySpot.current()
        if(not mySpot.playing()):
            title["text"] = title["text"] + " (paused)"
        n = 0
    root.update()
    n = n + 1

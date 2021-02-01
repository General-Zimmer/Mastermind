from tkinter import *


gui = Tk()
gui.title("MustardMind")
gui.geometry("1000x500")
for i in range(10):
    gui.columnconfigure(i, weight=2)
for i in range(4):
    gui.rowconfigure(i, weight=2)
for i in range(2):
    gui.rowconfigure(i + 4, weight=1)

backg = Label(gui, bg="grey")
backg.grid(column=0, row=0, columnspan=10, rowspan=4, sticky="NESW")
UI = Label(gui, bg="black")
UI.grid(column=0, row=4, columnspan=10, rowspan=2, sticky="NESW")


GuessLst = []
def AddColor(n):
    GuessLst.append(n)
    print(GuessLst)
def AddGreen():
    AddColor("dark green")
def AddRed():
    AddColor("dark red")
def AddBlue():
    AddColor("dark blue")
def AddYellow():
    AddColor("Yellow")
def AddPurple():
    AddColor("purple")
def AddWhite():
    AddColor("white")

green = Button(gui, bg="dark green", command=AddGreen)
green.grid(column=0, row=4, sticky="NESW")
red = Button(gui, bg="dark red", command=AddRed)
red.grid(column=1, row=4, sticky="NESW")
yellow = Button(gui, bg="yellow", command=AddYellow)
yellow.grid(column=1, row=5, sticky="NESW")
blue = Button(gui, bg="dark blue", command=AddBlue)
blue.grid(column=0, row=5, sticky="NESW")
purple = Button(gui, bg="purple", command=AddPurple)
purple.grid(column=2, row=5, sticky="NESW")
white = Button(gui, bg="white", command=AddWhite)
white.grid(column=2, row=4, sticky="NESW")

gui.mainloop()

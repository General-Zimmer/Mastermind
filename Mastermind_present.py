from tkinter import *
import Mastermind_Logic as logic
# import random

nguess = 10
ncombi = 4
ncolour = 6

gui = Tk()
gui.title("MustardMind")
gui.geometry("1000x500")
for i in range(nguess):
    gui.columnconfigure(i, weight=2)
for i in range(ncombi):
    gui.rowconfigure(i, weight=2)
for i in range(2):
    gui.rowconfigure(i + ncombi, weight=1)

game = logic.dinLogik()
game.makeStart(ncombi)

backg = Label(gui, bg="grey")
backg.grid(column=0, row=0, columnspan=nguess, rowspan=ncombi, sticky="NESW")
for i in range(nguess+1):
    backg.columnconfigure(i, weight=2)
for i in range(ncombi):
    backg.rowconfigure(i, weight=2)

UI = Label(gui, bg="black")
UI.grid(column=0, row=ncombi, columnspan=nguess, rowspan=2, sticky="NESW")

for x in range(nguess):
    for n in range(ncombi):
        exec(f'L{x}R{n} = Label(backg, bg="gray", relief=RAISED)')
        exec(f'L{x}R{n}.grid(column={x}, row={n}, sticky="NESW")')
for n in range(ncombi):
    exec(f'A{n} = Label(backg, bg="white", relief=RAISED)')
    exec(f'A{n}.grid(column={nguess}, row={n}, sticky="NESW")')
for x in range(nguess):
    exec(f'K{x} = Label(backg, bg="black", relief=RAISED)')
    exec(f'K{x}.grid(column={x}, row={ncombi}, sticky="NESW")')
    for i in range(2):
        exec(f'K{x}.columnconfigure({i}, weight=1)')
    exec(f'K{x}.rowconfigure(0, weight=1)')
    exec(f'K{x}R = Label(K{x}, bg="red", relief=RAISED, text="0")')
    exec(f'K{x}R.grid(column=0, row=0, sticky="NESW")')
    exec(f'K{x}W = Label(K{x}, bg="white", relief=RAISED, text="0")')
    exec(f'K{x}W.grid(column=1, row=0, sticky="NESW")')

Guess = []
nx = 0

def AddColor(n):
    if len(Guess) < ncombi:
        Guess.append(n)
        exec(f'L{nx}R{len(Guess)-1}.config(bg="{n}")')

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
def submit():
    global nx
    if len(Guess) == ncombi:
        SV = game.tjekFarve(Guess)
        exec(f'K{nx}R.config(text="{SV[0]}")')
        exec(f'K{nx}W.config(text="{SV[1]}")')
        for i in range(len(Guess)):
            Guess.pop(0)
        nx += 1
def delete():
    if len(Guess) > 0:
        Guess.pop(-1)
        exec(f'L{nx}R{len(Guess)}.config(bg="gray")')

green = Button(gui, bg="dark green", command=AddGreen)
green.grid(column=0, row=ncombi, sticky="NESW")
red = Button(gui, bg="dark red", command=AddRed)
red.grid(column=1, row=ncombi, sticky="NESW")
yellow = Button(gui, bg="yellow", command=AddYellow)
yellow.grid(column=1, row=ncombi+1, sticky="NESW")
blue = Button(gui, bg="dark blue", command=AddBlue)
blue.grid(column=0, row=ncombi+1, sticky="NESW")
purple = Button(gui, bg="purple", command=AddPurple)
purple.grid(column=2, row=ncombi+1, sticky="NESW")
white = Button(gui, bg="white", command=AddWhite)
white.grid(column=2, row=ncombi, sticky="NESW")
guess = Button(gui, bg="black", command=submit, text="submit guess", fg="white")
guess.grid(column=3, row=ncombi+1, sticky="NESW")
remove = Button(gui, bg="black", command=delete, text="remove last", fg="white")
remove.grid(column=3, row=ncombi, sticky="NESW")

gui.mainloop()

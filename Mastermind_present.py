from tkinter import *

gui = Tk()
gui.title("MustardMind")
gui.geometry("1000x500")
for i in range(10):
    gui.columnconfigure(i, weight=2)
for i in range(4):
    gui.rowconfigure(i, weight=2)
for i in range(2):
    gui.rowconfigure(i+4, weight=1)

backg = Label(gui, bg="grey")
backg.grid(column=0, row=0, columnspan=10, rowspan=4,sticky="NESW")
UI = Label(gui, bg="black")
UI.grid(column=0, row=4, columnspan=10, rowspan=2, sticky="NESW")



gui.mainloop()

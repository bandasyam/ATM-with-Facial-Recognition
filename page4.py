from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def screen4(fourthpage):
    fourthpage.title("ICFAI BANK")
    fourthpage.geometry("700x500+200+150")
    tqlabel = Label(fourthpage, text = "Thank you... for banking with us", font=("Times_New_Roman",25))
    tqlabel.place(x = 120, y = 70)
    # homebutton = Button(fourthpage, text="Next page", width=20, command=lambda: change(fourthpage))
    # homebutton.place(x=500, y=450)


def page4():
    fourthpage = Tk()
    screen4(fourthpage)
    fourthpage.mainloop()
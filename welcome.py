from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from page2 import *
from page3 import *


def change(mainpage):
    mainpage.destroy()
    page2()


def start(mainpage):
    mainpage.title("ICFAI BANK")
    mainpage.geometry("700x500+200+150")
    l1 = Label(mainpage, text='Welcome to ICFAI BANK', font=("Times_New_Roman",25))
    l1.place(x=120, y=70)
    button1 = Button(mainpage, text="Next page", width=20, command=lambda :change(mainpage))
    button1.place(x=500, y=450)


def main():
    mainpage = Tk()
    start(mainpage)
    mainpage.mainloop()


# def start(mainpage):
#     mainpage.title("ICFAI BANK")
#     mainpage.geometry("700x500+200+150")
#     l1 = Label(mainpage, text='Welcome to ICFAI BANK', font=("Times_New_Roman",25))
#     l1.place(x=170, y=30)
#     button1 = Button(mainpage, text="Next page", width=20, command=lambda :change(mainpage))
#     button1.place(x=500, y=450)


    # button1.pack()    button.pack() places button at the center of the page


# def change(mainpage):
#     mainpage.destroy()
#     page2()


main()


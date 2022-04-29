from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from page2 import *
from dbms import *
from page4 import *

username = ""
password = ""


def change(thirdpage):
    thirdpage.destroy()
    page4()


def screen3(thirdpage, username, password):
    def withdraw(username, password):
        withdrawamount = int(withdrawEntry.get())
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Blssal@77805", database="icfaibank")

        if mydb.is_connected():
            print("Connection successful")
        cursor = mydb.cursor()
        selectquery = "update users set accamount = accamount - %s where username = %s and passwd = %s"
        cursor.execute(selectquery, [(withdrawamount), (username), (password)])

        selectquery2 = "select accamount from users where username = %s and passwd = %s"
        cursor.execute(selectquery2, [(username), (password)])
        results = cursor.fetchall()

        print("Withdrawal amount is : ",withdrawamount)
        print(results)

        global withdrawsuccesslabel
        withdrawsuccesslabel = Label(thirdpage, text="Amount Rs.%d has been debited "%(withdrawamount), font=("Times_New_Roman", 12), fg="red")
        withdrawsuccesslabel.place(x=250, y=250)

        mydb.commit()
        cursor.close()
        mydb.close()


    def cashDeposit(username, password):
        # print("username in 3rd page in fn2 ", username, password)
        # username = username
        # password = password
        depositamount = int(cashdepositEntry.get())
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Blssal@77805", database="icfaibank")

        if mydb.is_connected():
            print("Connection successful")
        cursor = mydb.cursor()

        selectquery = "update users set accamount = accamount + %s where username = %s and passwd = %s"
        cursor.execute(selectquery, [(depositamount), (username), (password)])

        selectquery2 = "select accamount from users where username = %s and passwd = %s"
        cursor.execute(selectquery2, [(username), (password)])

        results = cursor.fetchall()

        global depositsuccesslabel
        if withdrawsuccesslabel.winfo_exists():
            withdrawsuccesslabel.destroy()

        depositsuccesslabel = Label(thirdpage, text="Amount Rs.%d has been credited " % (depositamount),font=("Times_New_Roman", 12), fg = "green")
        depositsuccesslabel.place(x=250, y=250)
        print("The amount deposited is : ",depositamount)
        print(results)

        mydb.commit()
        cursor.close()
        mydb.close()


    def checkBalance(username, password):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Blssal@77805", database="icfaibank")

        if mydb.is_connected():
            print("Connection successful")
        cursor = mydb.cursor()
        selectquery = "select accamount from users where username = %s and passwd = %s"
        cursor.execute(selectquery, [(username), (password)])
        results = cursor.fetchall()

        global balancesuccesslabel
        if depositsuccesslabel.winfo_exists():
            depositsuccesslabel.destroy()
        if withdrawsuccesslabel.winfo_exists():
            withdrawsuccesslabel.destroy()
        for i in results:
            balancesuccesslabel = Label(thirdpage, text="Your balance is Rs.%d " % (i[0]), font=("Times_New_Roman", 12))
            balancesuccesslabel.place(x=250, y=250)
            print("Your balance is : ", i[0])
        # balancesuccesslabel = Label(thirdpage, text="Amount in your account is %d" % (depositamount),font=("Times_New_Roman", 12))
        # balancesuccesslabel.place(x=250, y=250)
        # print("The amount deposited is : ", depositamount)


        cursor.close()
        mydb.close()


    thirdpage.title("ICFAI BANK")
    thirdpage.geometry("700x500+200+150")

    withdrawlabel = Label(thirdpage, text="Withdraw : ", width=20)
    withdrawlabel.place(x=10, y=30)

    withdrawEntry = Entry(thirdpage, font=("Times_New_Roman", 12))
    withdrawEntry.place(x=200, y=30)

    withdrawButton = Button(thirdpage, text="Withdraw", width=20,command = lambda :withdraw(username, password))
    withdrawButton.place(x=460, y=30)


    cashdepositlabel = Label(thirdpage, text="Cash deposit : ", width=20)
    cashdepositlabel.place(x=10, y=100)

    cashdepositEntry = Entry(thirdpage, font=("Times_New_Roman", 12))
    cashdepositEntry.place(x=200, y=100)

    cashdeposit = Button(thirdpage, text="Cash Deposit", width=20, command = lambda:cashDeposit(username, password))
    cashdeposit.place(x=460, y=100)

    checkbalanceButton = Button(thirdpage, text="Check balance : ", width=20, command = lambda:checkBalance(username, password))
    checkbalanceButton.place(x=10, y=170)

    button1 = Button(thirdpage, text="Log out", width=20, command=lambda: change(thirdpage))
    button1.place(x=500, y=450)

    # button1 = Button(thirdpage, text="Withdraw", width=20)
    # button1.place(x=10, y=30)


def page3(uname,passwd):
    global username
    global password
    username = username + uname
    password = password + passwd
    print("This is in page 3 :", username,password)
    thirdpage = Tk()
    screen3(thirdpage, username, password)
    thirdpage.mainloop()


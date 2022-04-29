from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from page3 import *
from opencvwebcam import *
from dbms import *


uname = ""
passwd = ""


def change(secondpage):
    print("This is in change(secondpage)", uname, passwd)
    secondpage.destroy()
    page3(uname, passwd)


def screen2(secondpage):
    def opencv():
        global uname
        global passwd
        uname = uname_Entry.get()
        passwd = passwd_Entry.get()
        print("uname is : ", uname, "\npasswd is : ", passwd)

        selectquery = "select * from users where username = %s and passwd = %s"
        cursor.execute(selectquery, [(uname), (passwd)])
        results = cursor.fetchall()
        print("The database result is : ",results)

        global labelverifynotid
        if not results:
            labelverifynotid = Label(secondpage, text="user id and password is not Verified ", font=("Times_New_Roman", 12))
            labelverifynotid.place(x=250, y=270)

        if results:
            print("Username and password is in database")
            labelverifiedid = Label(secondpage, text="User id and password is Verified ", font=("Times_New_Roman", 12))
            labelverifiedid.place(x=250, y=270)

            global list
            everything()
            if True in list[0]:
                label_verifiedfaceid = Label(secondpage, text="Face ID is Verified ", font=("Times_New_Roman", 12))
                label_verifiedfaceid.place(x=250, y=300)
                button1['state'] = NORMAL
            else:
                label_verifiedfaceid = Label(secondpage, text="Face ID is Not Verified ", font=("Times_New_Roman", 12))
                label_verifiedfaceid.place(x=250, y=300)

        # cursor.close()
        # mydb.close()

    # def change(secondpage):
    #     print("This is in 2nd page function...",uname, passwd)
    #     secondpage.destroy()
    #     page3(uname,passwd)


        # everything()
        # if True in list[0]:
        #     label_verifiedfaceid = Label(secondpage, text="Face ID is Verified ", font=("Times_New_Roman", 12))
        #     label_verifiedfaceid.place(x=250, y=270)
        # else:
        #     label_verifiedfaceid = Label(secondpage, text="Face ID is Not Verified ", font=("Times_New_Roman", 12))
        #     label_verifiedfaceid.place(x=250, y=270)


    secondpage.title("ICFAI BANK")
    secondpage.geometry("700x500+200+150")

    label_yourname = Label(secondpage, text="Enter your name : ", font=("Times_New_Roman", 12))
    label_yourname.place(x=0, y=20)

    uname_Entry = Entry(secondpage, font=("Times_New_Roman", 12))
    uname_Entry.place(x=200, y=20)

    label_yourpassword = Label(secondpage, text="Enter your password : ", font=("Times_New_Roman", 12))
    label_yourpassword.place(x=0, y=100)

    passwd_Entry = Entry(secondpage, font=("Times_New_Roman", 12))
    passwd_Entry.place(x=200, y=100)

    button_verfyfaceid = Button(secondpage, text = "Verify", font=("Times_New_Roman", 12), command=opencv)
    button_verfyfaceid.place(x=250, y=200)

    button1 = Button(secondpage, text="Nextpage", width=20, command=lambda : change(secondpage))
    button1.place(x=500, y=450)  # Here we wrote lambda change(secondpage) because the mentioned function is outside this function.
    button1['state'] = DISABLED

    # uname = uname_Entry.get()
    # passwd = passwd_Entry.get()
    # print("u,p is : ",uname, passwd)

    # button_nameverify = Button(secondpage, text = "Verify userid passwd", font=("Times_New_Roman", 12), command=verify)
    # button_nameverify.place(x=350, y=450)


    # l1 = Label(root, text='This is Second page', font=("Times_New_Roman", 25))
    # l1.pack()


def page2():
    secondpage = Tk()
    screen2(secondpage)
    secondpage.mainloop()


# def screen2(secondpage):
#     def opencv():
#         # mydb = mysql.connector.connect(host="localhost", user="root", passwd="Blssal@77805", database="icfaibank")
#         #
#         # if mydb.is_connected():
#         #     print("Connection successful")
#         # cursor = mydb.cursor()
#         # selectquery = "select * from users"
#         # cursor.execute(selectquery)
#         # results = cursor.fetchall()
#         # print(results)   # This prints all the details as a tuple
#         # for i in results:
#         #     print(i[0])  # This prints the all the details of the first column in the table line by line in terminal
#
#         global uname
#         global passwd
#         uname = uname_Entry.get()
#         passwd = passwd_Entry.get()
#         print("uname is : ", uname, "\npasswd is : ", passwd)
#
#         selectquery = "select * from users where username = %s and passwd = %s"
#         cursor.execute(selectquery, [(uname), (passwd)])
#         results = cursor.fetchall()
#         print("The database result is : ",results)
#
#         if results:
#             print("Username and password is in database")
#             label_verifiedid = Label(secondpage, text="User id and password is Verified ", font=("Times_New_Roman", 12))
#             label_verifiedid.place(x=250, y=270)
#
#             global list
#             everything()
#             if True in list[0]:
#                 label_verifiedfaceid = Label(secondpage, text="Face ID is Verified ", font=("Times_New_Roman", 12))
#                 label_verifiedfaceid.place(x=250, y=300)
#             else:
#                 label_verifiedfaceid = Label(secondpage, text="Face ID is Not Verified ", font=("Times_New_Roman", 12))
#                 label_verifiedfaceid.place(x=250, y=300)
#
#         else:
#             label_verifiedid = Label(secondpage, text="user id and password is not Verified ", font=("Times_New_Roman", 12))
#             label_verifiedid.place(x=250, y=270)
#
#         cursor.close()
#         mydb.close()
#
#
#
#         # everything()
#         # if True in list[0]:
#         #     label_verifiedfaceid = Label(secondpage, text="Face ID is Verified ", font=("Times_New_Roman", 12))
#         #     label_verifiedfaceid.place(x=250, y=270)
#         # else:
#         #     label_verifiedfaceid = Label(secondpage, text="Face ID is Not Verified ", font=("Times_New_Roman", 12))
#         #     label_verifiedfaceid.place(x=250, y=270)
#
#
#     secondpage.title("ICFAI BANK")
#     secondpage.geometry("700x500+200+150")
#
#     label_yourname = Label(secondpage, text="Enter your name : ", font=("Times_New_Roman", 12))
#     label_yourname.place(x=0, y=20)
#
#     uname_Entry = Entry(secondpage, font=("Times_New_Roman", 12))
#     uname_Entry.place(x=200, y=20)
#
#     label_yourpassword = Label(secondpage, text="Enter your password : ", font=("Times_New_Roman", 12))
#     label_yourpassword.place(x=0, y=100)
#
#     passwd_Entry = Entry(secondpage, font=("Times_New_Roman", 12))
#     passwd_Entry.place(x=200, y=100)
#
#     button_verfyfaceid = Button(secondpage, text = "Verify", font=("Times_New_Roman", 12), command=opencv)
#     button_verfyfaceid.place(x=250, y=200)
#
#     button1 = Button(secondpage, text="Nextpage", width=20, command=lambda: change(secondpage)) # Here we wrote lambda change(secondpage) because the mentioned function is outside this function.
#     button1.place(x=500, y=450)
#
#     # uname = uname_Entry.get()
#     # passwd = passwd_Entry.get()
#     # print("u,p is : ",uname, passwd)
#
#     # button_nameverify = Button(secondpage, text = "Verify userid passwd", font=("Times_New_Roman", 12), command=verify)
#     # button_nameverify.place(x=350, y=450)
#
#
#     # l1 = Label(root, text='This is Second page', font=("Times_New_Roman", 25))
#     # l1.pack()


# def change(secondpage):
#     print(uname, passwd)
#     secondpage.destroy()
#     page3()
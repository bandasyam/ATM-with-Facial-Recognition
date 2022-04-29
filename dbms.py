import mysql.connector


mydb = mysql.connector.connect(host="localhost", user="root", passwd="Blssal@77805",database="icfaibank")

if mydb.is_connected():
    print("Connection successful")
cursor = mydb.cursor()


# mydb = mysql.connector.connect(host="localhost", user="root", passwd="Blssal@77805", database="icfaibank")
        #
        # if mydb.is_connected():
        #     print("Connection successful")
        # cursor = mydb.cursor()
        # selectquery = "select * from users"
        # cursor.execute(selectquery)
        # results = cursor.fetchall()
        # print(results)   # This prints all the details as a tuple
        # for i in results:
        #     print(i[0])  # This prints the all the details of the first column in the table line by line in terminal



# selectquery = "select * from users"
# cursor.execute(selectquery)
# records = cursor.fetchall()
# print("No.of records in the table are : ",cursor.rowcount)
#
# for i in records:
#     print("id : ",i[0])
#     print("name : ",i[1])
#     print("passwd : ",i[2])



# import sqlite3
#
# conn = sqlite3.connect('icfaibank.db')

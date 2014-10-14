import mysql.connector
import time
import os
import datetime

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

while True:

        cls()

        cnx = mysql.connector.connect(user='root', password='potatowithsalt', host='127.0.0.1', database='wehavecake', port='3306')

        cursor = cnx.cursor()

        query = ("SELECT Node1, Start, Username, ID  FROM routes ")

        cursor.execute(query)

        for (Node1, Start, Username, ID) in cursor:
                print("Username: " + str(Username) + " |UniqueID: " + str(ID))
                print("Time: " + str(Start) + " Node: " + str(Node1))
                print("")

        print("")
        print('Last update: ' + str(datetime.datetime.now()))
        cursor.close()
        cnx.close()

        time.sleep(60) 

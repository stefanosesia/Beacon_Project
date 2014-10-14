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

        query = ("SELECT User1, User2 FROM friendship ")

        cursor.execute(query)

        for (User1, User2) in cursor:
                print("User1: " + str(User1) + " |User2:  " + str(User2))
		print("")

        print("")
        print('Last update: ' + str(datetime.datetime.now()))
	cursor.close()
        cnx.close()
	
        time.sleep(60)

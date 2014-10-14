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

        query = ("SELECT Username, HashPass, Email, CurrentLocation  FROM user ")

        cursor.execute(query)

        for (Username, HashPass, Email, CurrentLocation) in cursor:
                print("Username: " + str(Username) + " |Pass: " + str(HashPass))
                print("Email: " + str(Email) + " Location: " + str(CurrentLocation))
		print("")

        print("")
        print('Last update: ' + str(datetime.datetime.now()))
	cursor.close()
        cnx.close()
	
        time.sleep(60)

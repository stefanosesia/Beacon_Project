import mysql.connector
import hashlib
import datetime

username = raw_input("Enter username: ")
node = raw_input("Enter node BSSID: ")
time = datetime.datetime.now()
ID = 0
ID = int(input("Enter unique ID (ie. next UID in chain - use getRoute.py to view UIDs): "))

cnx = mysql.connector.connect(user='root', password='potatowithsalt', host='127.0.0.1', database='wehavecake', port='3306')

cursor = cnx.cursor()

add_route = ("INSERT INTO routes "
              "(Node1, Start, Username, ID) "
              "VALUES (%(node)s, %(time)s, %(username)s, %(ID)s)")

data_route = {
  'node': node,
  'time': time,
  'username': username,
  'ID': ID,
}


cursor.execute(add_route, data_route)

cnx.commit()

cursor.close()
cnx.close()

print("Success")

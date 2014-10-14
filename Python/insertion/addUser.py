import mysql.connector
import hashlib

username = raw_input("Enter username: ")
hashpass = raw_input("Enter password: ")

hashpass = hashlib.sha224(hashpass).hexdigest()

email = raw_input("Enter email: ")
       
cnx = mysql.connector.connect(user='root', password='potatowithsalt', host='127.0.0.1', database='wehavecake', port='3306')

cursor = cnx.cursor()

add_user = ("INSERT INTO user "
              "(Username, HashPass, Email, CurrentLocation) "
              "VALUES (%(Username)s, %(HashPass)s, %(Email)s, %(CurrentLocation)s)")

data_user = {
  'Username': username,
  'HashPass': hashpass,
  'Email': email,
  'CurrentLocation': '00:00:00:00:00:00',
}


cursor.execute(add_user, data_user)

cnx.commit()

print(str(add_user))
print("")
print(str(data_user))
print("")

cursor.close()
cnx.close()

print("Success")

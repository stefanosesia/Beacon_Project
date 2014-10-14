import mysql.connector
import hashlib

User1 = raw_input("Enter user1: ")
User2 = raw_input("Enter user2: ")


cnx = mysql.connector.connect(user='root', password='potatowithsalt', host='127.0.0.1', database='wehavecake', port='3306')


cursor = cnx.cursor()


add_friendship = ("INSERT INTO friendship "
              "(User1, User2) "
              "VALUES (%(User1)s, %(User2)s)")

data_friendship = {
  'User1': User1,
  'User2': User2,
}


cursor.execute(add_friendship, data_friendship)

cnx.commit()

cursor.close()
cnx.close()

print("Success")

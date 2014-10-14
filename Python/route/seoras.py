import mysql.connector
from datetime import datetime

class route():

	Node = '00:00:00:00:00:00:'
	Time = "2014-01-01 00:00:00"

def getUserNames():
	cnx = mysql.connector.connect(user='root', password='potatowithsalt', host='127.0.0.1', database='wehavecake', port='3306')
        cursor = cnx.cursor()

        query = ("SELECT Username FROM user ")
        cursor.execute(query)
        userNames = []
        for Username in cursor:
                userNames.append(str(Username[0]))

        cursor.close()
        cnx.close()
	
        return userNames

	
def printColumn():

	cnx = mysql.connector.connect(user='root', password='potatowithsalt', host='127.0.0.1', database='wehavecake', port='3306')
        cursor = cnx.cursor()

        query = ("SELECT Username, Node1, Start  FROM routes")
        cursor.execute(query)

        userNames = []
        for Username in cursor:
                userNames.append(str(Username))

        cursor.close()
        cnx.close()
	
        print userNames

def populate():

	cnx = mysql.connector.connect(user='root', password='potatowithsalt', host='127.0.0.1', database='wehavecake', port='3306')
        cursor = cnx.cursor()
	
	userArray = getUserNames()
	
	#for i in userArray:
	query = ("INSERT INTO routes (Username, Node1, Start) VALUES (\"stefano\", \"00:00:00:00:00:00\", \"2014-01-01 00:00:00\")")
	cursor.execute(query)


if __name__ == '__main__':

	print(getUserNames())
	populate()
	printColumn()

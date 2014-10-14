import mysql.connector
import time

def getUserInfo():

	cnx = mysql.connector.connect(user='root', password='potatowithsalt', host='127.0.0.1', database='wehavecake', port='3306')

	cursor = cnx.cursor()

	query = ("SELECT Username, HashPass, Email, CurrentLocation  FROM user ")

	cursor.execute(query)

	for (Username, HashPass, Email, CurrentLocation) in cursor:
		print("Username: " + str(Username) + " |Pass: " + str(HashPass))
		print("Email: " + str(Email) + " Location: " + str(CurrentLocation))

	print("")
	cursor.close()
	cnx.close()

	time.sleep(5)

def updateFriendsList(friend1, friend2):

	friend1 = []
	friend2 = []

	cnx = mysql.connector.connect(user='root', password='potatowithsalt', host='127.0.0.1', database='wehavecake', port='3306')

        cursor = cnx.cursor()

        query = ("SELECT user1, user2  FROM friendship ")

        cursor.execute(query)

        for (user1, user2) in cursor:
		friend1.append(str(user1))
		friend2.append(str(user2))	
		

        cursor.close()
        cnx.close()
	
	if len(friend1) == 0:
		print("NO FRIENDS IN DATABASE")
		return("NO FRIENDS")
	else:
		print("Successfully Updated Friends List")
		return

def updateUserLocations(LocationUsername, LocationNodeNum):

	LocationUsername = []
	LocationNodeNum = []

        cnx = mysql.connector.connect(user='root', password='potatowithsalt', host='127.0.0.1', database='wehavecake', port='3306')

        cursor = cnx.cursor()

        query = ("SELECT Username, CurrentLocation FROM user")

        cursor.execute(query)

        for (Username, CurrentLocation) in cursor:
                LocationUsername.append(str(Username))
                LocationNodeNum.append(str(CurrentLocation))


        cursor.close()
        cnx.close()

        if len(location) == 0:
                print("NO LOCATION DATA IN DATABASE")
                return("FAILURE")
        else:
                print("Successfully Updated location data")
                return("SUCCESS")


def main():
	
	friends1 = []
	friends2 = []

	LocationUsername = []
	LocationNodeNum = []

	while True:	

		updateFriendsList(friends1, friends2)
		updateUserLocations(LocationUsername, LocationNodeNum)

		file1 = open("~/pyServerLogs/friends.txt", "w")
		file2 = open("~/pyServerLogs/locations.txt", "w")

		for i in range(0, len(friends1)-1):
			file1.write(friends1[i] + ":" + friends2[i] + "\n")
	
		for j in range(0, len(LocationUsername)-1):
			file2.write(LocationUsername[j] + ":" + LocationNodeNum[j] + "\n")
		
		time.sleep(300)

getUserInfo()

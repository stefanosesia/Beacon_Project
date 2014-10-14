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

def updateFriendsList():

	friend = []

	cnx = mysql.connector.connect(user='root', password='potatowithsalt', host='127.0.0.1', database='wehavecake', port='3306')

        cursor = cnx.cursor()

        query = ("SELECT user1, user2  FROM friendship ")

        cursor.execute(query)

        for (user1, user2) in cursor:
		friend.append(str(user1) + "|" + str(user2))
	
	

        cursor.close()
        cnx.close()
	
	return friend

	#if len(friend1) == 0:
	#	print("NO FRIENDS IN DATABASE")
	#	return "NO FRIENDS"
	#else:
	#	print("Successfully Updated Friends List")
	#	return "SUCCESS"

def updateUserLocations():
	location = []
        cnx = mysql.connector.connect(user='root', password='potatowithsalt', host='127.0.0.1', database='wehavecake', port='3306')

        cursor = cnx.cursor()

        query = ("SELECT Username, CurrentLocation FROM user")

        cursor.execute(query)

        for (Username, CurrentLocation) in cursor:
                location.append(str(Username) + "|" + str(CurrentLocation))


        cursor.close()
        cnx.close()

        return location

def main():

	
	while True:

		friends1 = []
		friends2 = []

		locationUsername = []
		locationNodeNum = []
	

		friends0 = updateFriendsList()
		location0 = updateUserLocations()
			
		#print(str(friends0))
		#print(str(location0))

		for i in range(0, len(friends0)):
			friends1.append(friends0[i].split("|")[0])
			friends2.append(friends0[i].split("|")[1])

		for i in range(0, len(location0)):
			locationUsername.append(location0[i].split("|")[0])
			locationNodeNum.append(location0[i].split("|")[1])

		#print(str(friends1))
		#print(str(friends2))
		#print(str(locationUsername))
		#print(str(locationNodeNum))
	
		location1 = ''
		location2 = ''
		
		locationFriends1 = []
		locationFriends2 = []
		

		for i in range(0, len(friends1)):
			for j in range(0, len(locationUsername)):
				#print(str(friends1[i]) +str(locationUsername[j]))
				if friends1[i] == locationUsername[j]:
					location1 = locationNodeNum[j]
				if friends2[i] == locationUsername[j]:
					location2 = locationNodeNum[j]

			if location1 == location2:
				locationFriends1.append(friends1[i])
				locationFriends2.append(friends2[i])
	
		for i in range(0, len(locationFriends1)):
			print('NEARBY FRIENDS: ' + locationFriends1[i] + ' & ' + locationFriends2[i])
			
		time.sleep(300)

main()

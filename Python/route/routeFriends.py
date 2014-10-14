import mysql.connector
import datetime

#Route class (redundant?)
class route():
	
	Node = '00:00:00:00:00:00'
	
	Time = "2014-01-01 00:00:00"

	Username = ""

	UID = 0

#Function that returns an array of Usernames from the mySQL server
def getUsernames():

	#Seoras
	#Return array of usernames

	cnx = mysql.connector.connect(user='root', password='potatowithsalt', host='127.0.0.1', database='wehavecake', port='3306')
        cursor = cnx.cursor()

        query = ("SELECT Username, HashPass, Email, CurrentLocation  FROM user ")
        cursor.execute(query)

        userNames = []
        for (Username, HashPass, Email, CurrentLocation) in cursor:
                userNames.append(str(Username))

        cursor.close()
        cnx.close()

        return userNames

#Gets the routes (points...) from the database and returns an array (list) of points the specified user visited. only the specific user's routes are returned because the SQL demands only a specific user
def getRoutes(USER): #UPDATE DATABASE *Done*

	cnx = mysql.connector.connect(user='root', password='potatowithsalt', host='127.0.0.1', database='wehavecake', port='3306')
        cursor = cnx.cursor()

        query = ("SELECT Node1, Start, Username, ID FROM routes "
		"WHERE Username='" + USER + "'")

        cursor.execute(query)

        routes = []
	currentRoute = route()	

        for (Node1, Start, Username, ID) in cursor:
                currentRoute.Node = Node1
		currentRoute.Time = Start
		currentRoute.Username = Username
		currentRoute.ID = ID
		#print(str(currentRoute.Node))
		#print(str(currentRoute.Time))
		#print(str(currentRoute.Username))
		#print(str(currentRoute.ID))


		routes.append(currentRoute)
	
        cursor.close()
        cnx.close()

        return routes

#this sub takes in an array of routes (points) and returns a string of the node identifiers
def stringify(routes):
	
	stringy = ""

	for k in range(0, len(routes)-1):
		stringy = stringy + routes[k].Node.replace(":", "")
	#print stringy
	return stringy 	

#This trio of subs is used to try and identify how similar a pair of route strings are.
#finds longest common substring. From http://stackoverflow.com/questions/2892931/longest-common-substring-from-more-than-two-strings-python by jtjacques
def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

#Used by long_substr. Also by jtjacques
def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True

def similarity(string1, string2):

	#Find the longest common substring and use this as a factor of similarity:
	#If the day's routes contain a 40% match on the longest substring, then a match is reccomended.
	
	longest_substring = long_substr([string1,string2])
	
	ratio = (len(longest_substring)/((len(string1)+len(string2))/2) * 100)
	#print("Ratio: " +str(ratio))
	if ratio  > 39:
		return True
	else:
		return False

def addFriends(user1, user2):
	cnx = mysql.connector.connect(user='root', password='potatowithsalt', host='127.0.0.1', database='wehavecake', port='3306')

	cursor = cnx.cursor()

	add_user = ("INSERT INTO friendship "
        	   "(User1, User2) "
              	   "VALUES (%(User1)s, %(User2)s)")

	data_user = {
  	'User1': user1,
  	'User2': user2,
	}


	cursor.execute(add_user, data_user)

	cnx.commit()

	cursor.close()
	cnx.close()

def main():
 	
	while True:

		usernames = getUsernames()

		#print(str(usernames))
	
		for i in range(0, len(usernames)):
			for j in range(i, len(usernames)):
				if usernames[i] != usernames[j]:
					string1 = stringify(getRoutes(usernames[i]))
					#string2 = stringify(getRoutes(usernames[i]))
					string2 = stringify(getRoutes(usernames[j]))
					if similarity(string1, string2):
						print("Match found! " + usernames[i] + ' & ' + usernames[j])
						addFriends(usernames[i], usernames[j])

		print("Completeed updating.")
			

main()








		





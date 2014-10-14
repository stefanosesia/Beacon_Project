while True:
        socit = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socit.bind((host, port))
        print("#Listening")
        socit.listen(1)

        conn, addr = socit.accept()
    
        print("#Connected by: ", addr)
    
        while True:
            data = repr(conn.recv(1024))
            data = str(data)
            while not data == "":

                    #Data of form "RequestType||$Username||$passwordHash||$MacAddressofBeacon"
                
                splitInfo = data.split("||")
		requesttype = splitInfo[0]
                username = splitInfo[1]
                passwordhash = splitInfo[2]
                macAddress = splitInfo[3]

		#Now check password hash against database

		cnx = mysql.connector.connect(user='root', password='potatowithsalt', host='127.0.0.1', database='wehavecake', port='3306')

        	cursor = cnx.cursor()

        	query = ("SELECT Username, HashPass, Email, CurrentLocation  FROM user ")
		
        	cursor.execute(query)
		
		passwordOK = False

        	for (Username, HashPass, Email, CurrentLocation) in cursor:		
			if (HashPass = passwordhash) and (Username = inputusername):
				passwordOK = True

		if passwordOK = True:
			#Add mac address to database
		

		cursor.close()
        	cnx.close()

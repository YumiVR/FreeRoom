#FreeRoom Hosted at ---> https://github.com/YumiVR/FreeRoom.git 
#By Yumi Verma 

import sys
 
username = 'root'
password = 'root' 

valid = 0
loginvalid = 0

print ("Welcome To FreeRoom V 0.0.1")

while loginvalid == 0:
	try:
		usernameinput = input ("Username >")
		passwordinput = input ("Password >")
		print ("")
		loginvalid = 1
	except:
		print ("Error Try again!")
		print("")

if usernameinput == username and passwordinput == password:
	print ("welcome", username)
	print ("Type help for a list of commands")
	print ("")


	while valid == 0:
				
		userinputfield = input (">")

		if userinputfield == 'help':
			print ("help	- Display this page")
			print ("exit	- To terminate the program now")
			print ("rooms	- Display rooms in the database")
			print ("mk	- Create a Room ")
			print ("rm	- Remove a room")
			print ("active 	- Display Online Rooms")
			print ("edit 	- edit a room's prefrences")
			print("")

		elif userinputfield == 'exit':
			print("Shutting down! ")
			print("Program exited")
			print("")
			sys.exit()	 

		elif userinputfield == 'rooms':
			print ("List of Rooms in Orginisation")
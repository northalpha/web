"""picdumpchecker.py
author: https://twitter.com/northalpha
desc: A simple web checker if the picdump from www.bildschirmarbeiter.com is beeing uploaded, if yes: send me an email"""

import time
import requests
import smtplib

### Config ###

my_email = "mymailadresse@gmail.com"
my_pass = "super_secret_in_here"

#Lets create some URL
picdump_url = "http://www.bildschirmarbeiter.com/pic/bildschirmarbeiter_-_picdump_" + time.strftime("%d.%m.%Y") 

#Check if the Day is Day 5 in week == Friday
if (time.strftime("%w")) == "5":

	#Lets get that URLs
	r = requests.get(picdump_url)

	def sendMail(msg, url):

        	#Create an Server Object
        	server = smtplib.SMTP('smtp.gmail.com', 587)

        	#Do the TLS server connection
        	server.starttls()

        	#Next, log in to the server
        	server.login(my_email, my_pass)

        	#Send the mail
        	content = "\n" + msg + " " + url  # The /n separates the message from the headers
        	server.sendmail("picdumpalert@gmail.com", my_email , content)
        	server.quit()

	if r.status_code != 200:
        	print("Oh noes")

	else:
		sendMail("PICDUUUUUUUUUMP", picdump_url)
		print("Oh yes")

else:
		if time.strftime("%A") != "Friday":
			print("There is no Picdump on " + time.strftime("%A") + "s") 
		else:
			print("Already run")

"""picdumpchecker.py
author: https://twitter.com/northalpha
desc: A simple web checker if the picdump from www.bildschirmarbeiter.com is beeing uploaded, if yes: send me an email"""

import os.path
import sys
import time
import requests
import smtplib

### Config ###

my_email = "mymailadresse@gmail.com"
my_pass = "super_secret_in_here"

### Get Time ###
now = time

### Check for Token: if it is there, email was already sent ###
if (os.path.isfile('/tmp/' + now.strftime("%d.%m.%Y") + '.done')):
	sys.exit(0)

### Leave if Today is not a Friday :-( ###
if (now.strftime("%w")) != "5":
	sys.exit(0)

### Today is Friday (Yippee!!!) ###
picdump_url = "http://www.bildschirmarbeiter.com/pic/bildschirmarbeiter_-_picdump_" + now.strftime("%d.%m.%Y") 
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

if r.status_code == 200:
	sendMail("PICDUUUUUUUUUMP", picdump_url)
	# Write Token
	open('/tmp/' + now.strftime("%d.%m.%Y") + '.done', 'a').close()

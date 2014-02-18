"""picdumpchecker.py
author: northalpha
desc: bla"""

import time
import requests
import smtplib

#Wir bauen uns eine URL
picdump_url = "http://www.bildschirmarbeiter.com/pic/bildschirmarbeiter_-_picdump_" + time.strftime("%d.%m.%Y") 

#Wir holen uns di URL
r = requests.get(picdump_url)

def sendMail(msg):

        #Wir bauen uns ein Server Object
        server = smtplib.SMTP('smtp.gmail.com', 587)

        #Do the TLS server connection
        server.starttls()

        #Next, log in to the server
        server.login("meine_email_adresse", "mein_passwort")

        #Send the mail
        content = "\n" + msg + " " + picdump_url  # The /n separates the message from the headers
        server.sendmail("picdumpalert@gmail.com", "meine_email_adresse", content)
        server.quit()

if r.status_code != 200:
        print("Oh yes")
	sendMail("PICDUUUUUUUUUMP")
else:
        #sendMail("Keine URL kein Fun")
	print("Oh noes") 
